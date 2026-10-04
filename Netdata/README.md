# Netdata

[Netdata](https://netdata.cloud/) is an open-source, real-time performance and health monitoring solution. It collects thousands of metrics per second from CPUs, disks, filesystems, Docker containers, and services with per-second granularity and interactive visualization.

## Configuration & Environment Variables

This service uses an [`.env`](.env) file to configure optional Netdata Cloud claiming credentials.

> [!NOTE]
> Review [`.env`](.env) before launching:
> - By default, Netdata runs completely offline and locally without an account.
> - To connect your instance to Netdata Cloud, populate `NETDATA_CLAIM_TOKEN` and `NETDATA_CLAIM_ROOMS` from your Netdata Cloud account space.

## Deployment Instructions

To start Netdata with host monitoring capabilities:

```bash
docker compose up -d
```

Once running, access the local Netdata dashboard directly in your browser:

```
http://<your-server-ip>:19999
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
  netdata:
    image: netdata/netdata:latest
    container_name: netdata
    pid: host
    network_mode: host
    restart: unless-stopped
    cap_add:
      - SYS_PTRACE
      - SYS_ADMIN
    security_opt:
      - apparmor:unconfined
    volumes:
      - netdataconfig:/etc/netdata
      - netdatalib:/var/lib/netdata
      - netdatacache:/var/cache/netdata
      - /etc/passwd:/host/etc/passwd:ro
      - /etc/group:/host/etc/group:ro
      - /etc/localtime:/etc/localtime:ro
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /etc/os-release:/host/etc/os-release:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro
    environment:
      - NETDATA_CLAIM_TOKEN=${NETDATA_CLAIM_TOKEN}
      - NETDATA_CLAIM_URL=${NETDATA_CLAIM_URL:-https://app.netdata.cloud}
      - NETDATA_CLAIM_ROOMS=${NETDATA_CLAIM_ROOMS}

volumes:
  netdataconfig:
  netdatalib:
  netdatacache:
```
