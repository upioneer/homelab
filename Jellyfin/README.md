# Drive map
Refer to the [SMB share](../Proxmox/SMBmap.md) guide for mapping in your Proxmox host and exposing the SMB to the LXC

Keep this in mind when declaring the volumes, in the example below `- /media:/media:ro`
# Docker Compose
Option 1: Docker Compose
```yaml
services:
  jellyfin:
    image: jellyfin/jellyfin:latest
    container_name: jellyfin
    network_mode: "host"
    volumes:
      - /srv/jellyfin/config:/config
      - /srv/jellyfin/cache:/cache
      - /media:/media:ro
    restart: unless-stopped
```
Option 2: Docker Compose + Watchtower. Checks for updates at 4am
```yaml
services:
  jellyfin:
    image: jellyfin/jellyfin:latest
    container_name: jellyfin
    network_mode: "host"
    volumes:
      - /srv/jellyfin/config:/config
      - /srv/jellyfin/cache:/cache
      - /media:/media:ro
    restart: unless-stopped

  watchtower:
    image: containrrr/watchtower
    container_name: watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --schedule "0 0 4 * * *" --cleanup
    restart: unless-stopped
```
