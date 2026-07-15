# LibrePhotos

LibrePhotos is a self-hosted, open-source Google Photos alternative that allows you to manage and view your photo library. It offers facial recognition, object detection, and map views.

## Configuration

> [!WARNING]
> Before deploying, you must configure the `.env` file!

Sensitive credentials and environment variables are not hardcoded in the `docker-compose.yml` file. Instead, we use a `.env` file for variable substitution. 

Please follow these steps:
1. Locate the `.env` file in this directory.
2. Update the placeholder values (e.g., `dbPass=REPLACE_ME_WITH_A_SECURE_PASSWORD`) with your own secure passwords and credentials.
3. Configure the `scanDirectory` and `data` variables to point to your actual photo directories if you do not want to use the default `./data/pictures` relative path.

## Deployment

Once you have configured the `.env` file, you can deploy the stack using Docker Compose:

```bash
docker compose up -d
```

The service will be available on the port configured in your `.env` file (default is `3000`). Access it by navigating to `http://<your-server-ip>:3000` in your web browser.

## Docker Compose File

Companion configuration: [docker-compose.yml](docker-compose.yml)

```yaml
# DO NOT EDIT
# The .env file has everything you need to edit.
# Run options:
# 1. Use prebuilt images (preferred method):
#   run cmd: docker compose up -d
# 2. Build images on your own machine:
#   build cmd: docker compose build
#   run cmd: docker compose up -d

services:
  proxy:
    image: reallibrephotos/librephotos-proxy:${tag}
    container_name: proxy
    restart: unless-stopped
    volumes:
      - ${scanDirectory}:/data
      - ${data}/protected_media:/protected_media
    ports:
      - ${httpPort:-3000}:80
    depends_on:
      - backend
      - frontend

  db:
    image: pgautoupgrade/pgautoupgrade:latest
    container_name: db
    restart: unless-stopped
    environment:
      - POSTGRES_USER=${dbUser}
      - POSTGRES_PASSWORD=${dbPass}
      - POSTGRES_DB=${dbName}
    volumes:
      - ${data}/db:/var/lib/postgresql
    healthcheck:
      test: psql -U ${dbUser} -d ${dbName} -c "SELECT 1;"
      interval: 5s
      timeout: 5s
      retries: 5

  frontend:
    image: reallibrephotos/librephotos-frontend:${tag}
    container_name: frontend
    restart: unless-stopped

  backend:
    image: reallibrephotos/librephotos:${tag}
    container_name: backend
    restart: unless-stopped
    volumes:
      - ${scanDirectory}:/data
      - ${data}/protected_media:/protected_media
      - ${data}/logs:/logs
      - ${data}/cache:/root/.cache
    environment:
      - SECRET_KEY=${shhhhKey:-}
      - BACKEND_HOST=backend
      - ADMIN_EMAIL=${adminEmail:-}
      - ADMIN_USERNAME=${userName:-}
      - ADMIN_PASSWORD=${userPass:-}
      - DB_BACKEND=postgresql
      - DB_NAME=${dbName}
      - DB_USER=${dbUser}
      - DB_PASS=${dbPass}
      - DB_HOST=${dbHost}
      - DB_PORT=5432
      - MAPBOX_API_KEY=${mapApiKey:-}
      - WEB_CONCURRENCY=${gunniWorkers:-1}
      - SKIP_PATTERNS=${skipPatterns:-}
      - ALLOW_UPLOAD=${allowUpload:-false}
      - CSRF_TRUSTED_ORIGINS=${csrfTrustedOrigins:-}
      - DEBUG=0
    depends_on:
      db:
        condition: service_healthy
```
