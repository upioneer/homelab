# Voicebox

Voicebox is an open-source, local-first AI voice studio. It is a free alternative to tools like ElevenLabs and WisprFlow in a single package. It supports:
- Voice cloning from a few seconds of audio
- High-quality speech generation using 7 TTS engines (like Qwen3-TTS, Kokoro, etc.)
- 23+ supported languages
- Dictation with Whisper-based STT
- Post-processing audio effects
- Integration directly with MCP-aware AI agents through an API

For more information, see the [Voicebox Website](https://voicebox.sh/) or [GitHub Repository](https://github.com/jamiepine/voicebox).

## Configuration

This setup dynamically builds the Voicebox container using its GitHub repository (`main` branch) as the context. It binds port `17493` on all interfaces, so you can access it across your homelab network.

### Volumes

- `./output`: Local directory where generated audio files are saved.
- `voicebox-data`: Named volume for database, profiles, and cached configurations.
- `huggingface-cache`: Named volume to cache LLM/TTS models and avoid re-downloading them on rebuilds.

### Companion File

- [docker-compose.yml](docker-compose.yml)

### docker-compose.yml

```yaml
services:
  voicebox:
    build: https://github.com/jamiepine/voicebox.git#main
    container_name: voicebox
    restart: unless-stopped

    ports:
      # Exposing to all interfaces for homelab access.
      # Original used 127.0.0.1:17493:17493 for local security.
      - "17493:17493"

    volumes:
      # Bind-mount for generated audio
      - ./output:/app/data/generations
      # Named volume for profiles, DB, cache (persists across container restarts)
      - voicebox-data:/app/data
      # HuggingFace model cache (so models aren't re-downloaded on rebuild)
      - huggingface-cache:/home/voicebox/.cache/huggingface

    environment:
      - LOG_LEVEL=info
      - NUMBA_CACHE_DIR=/tmp/numba_cache

    networks:
      - voicebox-net

    deploy:
      resources:
        limits:
          cpus: '4'
          memory: 8G

networks:
  voicebox-net:
    driver: bridge

volumes:
  voicebox-data:
  huggingface-cache:
```

## Deployment

1. Navigate to this directory in your terminal.
2. Run the following command to build the image from GitHub and start the container in the background:

   ```bash
   docker compose up -d --build
   ```

**Note:** The initial run will take several minutes as Docker will clone the repository, build the image locally, and then download necessary voice models when the application starts.
