### Recommended Base Packages for LXC Templates

This table outlines useful packages to include in Proxmox LXC container templates. Only install what’s relevant to the role of your template.

| Package                  | Purpose                                     | Category              |
|--------------------------|---------------------------------------------|------------------------|
| `curl`                   | Web requests and API testing                | General Utilities      |
| `wget`                   | File downloads                              | General Utilities      |
| `vim`                    | Text editor (advanced)                      | General Utilities      |
| `nano`                   | Text editor (beginner-friendly)            | General Utilities      |
| `htop`                   | System resource monitor                     | General Utilities      |
| `tmux`                   | Terminal multiplexer                        | General Utilities      |
| `unzip`                  | Extract `.zip` files                        | General Utilities      |
| `bash-completion`        | Tab completion in Bash                      | General Utilities      |
| `lsb-release`            | Distro/version info                         | General Utilities      |
| `net-tools`              | Legacy tools: `ifconfig`, `netstat`        | Networking             |
| `iproute2`               | Modern tools: `ip a`, `ip r`, etc.         | Networking             |
| `dnsutils`               | Tools like `dig`, `nslookup`               | Networking             |
| `nmap`                   | Network/port scanner                        | Networking             |
| `tcpdump`                | Network packet capture                      | Networking             |
| `ufw`                    | Basic firewall management                   | Security               |
| `fail2ban`               | Brute-force protection                      | Security               |
| `openssh-server`         | SSH access (optional in LXC)               | Security               |
| `software-properties-common` | Manage APT sources and PPAs          | System Maintenance     |
| `ca-certificates`        | SSL certificate support for HTTPS          | System Maintenance     |
| `locales`                | Language support                            | System Maintenance     |
| `tzdata`                 | Timezone configuration                     | System Maintenance     |
| `docker.io`              | Docker runtime from Ubuntu repo            | Container / Dev Tools  |
| `docker-compose-plugin`  | Docker Compose v2                          | Container / Dev Tools  |
| `python3`                | Python runtime                             | Container / Dev Tools  |
| `python3-pip`            | Python package manager                     | Container / Dev Tools  |
| `build-essential`        | Compilers and build tools (C/C++)          | Container / Dev Tools  |
| `nodejs`                 | JavaScript runtime                         | Container / Dev Tools  |
| `npm`                    | Node.js package manager                    | Container / Dev Tools  |
| `openjdk-17-jdk`         | Java development kit                       | Container / Dev Tools  |

---

### Template Building Tips

- Install only what’s common to the use case for this template.
- Create separate templates for minimal, dev, or service-specific containers.
- Clean up: remove logs, SSH keys, apt cache, and temp files before exporting.
- Lightweight templates clone faster and consume fewer resources.
