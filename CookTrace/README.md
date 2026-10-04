# CookTrace

[CookTrace](https://github.com/TraceApps/cooktrace) is a self-hosted recipe, pantry, and cooking tracker with no accounts, no telemetry, and no cloud sync unless opted in. It runs as a lightweight Docker container with a PWA web interface and mobile support.

## Configuration & Environment Variables

This service uses a [`.env`](.env) file to configure application ports, security secrets, and optional SMTP settings.

> [!IMPORTANT]
> A [`.env`](.env) template has been created in this directory. Review and set the following variables before deploying:
> - `JWT_SECRET`: **Required.** A long random secret used to sign session tokens (generate with `openssl rand -hex 32`).
> - `INSECURE_COOKIES`: Set to `1` only if accessing over plain HTTP without a TLS reverse proxy on a trusted LAN.
> - `RECOVERY_TOKEN`: Optional lockout recovery token.
> - `SMTP_HOST`, `SMTP_USER`, `SMTP_PASS`, `SMTP_FROM`: Optional credentials for outgoing password reset emails.

## Deployment Instructions

To deploy CookTrace with Docker Compose, navigate to this directory and run:

```bash
docker compose up -d
```

Once running, access CookTrace in your web browser:

```
http://<your-server-ip>:3003
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
  cooktrace:
    image: ghcr.io/traceapps/cooktrace:latest
    container_name: cooktrace
    restart: unless-stopped
    ports:
      - "${COOKTRACE_PORT:-3003}:3003"
    volumes:
      - cooktrace_db:/data/db
      - cooktrace_uploads:/data/uploads
    environment:
      - DB_PATH=/data/db/cooktrace.db
      - UPLOADS_PATH=/data/uploads
      - JWT_SECRET=${JWT_SECRET}
      - RECOVERY_TOKEN=${RECOVERY_TOKEN}
      - INSECURE_COOKIES=${INSECURE_COOKIES:-0}
      - LOG_LEVEL=${LOG_LEVEL:-info}
      - SMTP_HOST=${SMTP_HOST}
      - SMTP_PORT=${SMTP_PORT:-587}
      - SMTP_USER=${SMTP_USER}
      - SMTP_PASS=${SMTP_PASS}
      - SMTP_FROM=${SMTP_FROM}

volumes:
  cooktrace_db:
  cooktrace_uploads:
```
