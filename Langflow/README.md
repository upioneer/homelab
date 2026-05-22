# Langflow Setup

[Langflow](https://www.langflow.org/) is a visual framework for building multi-agent and RAG (Retrieval-Augmented Generation) applications. Featuring a beautiful React-based flow editor and a powerful Python backend, Langflow enables you to drag-and-drop components (LLMs, Prompts, Agents, Tools, and Vector Stores) to prototype and export production-ready AI workflows.

## Docker Compose Configurations

### Option 1: Full Stack with PostgreSQL and Watchtower (Recommended)

This configuration includes Langflow, a dedicated PostgreSQL database backend for robust storage of your flows and configurations, and a Watchtower container that checks for image updates and cleans up obsolete layers daily at 4:00 AM.

```yaml
services:
  langflow:
    image: langflowai/langflow:latest
    container_name: langflow
    pull_policy: always
    ports:
      - "7860:7860"
    environment:
      - LANGFLOW_DATABASE_URL=postgresql://langflow:langflow@langflow-postgres:5432/langflow
      - LANGFLOW_CONFIG_DIR=/app/langflow
    volumes:
      - langflow-data:/app/langflow
    depends_on:
      - postgres
    restart: unless-stopped

  postgres:
    image: postgres:16-alpine
    container_name: langflow-postgres
    environment:
      - POSTGRES_USER=langflow
      - POSTGRES_PASSWORD=langflow
      - POSTGRES_DB=langflow
    volumes:
      - langflow-postgres:/var/lib/postgresql/data
    restart: unless-stopped

  watchtower:
    image: containrrr/watchtower
    container_name: watchtower-langflow
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --schedule "0 0 4 * * *" --cleanup
    restart: unless-stopped

volumes:
  langflow-data:
  langflow-postgres:
```

---

## Deployment Steps

1. **Deploy the service**:
   ```bash
   docker compose up -d
   ```

2. **Access the Web Interface**:
   Navigate to `http://<host-ip>:7860` in your web browser. You will be greeted by the interactive flow editor where you can start dragging and dropping AI nodes.

3. **Secure Your Instance**:
   Before exposing Langflow to external networks, ensure that:
   - PostgreSQL credentials in your `.env` or `docker-compose.yml` are updated to secure custom passwords.
   - You utilize a secure reverse proxy (like Nginx Proxy Manager or Traefik) to enable HTTPS.
