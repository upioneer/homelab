# Croc

Croc is a tool that allows any two computers to simply and securely transfer files and folders. It provides end-to-end encryption, allows resuming interrupted transfers, and doesn't require port forwarding. 
By self-hosting a croc relay, you can ensure your data never passes through a public third-party relay.

## Configuration

This service requires a `.env` file to securely store your relay password. A placeholder `.env` has been created for you.

Before deploying, make sure to configure the password in the `.env` file:
```bash
nano .env
```
*Set `CROC_RELAY_PASSWORD` to a strong, secure password.*

## Deployment

[docker-compose.yml](docker-compose.yml)

```yaml
services:
  croc:
    image: schollz/croc:latest
    container_name: croc
    restart: unless-stopped
    command: relay --pass ${CROC_RELAY_PASSWORD}
    ports:
      - "9009:9009"
      - "9010:9010"
      - "9011:9011"
      - "9012:9012"
      - "9013:9013"
```

To deploy this service, run:
```bash
docker compose up -d
```

## Usage

When sending and receiving files, you will need to specify your custom relay and password:

```bash
croc --relay your-server-ip:9009 --pass your_secure_password_here send file.txt
```

```bash
croc --relay your-server-ip:9009 --pass your_secure_password_here [code]
```
