# Notifuse

Open-source, self-hosted emailing platform for newsletters and transactional emails.

## Configuration

The service is managed via the companion [`docker-compose.yml`](docker-compose.yml) file. Below is the current configuration used to deploy the service:

```yaml
services:
  notifuse:
    image: notifuse/notifuse:latest
    container_name: notifuse
    ports:
      - "8081:8080"
    environment:
      - SERVER_PORT=8080
      - SERVER_HOST=0.0.0.0
      - ENVIRONMENT=production
      - DB_HOST=notifuse-db
      - DB_PORT=5432
      - DB_USER=postgres
      - DB_PASSWORD=${DB_PASSWORD}
      - DB_NAME=notifuse_system
      - SECRET_KEY=${SECRET_KEY}
    depends_on:
      - notifuse-db
    restart: unless-stopped

  notifuse-db:
    image: postgres:17-alpine
    container_name: notifuse-db
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=notifuse_system
    volumes:
      - notifuse-db-data:/var/lib/postgresql/data
    restart: unless-stopped

  watchtower:
    image: containrrr/watchtower
    container_name: watchtower-notifuse
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --schedule "0 0 4 * * *" --cleanup
    restart: unless-stopped

volumes:
  notifuse-db-data:
```

## Deployment

Before deploying, ensure you configure your environment variables. A `.env` file has been provided with placeholder values. Edit the `.env` file to set your secure credentials:

```env
DB_PASSWORD=your_secure_db_password_here
SECRET_KEY=your_secure_secret_key_here
POSTGRES_PASSWORD=your_secure_postgres_password_here
```

To start the service, ensure you are in this directory and run the following command:

```powershell
docker compose up -d
```
