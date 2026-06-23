# Langflow

Visual framework for building multi-agent and RAG applications.

## Configuration

The service is managed via the companion [`docker-compose.yml`](docker-compose.yml) file. Below is the current configuration used to deploy the service:

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
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
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

## Deployment

Before deploying, ensure you configure your environment variables. A `.env` file has been provided with placeholder values. Edit the `.env` file to set your secure credentials:

```env
POSTGRES_PASSWORD=your_secure_postgres_password_here
```

To start the service, ensure you are in this directory and run the following command:

```powershell
docker compose up -d
```
