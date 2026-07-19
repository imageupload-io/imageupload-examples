#!/usr/bin/env bash
set -euo pipefail

api_key="${IMAGEUPLOAD_API_KEY:-}"
file_path="${1:-}"
expiration="${2:-1d}"

if [[ -z "$api_key" ]]; then
  echo "Set IMAGEUPLOAD_API_KEY before running this example." >&2
  exit 1
fi

if [[ -z "$file_path" || ! -f "$file_path" ]]; then
  echo "Usage: $0 /path/to/image.png [1d|1w|1mo|3mo|burn|views|forever]" >&2
  exit 1
fi

curl --fail-with-body --silent --show-error \
  --request POST \
  --header "Authorization: Bearer ${api_key}" \
  --form "file=@${file_path}" \
  --form "expiration=${expiration}" \
  https://imageupload.io/api/upload

printf '\n'
