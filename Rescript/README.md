# Rescript

[Rescript](https://github.com/wassgha/rescript) is an open-source, transcript-based media editor. Drop in a video or audio file and it is transcribed locally with per-word timestamps and speaker labels. You can edit the video/audio simply by deleting text. All processing happens on-device for maximum privacy.

## Configuration

This service builds a local Docker image from the official Rescript repository.

[docker-compose.yml](docker-compose.yml)

```yaml
version: '3.8'

services:
  rescript:
    build: .
    container_name: rescript
    ports:
      - "3000:3000"
    restart: unless-stopped
```

## Deployment

1. Run the following command to build the image and start the service in the background:
   ```bash
   docker compose up -d --build
   ```
2. Access Rescript at `http://<your-server-ip>:3000`.
