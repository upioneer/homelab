# Option 1
Watchtower runs alongside and checks for updates at 4am. Adjust as required
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
# Option 2
## Ollama locally + Open WebUI via Docker
### These steps will expose your local models to the Open WebUI container
```yaml
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    ports:
      - "3000:8080"
    volumes:
      - open-webui:/app/backend/data
    extra_hosts:
      - "host.docker.internal:host-gateway"
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
You will need to update a few things to make your models visible to Open WebUI

Find the Ollama service file. Look for the path after "Loaded:"
```bash
sudo systemctl status ollama
```
Edit that file (example)
```bash
sudo nano /etc/systemd/system/ollama.service
```
Add a line directly and immediately under [Service]. It should look like this:
```yaml
[Service]
Environment="OLLAMA_HOST=0.0.0.0"
ExecStart=/usr/bin/ollama serve
```
Reload
```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama
```
Verify. You should have 0.0.0.0 or ::: but **not** 127.0.0.0
```bash
netstat -an | grep 11434
```
