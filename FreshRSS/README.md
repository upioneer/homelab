# FreshRSS

[FreshRSS](https://freshrss.org/) is a self-hosted, lightweight RSS feed aggregator that is fast, responsive, and easily extensible with plugins and custom themes. It supports multi-user setups, Fever and Google Reader APIs for mobile client synchronization.

## Configuration & Environment Variables

This service uses a [`.env`](.env) file to configure the host port binding and local time zone.

> [!NOTE]
> Review and customize the settings in [`.env`](.env) before launching:
> - `FRESHRSS_PORT`: Exposed host port (defaults to `8089`).
> - `TZ`: System time zone for scheduled RSS feed updates (e.g. `America/New_York`).
> - `CRON_MIN`: Minutes of the hour when automatic feed refresh should run (default `13,43`).

## Deployment Instructions

To deploy FreshRSS with Docker Compose:

```bash
docker compose up -d
```

Once running, navigate to the web setup wizard in your browser:

```
http://<your-server-ip>:8089
```

Follow the on-screen prompts to configure your administrator user and database (SQLite is supported out-of-the-box).

To view logs or stop the service:

```bash
# View live logs
docker compose logs -f

# Stop the container
docker compose down
```

## Docker Compose File

The companion compose file is available at [docker-compose.yml](docker-compose.yml):

```yaml
services:
  freshrss:
    image: freshrss/freshrss:latest
    container_name: freshrss
    restart: unless-stopped
    ports:
      - "${FRESHRSS_PORT:-8089}:80"
    environment:
      - TZ=${TZ:-America/New_York}
      - CRON_MIN=${CRON_MIN:-13,43}
    volumes:
      - freshrss_data:/var/www/FreshRSS/data
      - freshrss_extensions:/var/www/FreshRSS/extensions

volumes:
  freshrss_data:
  freshrss_extensions:
```
