# Homelabable

[Homelabable](https://github.com/Pouzor/homelable) (formerly Homelable) is a self-hosted homelab infrastructure visualization and network scanning tool.

## Deployment

1.  Deploy using Docker Compose:
    ```bash
    docker compose up -d
    ```

## Features

- **Network Scanning:** Automatically discover devices on your network.
- **Infrastructure Visualization:** Interactive network diagrams and canvas.
- **AI Integration:** Support for Model Context Protocol (MCP) for AI-driven management.

### Password Generation

To generate a password hash for `AUTH_PASSWORD_HASH`:
```bash
docker run --rm ghcr.io/pouzor/homelable-backend:latest python -c "from passlib.hash import bcrypt; print(bcrypt.hash('yourpassword'))"
```

For more information, visit the [GitHub repository](https://github.com/Pouzor/homelable).
