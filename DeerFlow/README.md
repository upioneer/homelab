# DeerFlow

[DeerFlow](https://deerflow.tech/) is ByteDance's open-source SuperAgent orchestration framework and deep research system designed for handling long-horizon tasks, multi-agent workflows, and human-AI teaming.

## Configuration

The service is managed via the companion [`docker-compose.yml`](docker-compose.yml) file. Below is the current configuration used to deploy the service:

```yaml
services:
  deer-flow:
    image: bytedance/deer-flow:latest
    container_name: deer-flow
    restart: unless-stopped
    ports:
      - "3000:3000"
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - DEERFLOW_HOST=${DEERFLOW_HOST}
      - DEERFLOW_PORT=${DEERFLOW_PORT}
    volumes:
      - ./data:/app/data
```

## Environment Variables & Credentials

Before deploying, ensure you configure your environment variables. A `.env` file is located in this directory with placeholder values. Be sure to configure your API keys and host settings securely prior to starting the container:

```env
OPENAI_API_KEY=your_openai_api_key_here
DEERFLOW_HOST=0.0.0.0
DEERFLOW_PORT=3000
```

## Deployment

To deploy DeerFlow, ensure you are in this directory and run:

```bash
docker compose up -d
```

For more details, visit the [DeerFlow GitHub Repository](https://github.com/bytedance/deer-flow) or the [DeerFlow Official Site](https://deerflow.tech/).
