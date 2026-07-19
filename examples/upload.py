#!/usr/bin/env python3
"""Upload one image to imageupload.io using only the Python standard library."""

from __future__ import annotations

import json
import mimetypes
import os
from pathlib import Path
import secrets
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def multipart_body(file_path: Path, expiration: str, boundary: str) -> bytes:
    mime = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
    allowed = {"image/png", "image/jpeg", "image/webp", "image/gif", "image/avif"}
    if mime not in allowed:
        raise ValueError("Supported formats: PNG, JPEG, WebP, GIF, and AVIF")

    chunks = [
        f"--{boundary}\r\n".encode(),
        b'Content-Disposition: form-data; name="expiration"\r\n\r\n',
        expiration.encode(),
        b"\r\n",
        f"--{boundary}\r\n".encode(),
        f'Content-Disposition: form-data; name="file"; filename="{file_path.name}"\r\n'.encode(),
        f"Content-Type: {mime}\r\n\r\n".encode(),
        file_path.read_bytes(),
        b"\r\n",
        f"--{boundary}--\r\n".encode(),
    ]
    return b"".join(chunks)


def main() -> int:
    api_key = os.environ.get("IMAGEUPLOAD_API_KEY", "")
    if not api_key:
        print("Set IMAGEUPLOAD_API_KEY before running this example.", file=sys.stderr)
        return 1

    if len(sys.argv) < 2:
        print("Usage: python3 examples/upload.py /path/to/image.png [expiration]", file=sys.stderr)
        return 1

    file_path = Path(sys.argv[1]).expanduser()
    if not file_path.is_file():
        print(f"File not found: {file_path}", file=sys.stderr)
        return 1

    expiration = sys.argv[2] if len(sys.argv) > 2 else "1d"
    boundary = "imageupload-" + secrets.token_hex(16)

    try:
        body = multipart_body(file_path, expiration, boundary)
    except (OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1

    request = Request(
        "https://imageupload.io/api/upload",
        method="POST",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "Accept": "application/json",
        },
    )

    try:
        with urlopen(request, timeout=60) as response:
            payload = json.load(response)
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        print(f"Upload failed with HTTP {error.code}: {detail}", file=sys.stderr)
        return 1
    except (URLError, TimeoutError, json.JSONDecodeError) as error:
        print(f"Upload failed: {error}", file=sys.stderr)
        return 1

    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
