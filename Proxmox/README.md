# Proxmox LXC Toolbox

A collection of scripts, guides, and best practices for managing LXC containers in **Proxmox VE**.

This project is designed to speed up common tasks like building reusable container templates, installing baseline packages, and automating container provisioning with consistency.

---

## Documentation

| Task | Description |
|------|-------------|
| [Create LXC Template](./NewCTTemplate.md) | Guide and script to clean, back up, and rename a container as a reusable template |
| [Install Docker & Compose](../Docker/README.md) | Proper method for installing Docker CE and Docker Compose inside an LXC |
| [Recommended Baseline Apps](./baselineApps.md) | Suggested minimal and extended packages to include in new LXC templates |
| [No Valid Subscription](./NoValidSubscription.md) | Remove the "No valid subscription" prompt when logging in |
| [Map SMB share](./SMBmap.md) | Persistent mapping of SMB shares and exposure to your LXC |

---

## Why This Exists

Tasks can be manual and repetitive. This repo makes it easier to:

- Automate LXC creation with opinionated defaults
- Maintain minimal, clean base templates
- Include repeatable setups for dev environments or service containers

# Default Credentials
Username `admin@example.com`

Password `changeme`
