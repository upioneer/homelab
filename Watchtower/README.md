# Example: Daily at 4am + orphaned image clean up
```yml
  watchtower:
    image: containrrr/watchtower
    container_name: watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --schedule "0 0 4 * * *" --cleanup
    restart: unless-stopped
```
# Example: Twice daily + rolling container restart
```yml
  watchtower:
    image: containrrr/watchtower
    container_name: watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --schedule "0 0 4,16 * * *" --cleanup --rolling-restart
    restart: unless-stopped
```
# Example: Hourly on the hour + only update images that exist locally
```yml
  watchtower:
    image: containrrr/watchtower
    container_name: watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --schedule "0 0 * * * *" --no-pull
    restart: unless-stopped
```
