# Heimdall

Elegant dashboard for your web applications.

## Configuration

The service is managed via the companion [`docker-compose.yml`](docker-compose.yml) file. Below is the current configuration used to deploy the service:

```yaml
services:
  heimdall:
    image: lscr.io/linuxserver/heimdall:latest
    container_name: heimdall
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - ALLOW_INTERNAL_REQUESTS=false #optional
    volumes:
      - .config:/config
    ports:
      - 80:80
      - 443:443
    restart: unless-stopped

  watchtower:
    image: containrrr/watchtower
    container_name: watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --schedule "0 0 4 * * *" --cleanup
    restart: unless-stopped
```

## Deployment

You can optionally configure environment variables via the provided `.env` file if needed (e.g. `TZ`).

To start the service, ensure you are in this directory and run the following command:

```powershell
docker compose up -d
```
