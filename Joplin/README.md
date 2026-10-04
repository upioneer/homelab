# Joplin Server

[Joplin](https://joplinapp.org/) is a free, open-source note-taking and to-do application. This service runs Joplin Server with a dedicated PostgreSQL database backend, allowing synchronization across all your Joplin desktop and mobile clients.

## Configuration & Environment Variables

This service requires database credentials and an application base URL configured before starting. An [`.env`](.env) file is provided in this directory.

> [!IMPORTANT]
> Ensure you update the sensitive variables in [`.env`](.env) before deploying:
> - `APP_BASE_URL`: The fully qualified URL or IP through which clients reach Joplin Server (e.g. `http://192.168.1.50:22300` or `https://joplin.yourdomain.com`).
> - `POSTGRES_USER`: Database user for PostgreSQL.
> - `POSTGRES_PASSWORD`: Strong password for the PostgreSQL user.
> - `JOPLIN_PORT`: Exposed host port (default `22300`).

## Deployment Instructions

Navigate to this directory and start the stack with Docker Compose:

```bash
docker compose up -d
```

Once running, access the Joplin Server admin dashboard in your web browser:

```
http://<your-server-ip>:22300
```

Default administrator login:
- **Email:** `admin@localhost`
- **Password:** `admin`

*(Ensure you change the admin password immediately upon first login!)*

To view logs or stop the service:

```bash
# View logs
docker compose logs -f

# Stop the service
docker compose down
```

## Docker Compose File

The companion compose file is available at [docker-compose.yml](docker-compose.yml):

```yaml
services:
  joplin-server:
    image: joplin/server:latest
    container_name: joplin-server
    restart: unless-stopped
    depends_on:
      - joplin-db
    ports:
      - "${JOPLIN_PORT:-22300}:22300"
    environment:
      - APP_BASE_URL=${APP_BASE_URL}
      - APP_PORT=22300
      - DB_CLIENT=pg
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DATABASE=joplin
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PORT=5432
      - POSTGRES_HOST=joplin-db

  joplin-db:
    image: postgres:16-alpine
    container_name: joplin-db
    restart: unless-stopped
    volumes:
      - joplin_db_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_DB=joplin

volumes:
  joplin_db_data:
```
