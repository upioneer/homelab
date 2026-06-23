# Tracefinity

Self-hosted tool for generating Gridfinity bins from tool photos.

## Configuration

The service is managed via the companion [`docker-compose.yml`](docker-compose.yml) file. Below is the current configuration used to deploy the service:

```yaml
services:
  tracefinity:
    image: ghcr.io/tracefinity/tracefinity:latest
    container_name: tracefinity
    ports:
      - "3000:3000"
    volumes:
      - ./data:/app/storage
    environment:
      # Optional: Add your Google Gemini API key here for cloud-powered tracing.
      # If omitted, Tracefinity will fall back to local ONNX models.
      - GOOGLE_API_KEY=
      # Optional: Set ONNX provider ("auto", "cuda", or "cpu"). Defaults to "auto".
      - TRACEFINITY_ONNX_PROVIDER=auto
    restart: unless-stopped
```

## Deployment

You can optionally configure environment variables via the provided `.env` file if needed (e.g. `TZ`).

To start the service, ensure you are in this directory and run the following command:

```powershell
docker compose up -d
```
