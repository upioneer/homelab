# TUIStudio

TUIStudio is a visual design tool for building Terminal User Interfaces (TUIs), often described as "Figma for the command line". The application is a static web app that allows you to drag and drop components to create TUI layouts and export them to frameworks like Bubble Tea, Ink, and Textual. 

This container builds the web application directly from the main GitHub repository and serves it statically via Nginx.

## Configuration

- **Companion file:** [docker-compose.yml](docker-compose.yml)

### docker-compose.yml

```yaml
version: "3.8"
services:
  tui-studio:
    build: https://github.com/jalonsogo/tui-studio.git#main
    container_name: tui-studio
    restart: unless-stopped
    ports:
      - "3080:80"
```

## Deployment Instructions

Since this service builds directly from the GitHub repository, use the `--build` flag when you first start it or when you want to fetch the latest updates.

Navigate to this directory and run:

```bash
docker compose up -d --build
```

Once running, you can access TUIStudio in your web browser at `http://<your-server-ip>:3080`.
