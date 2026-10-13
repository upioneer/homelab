# Termix

[Termix](https://github.com/Termix-SSH/Termix) is an open-source, self-hosted, plugin-based server management platform and web terminal. It provides a modern browser-based interface and cross-platform desktop application for managing infrastructure via SSH, SFTP, Remote Desktop (RDP/VNC via Apache Guacamole), Docker containers, tmux sessions, and Tailscale.

## Key Features

- **SSH Terminal & Workspaces**: Full-featured terminal sessions with tabs, split layouts, persistent history, macros, snippets, and broadcast input across multiple hosts.
- **Remote Desktop**: RDP and VNC support integrated seamlessly in the browser via an optional companion `guacd` (Apache Guacamole) daemon.
- **Remote File Management**: Built-in SFTP file browser with file editing, upload/download, and directory traversal.
- **Session Collaboration**: Record terminal and desktop sessions for playback, share live sessions via links, or collaborate in shared terminal rooms.
- **Monitoring & Utilities**: Docker container monitoring, host resource metrics, tmux session inspector, Tailscale SSH support, and Wake-on-LAN.
- **Authentication**: Local user accounts, WebAuthn passkeys, TOTP 2FA, OpenID Connect / SSO (GitHub, Google, OIDC), or trusted reverse proxy headers (Authelia/Authentik).

## Configuration & Environment Variables

This deployment uses a [`.env`](.env) file in the same directory to manage port bindings and sensitive encryption credentials.

> [!IMPORTANT]
> **Security & Credentials Awareness**
>
> A [`.env`](.env) file is provided in this directory. Review and configure the following variables before deployment:
> - `TERMIX_PORT`: The host port exposed for the web interface (defaults to `8080`).
> - `JWT_SECRET`: Signing secret for user sessions. Must be at least 64 characters long (generate via `openssl rand -base64 48`).
> - `DATABASE_KEY`: 64-hexadecimal-character encryption key (32 bytes) for encrypting the SQLite database at rest (generate via `openssl rand -hex 32`).
> - `ENCRYPTION_KEY`: 64-hexadecimal-character key (32 bytes) used to encrypt stored host passwords and SSH private keys (generate via `openssl rand -hex 32`).
> - `INTERNAL_AUTH_TOKEN`: Secret token used for internal inter-service authentication (generate via `openssl rand -hex 16`).
>
> *Note:* If the security secret variables are left blank in [`.env`](.env), Termix will automatically generate cryptographically secure keys on initial startup and safely persist them in `/app/data/.env` inside the `termix_data` volume.

## Deployment Instructions

To start Termix and its companion Guacamole daemon using Docker Compose:

1. Navigate to this directory:
   ```bash
   cd Termix
   ```

2. *(Optional)* Edit the [`.env`](.env) file to customize the host port or pre-seed your encryption keys:
   ```bash
   nano .env
   ```

3. Launch the containers in detached mode:
   ```bash
   docker compose up -d
   ```

4. Access the web interface in your browser:
   ```
   http://<host-ip>:8080
   ```

### Managing the Service

```bash
# View live container logs
docker compose logs -f

# Check container status
docker compose ps

# Restart the service
docker compose restart

# Stop and remove containers
docker compose down
```

## Docker Compose File

The companion Compose specification is available at [docker-compose.yml](docker-compose.yml):

```yaml
services:
  termix:
    image: ghcr.io/termix-ssh/termix:latest
    container_name: termix
    restart: unless-stopped
    ports:
      - "${TERMIX_PORT:-8080}:8080"
    volumes:
      - termix_data:/app/data
    environment:
      - PORT=8080
      - GUACD_HOST=guacd
      - GUACD_TUNNEL_HOST=termix
      - GUACD_RECORDING_PATH=/termix-data/session_recordings/guacamole
      - GUACD_DRIVE_PATH=/termix-data/rdp-drive
      - JWT_SECRET=${JWT_SECRET:-}
      - DATABASE_KEY=${DATABASE_KEY:-}
      - ENCRYPTION_KEY=${ENCRYPTION_KEY:-}
      - INTERNAL_AUTH_TOKEN=${INTERNAL_AUTH_TOKEN:-}
    depends_on:
      - guacd
    networks:
      - termix_net

  guacd:
    image: guacamole/guacd:1.6.0
    container_name: guacd
    restart: unless-stopped
    volumes:
      - termix_data:/termix-data
    networks:
      - termix_net

volumes:
  termix_data:
    driver: local

networks:
  termix_net:
    driver: bridge
```
