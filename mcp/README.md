# MCP client configuration

The official [`@imageupload/mcp`](https://www.npmjs.com/package/@imageupload/mcp) package exposes imageupload.io tools to MCP-compatible clients. Create an API key in your imageupload.io profile before adding the server.

## Claude Desktop

Add the server to the `mcpServers` object in the Claude Desktop configuration:

```json
{
  "mcpServers": {
    "imageupload": {
      "command": "npx",
      "args": ["-y", "@imageupload/mcp"],
      "env": {
        "IMAGEUPLOAD_API_KEY": "iu_live_replace_with_your_key"
      }
    }
  }
}
```

Restart Claude Desktop after saving the configuration.

## Cursor and Windsurf

Use the same server definition in the MCP settings for the editor. The command is `npx`, the arguments are `-y` and `@imageupload/mcp`, and the environment contains `IMAGEUPLOAD_API_KEY`.

## Available tools

- `upload_image`: upload an image and return its share and direct URLs
- `list_images`: list account images with pagination and optional folder filtering
- `get_image`: retrieve metadata for an owned image
- `delete_image`: permanently delete an owned image
- `list_folders`: list folders and image counts
- `create_folder`: create a folder
- `get_quota`: inspect the account plan and API quota

Read the [complete MCP documentation](https://imageupload.io/docs) for arguments, response shapes, expiration rules, folder behavior, and troubleshooting.

## Secret handling

MCP configuration files commonly contain environment values in plain text. Restrict access to the configuration file, never commit it, and rotate the API key immediately if the file is exposed.
