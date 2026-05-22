# Notifuse Setup

[Notifuse](https://www.notifuse.com/) is an open-source, self-hosted emailing platform designed for sending newsletters and transactional emails. It features event-driven automation, Liquid-based dynamic templates, a REST API, and native support for major email service providers like Amazon SES, Mailgun, Postmark, SparkPost, or generic SMTP.

## Docker Compose Configurations

### Option 1: Full Stack with PostgreSQL and Watchtower (Recommended)

This configuration includes Notifuse, a dedicated PostgreSQL database, and a Watchtower container that checks for image updates and cleans up obsolete layers daily at 4:00 AM.

```yaml
services:
  notifuse:
    image: notifuse/notifuse:latest
    container_name: notifuse
    ports:
      - "8081:8080"
    environment:
      - SERVER_PORT=8080
      - SERVER_HOST=0.0.0.0
      - ENVIRONMENT=production
      - DB_HOST=notifuse-db
      - DB_PORT=5432
      - DB_USER=postgres
      - DB_PASSWORD=postgres # Change this in production
      - DB_NAME=notifuse_system
      - SECRET_KEY=d04zCk3Fa45oOjDWHpAvc1AZxnLdGffOnNWK+Jt2yXf37+FTfuMMHb8flcfPMqLluRR3rvhbr555r6j1DEigrA== # Generated random key
    depends_on:
      - notifuse-db
    restart: unless-stopped

  notifuse-db:
    image: postgres:17-alpine
    container_name: notifuse-db
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=notifuse_system
    volumes:
      - notifuse-db-data:/var/lib/postgresql/data
    restart: unless-stopped

  watchtower:
    image: containrrr/watchtower
    container_name: watchtower-notifuse
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --schedule "0 0 4 * * *" --cleanup
    restart: unless-stopped

volumes:
  notifuse-db-data:
```

---

## Deployment Steps

1. **Deploy the service**:
   ```bash
   docker compose up -d
   ```

2. **First-run Setup Wizard**:
   Navigate to `http://<host-ip>:8081` in your browser. You will be greeted by the **Setup Wizard** which will guide you through:
   - Creating a root administrator account (email & password).
   - Setting your base API endpoint URL (e.g., `http://<host-ip>:8081` or your public domain).
   - Scaffolding out SMTP / Transactional email settings.

3. **Secure Your Instance**:
   Before deploying to production, it is highly recommended to:
   - Change the `DB_PASSWORD` configuration to a secure string.
   - Generate a custom `SECRET_KEY` by running `openssl rand -base64 32` or similar securely and specifying it in the environments section. Do not change the `SECRET_KEY` after completing the setup, as it is used to encrypt API secrets and database values.
