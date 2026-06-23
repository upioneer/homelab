# NginxProxyManager

Nginx reverse proxy with a web UI.

## Configuration

The service is managed via the companion [`docker-compose.yml`](docker-compose.yml) file. Below is the current configuration used to deploy the service:

```yaml
services:
  nginx-proxy-manager:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
      - "81:81"
    volumes:
      - data_nginx:/data
      - data_letsencrypt:/etc/letsencrypt
    networks:
      - proxy-net

  cloudflared:
    image: cloudflare/cloudflared:latest
    container_name: cloudflared
    restart: unless-stopped
    command: tunnel --no-autoupdate run --token ${CLOUDFLARE_TOKEN}
    volumes:
      - data_cloudflared:/home/nonroot/.cloudflared/
    networks:
      - proxy-net

networks:
  proxy-net:

volumes:
  data_nginx:
  data_letsencrypt:
  data_cloudflared:
```

## Deployment

Before deploying, ensure you configure your environment variables. A `.env` file has been provided with placeholder values. Edit the `.env` file to set your secure credentials:

```env
CLOUDFLARE_TOKEN=your_secure_cloudflare_token_here
```

To start the service, ensure you are in this directory and run the following command:

```powershell
docker compose up -d
```
