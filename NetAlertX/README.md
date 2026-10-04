# NetAlertX

[NetAlertX](https://github.com/jokob-sk/NetAlertX) (formerly Pi.Alert) is a self-hosted WiFi / LAN intruder detector, network scanner, and device connection monitor. It periodically scans your local network using ARP, ICMP, and port probes to identify connected devices, report new/unknown MAC addresses, and track availability.

## Configuration & Environment Variables

This service uses an [`.env`](.env) file to configure the web interface port and system time zone.

> [!NOTE]
> Review [`.env`](.env) before launching:
> - `PORT`: Web port (defaults to `20211`).
> - `TZ`: System time zone for scheduled scan timestamps (e.g. `America/New_York`).
>
> *Note:* NetAlertX utilizes `network_mode: "host"` to directly listen for local ARP packets and broadcast traffic across your subnets.

## Deployment Instructions

To start NetAlertX:

```bash
docker compose up -d
```

Once started, access the web UI in your browser:

```
http://<your-server-ip>:20211
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
  netalertx:
    image: jokobsk/netalertx:latest
    container_name: netalertx
    network_mode: "host"
    restart: unless-stopped
    environment:
      - TZ=${TZ:-America/New_York}
      - PORT=${PORT:-20211}
    volumes:
      - netalertx_config:/app/config
      - netalertx_db:/app/db
      - netalertx_log:/app/log

volumes:
  netalertx_config:
  netalertx_db:
  netalertx_log:
```
