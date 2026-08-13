# Neko

Neko is a self-hosted virtual browser that runs in Docker and uses WebRTC video streaming.

## Configuration

This setup requires passwords to be configured before deploying. An `.env` file has been created.
Please ensure you set the `NEKO_USER_PASSWORD` and `NEKO_ADMIN_PASSWORD` variables in the `.env` file.

## Deployment

Deploy this service using docker compose:

```bash
docker compose up -d
```

## Docker Compose File
[docker-compose.yml](docker-compose.yml)

```yaml
services:
  neko:
    image: "ghcr.io/m1k1o/neko/firefox:latest"
    restart: "unless-stopped"
    shm_size: "2gb"
    ports:
      - "8080:8080"
      - "52000-52100:52000-52100/udp"
    environment:
      NEKO_SCREEN: 1920x1080@30
      NEKO_PASSWORD: ${NEKO_USER_PASSWORD}
      NEKO_PASSWORD_ADMIN: ${NEKO_ADMIN_PASSWORD}
      NEKO_EPR: 52000-52100
      NEKO_ICELITE: 1
```
