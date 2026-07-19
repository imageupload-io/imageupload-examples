# imageupload.io examples

Runnable examples for the [imageupload.io image upload API](https://imageupload.io/image-upload-api) and [MCP server](https://imageupload.io/docs).

imageupload.io accepts PNG, JPEG, WebP, GIF, and AVIF files and returns a share page, direct image URL, and embed codes. Account owners can also choose expiration rules, passwords, folders, and custom slugs according to their plan.

## Quick start

Create an API key in your [imageupload.io profile](https://imageupload.io/dashboard/profile), then export it in your shell. Keep this key private.

```bash
export IMAGEUPLOAD_API_KEY='iu_live_replace_with_your_key'
```

Upload with the cURL example:

```bash
./examples/upload.sh ./photo.png 1d
```

Upload with Node.js 20 or newer:

```bash
node examples/upload.mjs ./photo.png 1d
```

Upload with Python 3.10 or newer, using only the standard library:

```bash
python3 examples/upload.py ./photo.png 1d
```

Each program prints the JSON response returned by the API. A successful response includes `share_url` and `direct_url` values that can be used in browsers, Markdown, forums, or applications.

## Expiration values

The examples accept these expiration modes:

| Value | Behavior |
| --- | --- |
| `1d` | Delete after one day |
| `1w` | Delete after one week |
| `1mo` | Delete after one month |
| `3mo` | Delete after three months on eligible plans |
| `burn` | Delete after the first successful view |
| `views` | Delete after a configured number of unique viewers |
| `forever` | Keep without a scheduled expiry on eligible plans |

See the [complete API documentation](https://imageupload.io/docs) for password protection, view limits, custom expiry dates, folders, custom slugs, quota headers, and response fields.

## MCP setup

The official `@imageupload/mcp` package lets compatible AI clients upload, list, inspect, organize, and delete images using the same account. The package can be run directly with `npx`:

```bash
npx -y @imageupload/mcp
```

Configuration examples for Claude Desktop, Cursor, Windsurf, and other MCP clients are in [mcp/README.md](mcp/README.md).

## Security

- Never commit an API key to source control.
- Prefer an environment variable or the secret store provided by your CI system.
- Rotate a key immediately from your imageupload.io profile if it is exposed.
- Treat returned direct URLs as access links. Add a password or expiration rule when the image is sensitive.
- Validate file paths and upload sources in applications that accept user-controlled input.

The examples deliberately read the key only from `IMAGEUPLOAD_API_KEY`. They do not write credentials to disk or print the key.

## More guides

- [Free image hosting](https://imageupload.io/free-image-hosting)
- [Temporary image hosting](https://imageupload.io/temporary-image-hosting)
- [Anonymous image hosting and its limits](https://imageupload.io/anonymous-image-hosting)
- [Image upload API guide](https://imageupload.io/image-upload-api)
- [API and MCP reference](https://imageupload.io/docs)

## License

MIT. See [LICENSE](LICENSE).
