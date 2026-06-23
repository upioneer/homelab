# your_spotify

Self-hosted tracker for your Spotify listening habits.

## Configuration

The service is managed via the companion [`docker-compose.yml`](docker-compose.yml) file. Below is the current configuration used to deploy the service:

```yaml
services:
  server:
    image: yooooomi/your_spotify_server
    restart: always
    ports:
      - "8080:8080"
    links:
      - mongo
    depends_on:
      - mongo
    environment:
      API_ENDPOINT: http://localhost:8080 # This MUST be included as a valid URL in the spotify dashboard
      CLIENT_ENDPOINT: http://localhost:3000
      SPOTIFY_PUBLIC: ${SPOTIFY_PUBLIC} # add to .env file
      SPOTIFY_SECRET: ${SPOTIFY_SECRET} # add to .env file

  mongo:
    container_name: mongo
    image: mongo:6
    restart: always
    volumes:
      - ./your_spotify_db:/data/db

  web:
    image: yooooomi/your_spotify_client
    restart: always
    ports:
      - "3000:3000"
    environment:
      API_ENDPOINT: http://localhost:8080

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
