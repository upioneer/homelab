# SongGeneration Studio

[SongGeneration Studio](https://github.com/BazedFrog/SongGeneration-Studio) is an open-source AI song and music generation web application that leverages deep learning audio models to compose full tracks, vocals, and musical stems locally on GPU hardware.

## Configuration

The service is managed via the companion [`docker-compose.yml`](docker-compose.yml) file. Below is the current configuration used to deploy the service:

```yaml
services:
  songgeneration-studio:
    image: bazedfrog/songgeneration-studio:latest
    container_name: songgeneration-studio
    restart: unless-stopped
    ports:
      - "7860:7860"
    environment:
      - SONG_GEN_API_KEY=${SONG_GEN_API_KEY}
      - CUDA_VISIBLE_DEVICES=0
    volumes:
      - ./data:/app/data
      - ./models:/app/models
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
```

## Environment Variables & Credentials

Before deploying, ensure you configure your environment variables. A `.env` file is located in this directory with placeholder values. Set any required credentials before starting:

```env
SONG_GEN_API_KEY=your_optional_api_key_here
```

## Deployment

To deploy SongGeneration Studio, ensure you have NVIDIA GPU drivers & NVIDIA Container Toolkit installed, then run:

```bash
docker compose up -d
```

Once running, access the web interface at `http://localhost:7860`.

For more details, visit the [SongGeneration Studio GitHub Repository](https://github.com/BazedFrog/SongGeneration-Studio).
