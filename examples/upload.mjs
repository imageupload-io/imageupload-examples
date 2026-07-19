#!/usr/bin/env node
import { readFile } from 'node:fs/promises';
import path from 'node:path';

const MIME_BY_EXTENSION = new Map([
  ['.png', 'image/png'],
  ['.jpg', 'image/jpeg'],
  ['.jpeg', 'image/jpeg'],
  ['.webp', 'image/webp'],
  ['.gif', 'image/gif'],
  ['.avif', 'image/avif'],
]);

const apiKey = process.env.IMAGEUPLOAD_API_KEY || '';
const filePath = process.argv[2] || '';
const expiration = process.argv[3] || '1d';

if (!apiKey) {
  console.error('Set IMAGEUPLOAD_API_KEY before running this example.');
  process.exit(1);
}

if (!filePath) {
  console.error('Usage: node examples/upload.mjs /path/to/image.png [expiration]');
  process.exit(1);
}

const extension = path.extname(filePath).toLowerCase();
const mime = MIME_BY_EXTENSION.get(extension);
if (!mime) {
  console.error('Supported file extensions: png, jpg, jpeg, webp, gif, avif.');
  process.exit(1);
}

let bytes;
try {
  bytes = await readFile(filePath);
} catch (error) {
  console.error(`Could not read ${filePath}: ${error.message}`);
  process.exit(1);
}

const form = new FormData();
form.append('file', new Blob([bytes], { type: mime }), path.basename(filePath));
form.append('expiration', expiration);

const response = await fetch('https://imageupload.io/api/upload', {
  method: 'POST',
  headers: { Authorization: `Bearer ${apiKey}` },
  body: form,
});

const responseText = await response.text();
let payload;
try {
  payload = JSON.parse(responseText);
} catch {
  payload = { error: responseText || `HTTP ${response.status}` };
}

if (!response.ok) {
  console.error(JSON.stringify(payload, null, 2));
  process.exit(1);
}

console.log(JSON.stringify(payload, null, 2));
