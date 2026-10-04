# MusicGrabber

[MusicGrabber](https://gitlab.com/g33kphr33k/musicgrabber) is a self-hosted music acquisition service designed for grabbing individual tracks, watched playlists, and albums directly into your music library. It searches multiple sources (YouTube, SoundCloud, JioSaavn, Monochrome, Soulseek) and organizes downloads into your library for playback via Navidrome, Jellyfin, or Plex.

## Configuration & Environment Variables

This service uses a [`.env`](.env) file to configure the port, target library path, and optional media server rescan triggers.

> [!NOTE]
> Review [`.env`](.env) before starting:
> - `MUSICGRABBER_PORT`: Exposed host web port (default `38274`).
> - `MUSIC_DIR`: Path to the music library folder on the host.
> - `PUID` / `PGID`: Match your host storage user permissions (default `1000:1000`).
> - `NAVIDROME_URL`, `JELLYFIN_URL`, `PLEX_URL`: Optional auto-rescan triggers when downloads finish.

## Deployment Instructions

To deploy MusicGrabber with Docker Compose, navigate to this directory and run:

```bash
docker compose up -d
```

Once running, access the MusicGrabber web interface in your browser:

```
http://<your-server-ip>:38274
```

To view logs or stop the service:

```bash
# View live container logs
docker compose logs -f

# Stop the container
docker compose down
```

## Docker Compose File

The companion compose file is available at [docker-compose.yml](docker-compose.yml):

```yaml
services:
  music-grabber:
    image: g33kphr33k/musicgrabber:latest
    container_name: music-grabber
    restart: unless-stopped
    shm_size: '2gb'
    ports:
      - "${MUSICGRABBER_PORT:-38274}:8080"
    volumes:
      - ${MUSIC_DIR:-./music}:/music
      - musicgrabber_data:/data
    environment:
      - MUSIC_DIR=/music
      - DB_PATH=/data/music_grabber.db
      - ENABLE_MUSICBRAINZ=true
      - PUID=${PUID:-1000}
      - PGID=${PGID:-1000}
      - NAVIDROME_URL=${NAVIDROME_URL}
      - NAVIDROME_USER=${NAVIDROME_USER}
      - NAVIDROME_PASS=${NAVIDROME_PASS}
      - JELLYFIN_URL=${JELLYFIN_URL}
      - JELLYFIN_API_KEY=${JELLYFIN_API_KEY}
      - PLEX_URL=${PLEX_URL}
      - PLEX_TOKEN=${PLEX_TOKEN}

volumes:
  musicgrabber_data:
```
