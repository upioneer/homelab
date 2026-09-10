# OpenPrevue

[OpenPrevue](https://openprevue.com) is a glanceable event schedule board and retro 1990s TV guide simulator. It features continuous 60 FPS smooth scrolling event schedule matrices, Model Context Protocol (MCP 1.0) AI agent integration, Telegram alerts, and support for local venue calendar aggregation.

## Configuration & Environment Variables

This service uses a [`.env`](.env) file to configure application settings, location defaults, and sensitive credentials for third-party event providers and alert bots.

> [!IMPORTANT]
> A [`.env`](.env) template has been created in this directory. Before deploying, review and populate any required or optional credentials:
> - `TICKETMASTER_API_KEY`: API key for live Ticketmaster event discovery
> - `SEATGEEK_CLIENT_ID` & `SEATGEEK_CLIENT_SECRET`: Client credentials for SeatGeek integration
> - `EVENTBRITE_API_TOKEN`: Personal OAuth token for Eventbrite events
> - `TELEGRAM_BOT_TOKEN`: Telegram bot token for real-time schedule alerts

Sensitive credentials are substituted via environment variables and should not be committed into source control.

## Deployment Instructions

To start the OpenPrevue container stack, navigate to this directory and run:

```bash
docker compose up -d
```

Once running, OpenPrevue will be accessible in your web browser at:

```
http://<your-server-ip>:8080
```

To view logs or stop the service:

```bash
# View live logs
docker compose logs -f

# Stop the service
docker compose down
```

## Docker Compose File

The companion compose file is available at [docker-compose.yml](docker-compose.yml):

```yaml
services:
  openprevue:
    image: ghcr.io/upioneer/openprevue:latest
    container_name: openprevue
    restart: unless-stopped
    ports:
      - "${PORT:-8080}:8080"
    environment:
      - TZ=${TZ:-America/New_York}
      - PORT=8080
      - DATA_DIR=/app/data
      - LOG_LEVEL=${LOG_LEVEL:-INFO}
      - DEFAULT_POSTAL_CODE=${DEFAULT_POSTAL_CODE:-10001}
      - DEFAULT_METRO_LABEL=${DEFAULT_METRO_LABEL:-NEW YORK CITY}
      - DEFAULT_LATITUDE=${DEFAULT_LATITUDE:-40.7128}
      - DEFAULT_LONGITUDE=${DEFAULT_LONGITUDE:--74.0060}
      - DEFAULT_RADIUS_MILES=${DEFAULT_RADIUS_MILES:-25}
      - TICKETMASTER_API_KEY=${TICKETMASTER_API_KEY}
      - SEATGEEK_CLIENT_ID=${SEATGEEK_CLIENT_ID}
      - SEATGEEK_CLIENT_SECRET=${SEATGEEK_CLIENT_SECRET}
      - EVENTBRITE_API_TOKEN=${EVENTBRITE_API_TOKEN}
      - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
    volumes:
      - ./data:/app/data
    healthcheck:
      test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8080/api/v1/health')"]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 10s
    deploy:
      resources:
        limits:
          memory: 256M
        reservations:
          memory: 128M
```
