# WebODM

WebODM (OpenDroneMap) is a free, user-friendly, extendable application and API for drone image processing. It generates orthophotos, point clouds, 3D models, and more from aerial images. This deployment includes the webapp, database, broker, worker, and a default `node-odx-1` processing node to handle the actual computation tasks.

## Companion Files
- [docker-compose.yml](docker-compose.yml)
- [.env](.env)

## Docker Compose File

```yaml
version: '3.8'

volumes:
  dbdata:
  appmedia:

services:
  db:
    image: webodm/webodm_db
    container_name: webodm_db
    expose:
      - "5432"
    volumes:
      - ${WO_DB_DIR:-dbdata}:/var/lib/postgresql/data:Z
    restart: unless-stopped
    oom_score_adj: -100

  webapp:
    image: webodm/webodm_webapp
    container_name: webodm_webapp
    entrypoint: /bin/bash -c "service cron start && chmod +x /webodm/*.sh && /bin/bash -c \"/webodm/wait-for-postgres.sh db /webodm/wait-for-it.sh -t 0 broker:6379 -- /webodm/start.sh\""
    volumes:
      - ${WO_MEDIA_DIR:-appmedia}:/webodm/app/media:z
    ports:
      - "${WO_PORT:-8000}:8000"
    depends_on:
      - db
      - broker
      - worker
      - node-odx-1
    environment:
      - WO_PORT=${WO_PORT:-8000}
      - WO_HOST=${WO_HOST:-localhost}
      - WO_DEBUG=${WO_DEBUG:-False}
      - WO_BROKER=redis://broker:6379/0
      - WO_SECRET_KEY=${WO_SECRET_KEY:-}
      - WEB_CONCURRENCY=${WEB_CONCURRENCY:-}
      - WO_DEFAULT_NODES=${WO_DEFAULT_NODES:-1}
    restart: unless-stopped
    oom_score_adj: 0

  broker:
    image: redis:7.0.10
    container_name: webodm_broker
    restart: unless-stopped
    oom_score_adj: -500

  worker:
    image: webodm/webodm_webapp
    container_name: webodm_worker
    entrypoint: /bin/bash -c "/webodm/wait-for-postgres.sh db /webodm/wait-for-it.sh -t 0 broker:6379 -- /webodm/wait-for-it.sh -t 0 webapp:8000 -- /webodm/worker.sh start"
    volumes:
      - ${WO_MEDIA_DIR:-appmedia}:/webodm/app/media:z
    depends_on:
      - db
      - broker
    environment:
      - WO_BROKER=redis://broker:6379/0
      - WO_DEBUG=${WO_DEBUG:-False}
      - WO_SECRET_KEY=${WO_SECRET_KEY:-}
      - WEB_CONCURRENCY=${WEB_CONCURRENCY:-}
    restart: unless-stopped
    oom_score_adj: 250

  node-odx-1:
    image: webodm/nodeodx
    container_name: webodm_nodeodx
    expose:
      - "3000"
    restart: unless-stopped
    oom_score_adj: 500
```

## Hardware Sizing & Requirements

Processing drone imagery is highly resource-intensive. Below is a sizing guide based on dataset size:

- **Bare Minimum**: 4 GB RAM, 64-bit CPU, 20 GB Disk. This is only enough for tiny test datasets (< 100 images). Attempting larger datasets with minimum specs will result in processing crashes and "out of memory" errors.
- **Recommended (Practical Use)**: 16 GB to 32 GB RAM (scales with dataset size), Modern Multi-Core CPU, 100 GB+ SSD. **32 GB+ is ideal for standard commercial projects** (500+ images).
- **Disk Storage**: Large temporary files are generated during photogrammetry processing. Having a fast SSD is critical for performance. Ensure your host system or Docker storage location has 100GB+ of free space.

## Environment Variables & Credentials

> **Important:** This service requires a `.env` file for proper and secure deployment.

The companion `.env` file should contain the following settings:
- **`WO_SECRET_KEY`**: A random, secure string used by the Django backend. You **must** set this to a random value before deploying.
- **`WO_PORT`**: The default is `8000`. Change this if it conflicts with another service in your homelab.
- **`WO_DB_DIR` & `WO_MEDIA_DIR`**: Mappings for Docker volumes.

Please review the included `.env` file and replace placeholder variables like `CHANGEME_YOUR_SECRET_KEY_HERE` with actual secure values before proceeding.

## Deployment Instructions

1. Verify that your `.env` file has been updated with a secure `WO_SECRET_KEY`.
2. Navigate to this directory in your terminal.
3. Start the service by running:
   ```bash
   docker compose up -d
   ```
4. Access the web interface at `http://<your-server-ip>:8000/` (or whichever port you specified in `.env`).
5. On the first launch, you will be prompted to create your initial admin user and password directly in the WebODM UI.
