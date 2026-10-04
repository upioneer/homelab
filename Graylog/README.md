# Graylog

[Graylog](https://graylog.org/) is a leading open-source centralized log management and analysis solution. It captures, stores, and enables real-time search and alerting on log data across servers, network appliances, and containers. This stack deploys Graylog alongside **OpenSearch** for index storage and **MongoDB** for metadata.

## Configuration & Environment Variables

This stack requires credentials and secret hashes in a [`.env`](.env) file before first launch.

> [!CAUTION]
> You **MUST** update [`.env`](.env) before starting Graylog:
> 1. `GRAYLOG_PASSWORD_SECRET`: A secret salt with a minimum length of 16 characters (can be generated using `openssl rand -hex 16` or `pwgen -N 1 -s 96`).
> 2. `GRAYLOG_ROOT_PASSWORD_SHA2`: The SHA256 hash of your intended admin password. Create one in bash using:
>    ```bash
>    echo -n "YourSecretPassword" | sha256sum | cut -d" " -f1
>    ```
> 3. `GRAYLOG_HTTP_EXTERNAL_URI`: The public or LAN address where clients access Graylog (default: `http://localhost:9000/`).

## Deployment Instructions

Ensure the host kernel parameter `vm.max_map_count` is set to at least `262144` for OpenSearch (e.g., `sysctl -w vm.max_map_count=262144`).

Navigate to this directory and start the stack:

```bash
docker compose up -d
```

Once running, access the Graylog web console at:

```
http://<your-server-ip>:9000
```

- **Username:** `admin`
- **Password:** The plaintext password you used to generate `GRAYLOG_ROOT_PASSWORD_SHA2`.

To view logs or stop the stack:

```bash
# View live logs
docker compose logs -f

# Stop the stack
docker compose down
```

## Docker Compose File

The companion compose file is available at [docker-compose.yml](docker-compose.yml):

```yaml
services:
  mongodb:
    image: mongo:6.0
    container_name: graylog-mongodb
    restart: unless-stopped
    volumes:
      - mongodb_data:/data/db

  opensearch:
    image: opensearchproject/opensearch:2.15.0
    container_name: graylog-opensearch
    restart: unless-stopped
    environment:
      - "OPENSEARCH_JAVA_OPTS=-Xms1g -Xmx1g"
      - "bootstrap.memory_lock=true"
      - "discovery.type=single-node"
      - "action.auto_create_index=false"
      - "plugins.security.disabled=true"
    ulimits:
      memlock:
        soft: -1
        hard: -1
      nofile:
        soft: 65536
        hard: 65536
    volumes:
      - opensearch_data:/usr/share/opensearch/data

  graylog:
    image: graylog/graylog:6.1
    container_name: graylog-server
    restart: unless-stopped
    depends_on:
      - mongodb
      - opensearch
    ports:
      - "9000:9000"
      - "1514:1514"
      - "1514:1514/udp"
      - "12201:12201"
      - "12201:12201/udp"
    environment:
      - GRAYLOG_PASSWORD_SECRET=${GRAYLOG_PASSWORD_SECRET}
      - GRAYLOG_ROOT_PASSWORD_SHA2=${GRAYLOG_ROOT_PASSWORD_SHA2}
      - GRAYLOG_HTTP_EXTERNAL_URI=${GRAYLOG_HTTP_EXTERNAL_URI:-http://localhost:9000/}
      - GRAYLOG_OPENSEARCH_URI=http://opensearch:9200
      - GRAYLOG_MONGODB_URI=mongodb://mongodb:27017/graylog
    volumes:
      - graylog_data:/usr/share/graylog/data

volumes:
  mongodb_data:
  opensearch_data:
  graylog_data:
```
