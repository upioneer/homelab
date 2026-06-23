# WireGuard

Fast, modern, and simple VPN.

## Configuration

The service is managed via the companion [`docker-compose.yml`](docker-compose.yml) file. Below is the current configuration used to deploy the service:

```yaml
services:
  wg-easy:
    image: weejewel/wg-easy
    container_name: wg-easy
    environment:
      - WG_HOST=your.server.ip
    volumes:
      - .:/etc/wireguard
    ports:
      - "51820:51820/udp"
      - "51821:51821/tcp"
    cap_add:
      - NET_ADMIN
      - SYS_MODULE
    restart: unless-stopped
```

## Deployment

You can optionally configure environment variables via the provided `.env` file if needed (e.g. `TZ`).

To start the service, ensure you are in this directory and run the following command:

```powershell
docker compose up -d
```
