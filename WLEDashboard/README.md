# WLEDashboard

[WLEDashboard](https://wledashboard.com) is a high-performance, local-first control surface for WLED devices. It allows you to command from 1 to 100+ LED controllers from a single unified pane of glass with spring physics animations, group management, a 3D spatial viewport powered by Three.js, an effect studio & keyframe animator, and automatic mDNS discovery.

## Configuration & Environment Variables

This service uses an [`.env`](.env) file to configure the host port mapping and environment flags.

> [!NOTE]
> An [`.env`](.env) file is provided in this directory. Review and configure it before deploying:
> - `PORT`: Host port mapping (defaults to `3001`)
> - `NODE_ENV`: Runtime environment (`production`)

## Deployment Instructions

To deploy WLEDashboard, navigate to this directory and run:

```bash
docker compose up -d
```

Once the container is running, access the dashboard in your web browser:

```
http://<your-server-ip>:3001
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
  wledashboard:
    image: ghcr.io/upioneer/wledashboard:latest
    container_name: wledashboard
    ports:
      - "${PORT:-3001}:3001"
    environment:
      - NODE_ENV=production
      - DATA_DIR=/app/data
    volumes:
      - wledashboard_data:/app/data
    restart: unless-stopped

volumes:
  wledashboard_data:
```
