# Openship

[Openship](https://openship.io/) is an open-source, self-hostable deployment platform with built-in CI/CD. It allows you to push code, ship containers, and manage infrastructure from a desktop app, web dashboard, or CLI. Openship aims to provide a zero-configuration pipeline and self-hosted alternative to platforms like Vercel or Railway.

### Configuration

A [docker-compose.yml](docker-compose.yml) file is provided to deploy Openship. Because there are currently no pre-built official Docker images, the Compose file is configured to build the services directly from the source code.

> **Important**: This service requires sensitive credentials, such as your database passwords. A `.env` file has been created in this directory containing placeholder values. You **MUST** edit the `.env` file and replace the placeholders (e.g., `POSTGRES_PASSWORD`) with secure values before deploying the service.

### Deployment Instructions

1. Clone the Openship repository into a `src` subdirectory:
   ```bash
   git clone https://github.com/oblien/openship.git src
   ```

2. Configure your environment variables by editing the `.env` file:
   ```bash
   nano .env
   ```

3. Build and start the service in detached mode:
   ```bash
   docker compose up -d --build
   ```

The dashboard will be available at `http://<your-server-ip>:3001` and the web interface at `http://<your-server-ip>:3000`.

### docker-compose.yml

```yaml
# Openship - Docker Compose

services:
  # ─── Database (storage, private) ──────────────────────
  postgres:
    image: postgres:16-alpine
    restart: unless-stopped
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-openship}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-openship}
      POSTGRES_DB: ${POSTGRES_DB:-openship}
    expose:
      - "5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-openship} -d ${POSTGRES_DB:-openship}"]
      interval: 5s
      timeout: 3s
      retries: 12

  # ─── Cache / Queue / Rate-limit (private) ─────────────
  redis:
    image: redis:7-alpine
    restart: unless-stopped
    command: ["redis-server", "--appendonly", "yes"]
    expose:
      - "6379"
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 12

  # ─── API (control plane) ──────────────────────────────
  api:
    build:
      context: ./src
      dockerfile: apps/api/Dockerfile
    restart: unless-stopped
    ports:
      - "4000:4000"
    env_file:
      - .env
    environment:
      NODE_ENV: production
      PORT: "4000"
      DATABASE_URL: postgresql://${POSTGRES_USER:-openship}:${POSTGRES_PASSWORD:-openship}@postgres:5432/${POSTGRES_DB:-openship}
      REDIS_URL: redis://redis:6379
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    healthcheck:
      test: ["CMD-SHELL", "bun -e \"fetch('http://127.0.0.1:4000/api/health').then(r=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))\""]
      interval: 10s
      timeout: 5s
      retries: 12
      start_period: 40s

  # ─── Dashboard (app UI) ───────────────────────────────
  dashboard:
    build:
      context: ./src
      dockerfile: apps/dashboard/Dockerfile
    restart: unless-stopped
    ports:
      - "3001:3001"
    env_file:
      - .env
    environment:
      NODE_ENV: production
      PORT: "3001"
      INTERNAL_API_URL: http://api:4000
    depends_on:
      api:
        condition: service_healthy

  # ─── Web / Landing ────────────────────────────────────
  web:
    build:
      context: ./src
      dockerfile: apps/web/Dockerfile
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      NODE_ENV: production
      PORT: "3000"

volumes:
  postgres_data:
  redis_data:
```
