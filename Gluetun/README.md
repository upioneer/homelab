# Gluetun

VPN client container for other containers to use.

## Configuration

The service is managed via the companion [`docker-compose.yml`](docker-compose.yml) file. Below is the current configuration used to deploy the service:

```yaml
services:
  gluetun:
    image: qmcgaw/gluetun
    container_name: gluetun
    cap_add:
      - NET_ADMIN
    devices:
      - /dev/net/tun:/dev/net/tun
    ports:
      - 8888:8888/tcp # HTTP proxy
      - 8388:8388/tcp # Shadowsocks
      - 8388:8388/udp # Shadowsocks
    volumes:
      - ./data:/gluetun
    environment:
      - HTTPPROXY=on
      - SHADOWSOCKS=on
      - TZ=America/Chicago
      - VPN_SERVICE_PROVIDER=nordvpn
      - VPN_TYPE=openvpn
      - OPENVPN_USER=${OPENVPN_USER}
      - OPENVPN_PASSWORD=${OPENVPN_PASSWORD}
```

## Deployment

You can optionally configure environment variables via the provided `.env` file if needed (e.g. `TZ`).

To start the service, ensure you are in this directory and run the following command:

```powershell
docker compose up -d
```
