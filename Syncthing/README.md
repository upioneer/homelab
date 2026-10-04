# Syncthing

[Syncthing](https://syncthing.net/) is a continuous peer-to-peer decentralized file synchronization program. It synchronizes files between two or more computers in real time, securely protected from prying eyes with TLS encryption.

## Configuration & Environment Variables

This service uses an [`.env`](.env) file to configure the host port mapping, time zone, and file ownership permissions.

> [!NOTE]
> Review [`.env`](.env) before launching:
> - `PUID` / `PGID`: User and Group IDs matching your host user permissions (default `1000:1000`).
> - `TZ`: System time zone.
> - `SYNCTHING_GUI_PORT`: Port exposed for the Web Admin GUI (default `8384`).

## Deployment Instructions

To start Syncthing with Docker Compose:

```bash
docker compose up -d
```

Once running, access the Syncthing Web GUI in your browser:

```
http://<your-server-ip>:8384
```

To view logs or stop the service:

```bash
# View live container logs
docker compose logs -f

# Stop the container
docker compose down
```

## Docker Compose File

The companion compose file is available at [docker-compose.yml](docker-compose.yml):

```yaml
services:
  syncthing:
    image: syncthing/syncthing:latest
    container_name: syncthing
    hostname: syncthing
    restart: unless-stopped
    environment:
      - PUID=${PUID:-1000}
      - PGID=${PGID:-1000}
      - TZ=${TZ:-America/New_York}
    ports:
      - "${SYNCTHING_GUI_PORT:-8384}:8384"
      - "22000:22000/tcp"
      - "22000:22000/udp"
      - "21027:21027/udp"
    volumes:
      - syncthing_data:/var/syncthing

volumes:
  syncthing_data:
```
