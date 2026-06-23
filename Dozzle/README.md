# Dozzle

Container log viewer.

## Configuration

The service is managed via the companion [`docker-compose.yml`](docker-compose.yml) file. Below is the current configuration used to deploy the service:

```yaml
services:
  dozzle:
    container_name: dozzle
    image: amir20/dozzle:latest
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    ports:
      - 8080:8080
    command: --no-analytics
             --remote-host
             tcp://192.168.1.100|hostname1
             --remote-host
             tcp://192.168.1.101|hostname2
    restart: unless-stopped

  watchtower:
    image: containrrr/watchtower
    container_name: watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --schedule "0 0 4 * * *" --cleanup 
    restart: unless-stopped
```

## Deployment

You can optionally configure environment variables via the provided `.env` file if needed (e.g. `TZ`).

To start the service, ensure you are in this directory and run the following command:

```powershell
docker compose up -d
```
