# Security policy

## Protect API keys

API keys authorize actions on an imageupload.io account. Store keys in environment variables or a managed secret store. Do not place them in repositories, browser-side JavaScript, screenshots, logs, issue reports, or chat messages.

If a key is exposed, regenerate it immediately from the imageupload.io profile page. Rotation invalidates the previous key.

## Report a vulnerability

Please do not open a public issue for a suspected security vulnerability. Send a concise report to [hello@imageupload.io](mailto:hello@imageupload.io) with reproduction steps, affected endpoints, and the impact you observed. Do not include personal data or files belonging to other users.

Only test accounts and content you own or are authorized to use.
