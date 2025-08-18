# Add token on line 21
```yml
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
    user: root
    command: tunnel --no-autoupdate run --token YOUR_TOKEN_HERE
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
Alternatively, use a token variable and add your token to a `.env` file in the same folder as `docker-compose.yml`
```yml
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
    user: root
    command: tunnel --no-autoupdate run --token $(CF_TOKEN)
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
# Contents of the `.env`
```env
CF_TOKEN=YOUR_TOKEN_HERE
```
