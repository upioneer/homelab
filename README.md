[![GitHub Stars](https://img.shields.io/github/stars/upioneer/homelab?style=flat-square&color=yellow)](https://github.com/upioneer/homelab/stargazers)
[![Forks](https://img.shields.io/github/forks/upioneer/homelab?style=flat-square&color=green)](https://github.com/upioneer/homelab/network/members)
[![Issues](https://img.shields.io/github/issues/upioneer/homelab?style=flat-square&color=red)](https://github.com/upioneer/homelab/issues)
[![Contributors](https://img.shields.io/github/contributors/upioneer/homelab?style=flat-square&color=blue)](https://github.com/upioneer/homelab/graphs/contributors)

---
# Apps and recommended sizing
| Name | Type | CPU | Mem | Min Disk |
| :--- | :--: | :-: | :---: | :---: |
| [AdGuard Home](https://adguard.com/en/adguard-home/overview.html)<br>Network-wide ad and tracker blocking DNS server | LXC | 1 | 256MB | 512MB |
| [Ansible](https://www.ansible.com/)<br>IT automation and configuration management tool | VM | 1 | 1GB | 2GB |
| [Anytype](https://anytype.io/)<br>Local-first, open-source Notion alternative for notes and knowledge management | VM | 2 | 2GB | 5GB |
| [AppFlowy](https://www.appflowy.io/)<br>Open-source Notion alternative with a focus on data privacy | VM | 2 | 2GB | 5GB |
| [Audiobookshelf](https://www.audiobookshelf.org/)<br>Self-hosted audiobook and podcast server | LXC | 1 | 512MB | 5GB+ |
| [Automatic Ripping Machine (ARM)](https://b3n.org/automatic-ripping-machine)<br>Automated CD/DVD/Blu-ray ripping | VM | 2-4 | 2GB | 20GB+ |
| [Bazarr](https://www.bazarr.media/)<br>Automated subtitle management for media libraries | LXC | 1 | 512MB | 2GB |
| [Bitwarden](https://bitwarden.com/)<br>Password manager | VM | 2 | 2GB | 5GB |
| [Bookstack](https://www.bookstackapp.com/)<br>Simple platform for organizing documentation and knowledge | LXC | 1 | 512MB | 2GB |
| [BorgBackup](https://www.borgbackup.org/)<br>Deduplicating backup program | LXC | 1 | 1GB | 2GB |
| [Caddy](https://caddyserver.com/)<br>Web server with automatic HTTPS | LXC | 1 | 256MB | 1GB |
| [Calibre-Web](https://github.com/janeczku/calibre-web)<br>Web app for browsing eBooks | LXC | 1 | 512MB | 2GB |
| [CasaOS](https://casaos.zimaspace.com/)<br>Open-source personal cloud system | LXC | 1-2 | 1GB | 8GB |
| [Changedetection.io](https://github.com/dgtlmoon/changedetection.io)<br>Monitor websites and receive notifications on changes | LXC | 1-2 | 1GB | 5GB |
| [checkmk](https://checkmk.com)<br>Infrastructure monitoring | VM | 2-4 | 4GB | 8GB |
| [CloudFlared](https://github.com/cloudflare/cloudflared)<br>Cloudflare Tunnel daemon | LXC | 1 | 256MB | 512MB |
| [Cockpit](https://cockpit-project.org/)<br>Web-based graphical interface for servers | LXC | 1 | 512MB | 2GB |
| [Code-Server](https://github.com/coder/code-server)<br>Run VS Code in the browser | VM | 2 | 2GB | 5GB |
| [Compose Toolbox](https://github.com/bluegoosemedia/composetoolbox)<br>Simple web UI for Docker Compose | LXC | 1 | 256MB | 1GB |
| [Cosmos](https://cosmos-cloud.io/)<br>Self-hosting server and container management platform | LXC | 1-2 | 1GB | 8GB |
| [Crawl4AI](https://docs.crawl4ai.com/)<br>Python library to crawl and extract data from websites for LLMs | VM | 1 | 1GB | 2GB |
| [Cronmaster](https://github.com/fccview/cronmaster)<br>Simple and lightweight cron job manager | LXC | 1 | 256MB | 1GB |
| [CryptPad](https://cryptpad.fr/)<br>Zero-knowledge, end-to-end encrypted collaborative suite | VM | 2 | 2GB | 5GB |
| [Dasharr](https://github.com/taslabs-net/dasharr)<br>Dashboard for the Servarr stack | LXC | 1 | 256MB | 1GB |
| [Dashy](https://dashy.to/)<br>Highly customizable personal dashboard | LXC | 1 | 512MB | 1GB |
| [dockpeek](https://github.com/dockpeek/dockpeek)<br>Simple dashboard to view and manage Docker containers | LXC | 1 | 256MB | 1GB |
| [Dockge](https://dockge.kuma.pet)<br>Docker Compose management UI | LXC | 1 | 512MB | 2GB |
| [Docker](https://www.docker.com)<br>Containerization platform | VM | 2+ | 2GB+ | 10GB+ |
| [DocuWiki](https://www.dokuwiki.org/dokuwiki)<br>File-based wiki engine | LXC | 1 | 512MB | 1GB |
| [Dozzle](https://dozzle.dev/)<br>Container log viewer | LXC | 1 | 256MB | 1GB |
| [dtop](https://github.com/amir20/dtop)<br>Docker top alternative with container stats and logs | LXC | 1 | 256MB | 1GB |
| [Duplicati](https://www.duplicati.com/)<br>Secure, encrypted, and compressed backup client | LXC | 1 | 512MB | 1GB |
| [Emby](https://emby.media/)<br>Personal media server | VM | 2-4+ | 4GB+ | 20GB+ |
| [ErsatzTV](https://github.com/ErsatzTV/ErsatzTV)<br>Self-hosted pseudo-TV for Plex, Jellyfin, and Emby | VM | 2-4 | 2-4GB | 10GB+ |
| [Etherpad](https://etherpad.org/)<br>Real-time collaborative text editor | LXC | 1 | 512MB | 1GB |
| [FileStash](https://filestash.app/)<br>Web-based file manager that connects to various backends | LXC | 1 | 512MB | 1GB |
| [FileZilla Server](https://filezilla-project.org/)<br>FTP server for file sharing | LXC | 1 | 256MB | 1GB |
| [Firecrawl](https://firecrawl.dev/)<br>Turn any website into LLM-ready data (crawl, scrape, search, etc.) | VM | 2 | 2-4GB | 10GB |
| [Flame](https://github.com/pawelmalak/flame)<br>Self-hosted startpage and dashboard for your server | LXC | 1 | 256MB | 1GB |
| [FocusWriter](https://gottcode.org/focuswriter/)<br>Distraction-free writing environment | VM | 1 | 512MB | 1GB |
| [FreeCAD](https://www.freecad.org/)<br>3D modeler | VM | 2-4 | 4GB+ | 10GB |
| [FreeMind](https://freemind.sourceforge.net/wiki/index.php/Main_Page)<br>Mind-mapping software | VM | 1 | 512MB | 1GB |
| [Frigate NVR](https://frigate.video)<br>NVR with AI object detection | VM | 2-4 | 4GB+ | 32GB+ |
| [Funkwhale](https://funkwhale.audio/)<br>Federated audio streaming server | LXC | 1-2 | 1GB | 5GB+ |
| [Ghost](https://ghost.org/)<br>Professional publishing platform | LXC | 1-2 | 1GB | 5GB |
| [Gitea](https://gitea.io/en-us/)<br>Self-hosted Git service | LXC | 1-2 | 1GB | 5GB+ |
| [Glance](https://github.com/glanceapp/glance)<br>At-a-glance, self-hosted dashboard for your services | LXC | 1 | 256MB | 1GB |
| [Gluetun](https://github.com/qdm12/gluetun)<br>VPN client container for other containers to use | LXC | 1 | 128MB | 512MB |
| [Grafana](https://grafana.com)<br>Monitoring and data visualization | LXC | 1-2 | 1GB | 2GB |
| [Grocy](https://grocy.info/)<br>ERP system for your household and kitchen | LXC | 1 | 512MB | 2GB |
| [Harvester](https://www.harvesterhci.io/)<br>Kubernetes-based hyper-converged infrastructure | VM | 4+ | 8GB+ | 100GB+ |
| [Heimdall](https://heimdall.site/)<br>Elegant dashboard for your web applications | LXC | 1 | 256MB | 1GB |
| [Home Assistant](https://www.home-assistant.io/)<br>Open-source home automation hub | VM | 2 | 2GB | 10GB |
| [Homarr](https://homarr.dev/)<br>Simple, modern, and powerful server dashboard | LXC | 1 | 512MB | 1GB |
| [Homepage](https://gethomepage.dev/)<br>Modern and dynamic application dashboard | LXC | 1 | 512MB | 1GB |
| [Immich](https://immich.app)<br>Photo and video backup solution | VM | 2-4 | 4GB+ | 32GB+ |
| [InfluxDB](https://www.influxdata.com)<br>Time-series database | VM | 1-2 | 2GB | 4GB |
| [Instantly.ai](https://instantly.ai/)<br>SaaS platform for cold email outreach and lead management | | | | |
| [iVentoy](https://www.iventoy.com/en/index.html)<br>PXE server to boot multiple ISO files over a network | VM | 1-2 | 1GB | 5GB+ |
| [IT-Tools](https://github.com/sharevb/it-tools)<br>Collection of handy online tools for developers | LXC | 1 | 128MB | 512MB |
| [Jellyfin](https://jellyfin.org)<br>Media streaming system | VM | 2-4 | 4GB+ | 20GB+ |
| [Jellyseerr](https://docs.jellyseerr.dev)<br>Request management for media libraries | LXC | 1 | 512MB | 2GB |
| [Joplin](https://joplinapp.org/)<br>Open-source note-taking and to-do app | LXC | 1 | 512MB | 2GB |
| [Kavita](http://www.kavitareader.com/)<br>Cross-platform reading server | LXC | 1 | 1GB | 5GB+ |
| [Kestra](https://kestra.io/)<br>Data orchestration platform | VM | 2 | 2GB | 5GB |
| [Kiwix](https://kiwix.org/en/)<br>Offline internet access | LXC | 1 | 1GB | 5GB+ |
| [Kubernetes](https://kubernetes.io/)<br>Container orchestration system | VM | 2+ | 4GB+ | 20GB+ |
| [Lidarr](https://lidarr.audio/)<br>Automated music collection manager | LXC | 1 | 512MB | 5GB+ |
| [LinkAce](https://www.linkace.org/)<br>Self-hosted bookmark archive | LXC | 1 | 512MB | 2GB |
| [Linkarr](https://github.com/itsmejoeeey/linkarr)<br>Self-hosted, custom link-in-bio page | LXC | 1 | 256MB | 1GB |
| [LinkStack](https://linkstack.org/)<br>Linktree alternative | LXC | 1 | 256MB | 1GB |
| [Linkwarden](https://linkwarden.app/)<br>Collaborative bookmark and archival manager | LXC | 1 | 1GB | 5GB |
| [Logseq](https://logseq.com/)<br>Privacy-first, open-source knowledge management system | LXC | 1 | 512MB | 2GB |
| [Marreta](https://github.com/sikkgit/marreta-paywall-bypass/blob/main/README.en.md)<br>Paywall bypass | LXC | 1 | 128MB | 512MB |
| [Material Design Icons](https://pictogrammers.com/library/mdi/)<br>Community-driven library of Material Design icons | | | | |
| [Mealie](https://mealie.io/)<br>Recipe manager and meal planner | LXC | 1 | 1GB | 5GB |
| [Metabase](https://www.metabase.com/)<br>Business intelligence | VM | 2 | 2GB | 5GB |
| [MinIO](https://min.io/)<br>High-performance object storage server | LXC | 1 | 1GB | 2GB |
| [n8n](https://n8n.io)<br>Workflow automation | VM | 2 | 2GB | 5GB |
| [Navidrome](https://www.navidrome.org/)<br>Music streaming server | LXC | 1 | 512MB | 5GB+ |
| [netboot.xyz](https://netboot.xyz/)<br>Network bootable operating system installer | LXC | 1 | 256MB | 2GB |
| [Netbox](https://netbox.dev/)<br>IP address management and data center infrastructure management | VM | 2 | 2GB | 10GB |
| [Netdata](https://netdata.cloud/)<br>Real-time performance monitoring | LXC | 1 | 512MB | 2GB |
| [Nextcloud](https://nextcloud.com)<br>Remote collaboration platform | VM | 2-4 | 4GB+ | 40GB+ |
| [Nginx Proxy Manager](https://nginxproxymanager.com/)<br>Nginx reverse proxy with a web UI | LXC | 1 | 256MB | 1GB |
| [Node-RED](https://nodered.org/)<br>Flow-based visual programming tool | LXC | 1 | 512MB | 2GB |
| [Notifiarr](https://notifiarr.com/)<br>Unified notifications for the Servarr stack | LXC | 1 | 256MB | 1GB |
| [Ntfy](https://ntfy.sh/)<br>Simple push notification service | LXC | 1 | 256MB | 512MB |
| [NUT server](https://networkupstools.org)<br>Network UPS monitoring | LXC | 1 | 256MB | 512MB |
| [Octoprint](https://octoprint.org)<br>Web interface for 3D printers | VM | 1-2 | 1GB | 2GB |
| [OpenProject](https://www.openproject.org/)<br>Comprehensive project management software | VM | 2 | 2GB | 5GB |
| [OpenVPN](https://openvpn.net/)<br>Robust VPN solution | VM | 1 | 512MB | 2GB |
| [Overseerr](https://overseerr.dev/)<br>Request management and discovery for media libraries | LXC | 1 | 512MB | 2GB |
| [Packer](https://developer.hashicorp.com/packer)<br>Machine image creation tool | VM | 1 | 1GB | 2GB |
| [Paperless NGX](https://docs.paperless-ngx.com/)<br>Document management system | VM | 2-4 | 4GB+ | 20GB+ |
| [pfSense](https://www.pfsense.org)<br>Firewall and router platform | VM | 2 | 2GB | 8GB |
| [PhotoPrism](https://www.photoprism.app/)<br>AI-powered photos app | VM | 2-4 | 4GB+ | 20GB+ |
| [pi-dash](https://github.com/SurajVerma/pi-dash)<br>Simple, lightweight dashboard for Raspberry Pi | LXC | 1 | 256MB | 1GB |
| [Pi-hole](https://pi-hole.net)<br>Network-wide ad blocker | LXC | 1 | 256MB | 512MB |
| [Pi.Alert](https://github.com/leiweibau/Pi.Alert)<br>WIFI / LAN intruder detector | LXC | 1 | 512MB | 2GB |
| [Plex](https://www.plex.tv/)<br>Personal media server | VM | 2-4+ | 4GB+ | 20GB+ |
| [Portainer](https://www.portainer.io)<br>Container management platform | VM | 1-2 | 1GB | 2GB |
| [Porttracker](https://github.com/Mostafa-Wahied/portracker)<br>Lightweight container to track your container port mappings | LXC | 1 | 128MB | 512MB |
| [Postiz](https://postiz.com/)<br>Social media post scheduler | LXC | 1 | 1GB | 2GB |
| [Prometheus](https://prometheus.io/)<br>Systems monitoring and alerting | LXC | 1-2 | 2GB | 4GB |
| [Proxmox](https://www.proxmox.com/en)<br>Server virtualization management | VM | 2+ | 4GB+ | 16GB+ |
| [Proxmox Backup Server](https://www.proxmox.com/en/products/proxmox-backup-server/overview)<br>Enterprise backup solution for VMs, containers, and hosts | VM | 2-4 | 4GB+ | 32GB+ |
| [Prowlarr](https://prowlarr.com/)<br>Indexer manager for the Servarr stack | LXC | 1 | 512MB | 2GB |
| [Pterodactyl](https://pterodactyl.io/)<br>Game server management panel | VM | 2 | 2GB | 10GB |
| [qBittorrent](https://www.qbittorrent.org/)<br>Open-source BitTorrent client with a web UI | LXC | 1-2 | 1GB | 5GB+ |
| [Radarr](https://radarr.video/)<br>Automated movie collection manager | LXC | 1 | 512MB | 5GB+ |
| [Readarr](https://readarr.com/)<br>Automated ebook and audiobook collection manager | LXC | 1 | 512MB | 5GB+ |
| [Reactive Resume](https://rxresu.me/)<br>Resume builder | LXC | 1 | 512MB | 1GB |
| [RomM](https://romm.app/)<br>Retro game library manager | LXC | 1 | 1GB | 5GB+ |
| [Rsync](https://rsync.samba.org/)<br>Fast, incremental file transfer and synchronization utility | LXC | 1 | 512MB | 1GB |
| [RustDesk](https://rustdesk.com/)<br>Remote access and support utility | LXC | 1 | 256MB | 1GB |
| [rwMarkable](https://github.com/fccview/rwMarkable)<br>Self-hosted, collaborative markdown editor | LXC | 1 | 512MB | 2GB |
| [Self-Host Dashboard Icons](https://selfh.st/icons/)<br>Curated collection of icons for self-hosted services | | | | |
| [Servarr Stack](https://wiki.servarr.com/)<br>Suite of media management and automation tools | | | | |
| [Shiori](https://github.com/go-shiori/shiori)<br>Simple bookmark manager | LXC | 1 | 512MB | 2GB |
| [Simple Icons](https://simpleicons.org/)<br>Library of free SVG icons for popular brands | | | | |
| [Sonarr](https://sonarr.tv/)<br>Automated TV show collection manager | LXC | 1 | 512MB | 5GB+ |
| [Stirling-PDF](https://stirlingpdf.io)<br>Web-based PDF manipulation tool | VM | 2 | 2-4GB | 8GB |
| [Subsonic](http://www.subsonic.org/pages/index.jsp)<br>Personal media streamer | LXC | 1 | 512MB | 5GB+ |
| [Syncthing](https://syncthing.net/)<br>Continuous file synchronization | LXC | 1 | 512MB | 2GB |
| [Tailscale](https://tailscale.com)<br>Zero-configuration VPN | LXC | 1 | 256MB | 512MB |
| [Taiga](https://www.taiga.io/)<br>Project management platform for agile teams | VM | 2 | 2GB | 5GB |
| [Tautulli](https://tautulli.com)<br>Monitoring and tracking application for Plex Media Server | LXC | 1 | 512MB | 2GB |
| [Technitium](https://technitium.com/dns/)<br>DNS server | LXC | 1 | 512MB | 1GB |
| [Terraform](https://www.terraform.io/)<br>Infrastructure as code (IaC) tool | VM | 1 | 1GB | 2GB |
| [Tracktor](https://github.com/javedh-dev/tracktor)<br>Privacy-friendly, self-hosted time tracking tool | LXC | 1 | 256MB | 1GB |
| [Traefik](https://traefik.io)<br>Cloud-native edge router and reverse proxy | LXC | 1 | 256MB | 1GB |
| [Trilium](https://github.com/TriliumNext/Trilium)<br>Hierarchical note-taking application | LXC | 1-2 | 1GB | 5GB+ |
| [TrueNAS](https://www.truenas.com)<br>Network-attached storage (NAS) solution | VM | 2-4 | 8GB+ | 32GB+ |
| [Unbound](https://nlnetlabs.nl/projects/unbound/about/)<br>Validating, recursive, and caching DNS resolver | LXC | 1 | 256MB | 512MB |
| [Uptime Kuma](https://uptime.kuma.pet)<br>Self-hosted uptime monitoring | LXC | 1 | 512MB | 1GB |
| [Veloren](https://veloren.net/)<br>Open-world RPG | VM | 2-4 | 4GB+ | 10GB |
| [Ventoy](https://www.ventoy.net/en/index.html)<br>Tool to create a multi-boot USB drive from ISO files | VM | 1 | 1GB | 2GB |
| [VirtualBox](https://www.virtualbox.org)<br>Desktop virtualization | VM | 1+ | 1GB+ | 10GB+ |
| [Watchtower](https://containrrr.dev/watchtower/)<br>Automated Docker container updater | LXC | 1 | 128MB | 512MB |
| [Wekan](https://wekan.github.io/)<br>Open-source Kanban board | LXC | 1 | 512MB | 2GB |
| [Wiki.js](https://js.wiki/)<br>Wiki engine | LXC | 1-2 | 1GB | 5GB+ |
| [WireGuard](https://www.wireguard.com/)<br>Fast, modern, and simple VPN | LXC | 1 | 256MB | 512MB |
| [YOURLS](https://yourls.org/)<br>Link shortener | LXC | 1 | 256MB | 512MB |
| [your_spotify](https://github.com/Yooooomi/your_spotify)<br>Self-hosted tracker for your Spotify listening habits | LXC | 1 | 512MB | 2GB |
| [YouTrack](https://www.jetbrains.com/youtrack/)<br>Project management and issue tracking tool | VM | 2-4 | 4GB+ | 20GB |
| [ZoneMinder](https://zoneminder.com/)<br>Video camera security and surveillance | VM | 2-4 | 4GB+ | 32GB+ |
