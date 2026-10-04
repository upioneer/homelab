# LubeLogger

[LubeLogger](https://lubelogger.com/) is a modern, open-source, self-hosted vehicle maintenance records and fuel tracking application. It allows you to track fuel mileage, service records, maintenance reminders, vehicle expenses, parts, and documents across your household or fleet.

## Configuration & Environment Variables

This service uses an [`.env`](.env) file to configure the host port, locale, and optional SMTP email credentials for maintenance alerts.

> [!IMPORTANT]
> An [`.env`](.env) template is provided in this directory. Review the variables before deploying:
> - `LUBELOGGER_PORT`: Host port mapping (defaults to `8383`).
> - `LC_ALL` / `LANG`: System locale for date and currency formatting.
> - `MAIL_SERVER`, `MAIL_FROM`, `MAIL_PASSWORD`: Optional SMTP credentials for email alerts.

## Deployment Instructions

Navigate to this directory and start the service with Docker Compose:

```bash
docker compose up -d
```

Once running, access the LubeLogger dashboard in your web browser:

```
http://<your-server-ip>:8383
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
  lubelogger:
    image: hargoniuz/lubelogger:latest
    container_name: lubelogger
    restart: unless-stopped
    ports:
      - "${LUBELOGGER_PORT:-8383}:8080"
    environment:
      - LC_ALL=${LC_ALL:-en_US.UTF-8}
      - LANG=${LANG:-en_US.UTF-8}
      - MailConfig__EmailServer=${MAIL_SERVER}
      - MailConfig__EmailFrom=${MAIL_FROM}
      - MailConfig__Password=${MAIL_PASSWORD}
    volumes:
      - lubelogger_data:/App/data
      - lubelogger_config:/App/config
      - lubelogger_documents:/App/wwwroot/documents
      - lubelogger_images:/App/wwwroot/images
      - lubelogger_temp:/App/wwwroot/temp
      - lubelogger_log:/App/log

volumes:
  lubelogger_data:
  lubelogger_config:
  lubelogger_documents:
  lubelogger_images:
  lubelogger_temp:
  lubelogger_log:
```
