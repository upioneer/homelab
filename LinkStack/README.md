# LinkStack
Update the [docker-compose.yml](docker-compose.yml) file as needed. Have a coke and a smile 😁
```yml
services:
  linkstack:
    image: linkstackorg/linkstack
    container_name: linkstack
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    environment:
      - HTTP_SERVER_NAME="www.example.xyz"
      - HTTPS_SERVER_NAME="www.example.xyz"
      - SERVER_ADMIN="admin@example.xyz"
      - TZ="America/Chicago"
      - PHP_MEMORY_LIMIT="512M"
      - UPLOAD_MAX_FILESIZE="8M"
    volumes:
      - linkstack_data:/htdocs

volumes:
  linkstack_data:
```
