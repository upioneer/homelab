# Unsloth Studio

Unsloth Studio provides a local AI Web UI, utilizing Unsloth for efficient model fine-tuning and inference. This service allows you to run models directly on your hardware with GPU acceleration.

## Configuration

The service is managed via the companion [`docker-compose.yml`](docker-compose.yml) file. Below is the current configuration used to deploy the service, which maps the necessary ports and passes all available GPUs to the container.

```yaml
services:
  unsloth_studio:
    image: unsloth/unsloth
    container_name: unsloth_studio
    restart: unless-stopped
    ports:
      - "8888:8888"
      - "8000:8000"
      - "2222:22"
    environment:
      - JUPYTER_PASSWORD=${JUPYTER_PASSWORD}
    volumes:
      - ./work:/workspace/work
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
```

## Deployment

Before deploying, ensure you configure your environment variables. A `.env` file has been provided with a placeholder. Edit the `.env` file to set your secure password:

```env
JUPYTER_PASSWORD=your_secure_password_here
```

To start Unsloth Studio, ensure you are in this directory and run the following command:

```bash
docker compose up -d
```

Once running, you can access the interface at `http://localhost:8888`.
