
Watchtower runs alongside and checks for updates every 24h. Adjust as required
```yaml
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    ports:
      - "3000:8080"
    volumes:
      - open-webui:/app/backend/data
    restart: unless-stopped

  watchtower:
    image: containrrr/watchtower
    container_name: watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --interval 86400 --cleanup open-webui
    restart: unless-stopped

volumes:
  open-webui: {}
```

If running Ollama locally and Open WebUI via Docker. This will expose your local models to the Open WebUI container
```yaml
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    network_mode: "host"
    volumes:
      - open-webui:/app/backend/data
    restart: unless-stopped

  watchtower:
    image: containrrr/watchtower
    container_name: watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --interval 86400 --cleanup open-webui
    restart: unless-stopped

volumes:
  open-webui: {}
```
