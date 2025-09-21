# Widgets
## Proxmox API
When following [this guide](https://gethomepage.dev/configs/proxmox/#configuration-options), ensure the **api user** and **api token** have the PVEAuditor role. Not currently called out in the official documentation. See this [GitHub discussion](https://github.com/gethomepage/homepage/discussions/1406) for more.
## Proxmox traffic
Ensure you use local IP in the **services.yml** and **proxmox.yml** if you have a zero trust tunnel set up. It will be blocked otherwise unless you deploy a creative solution.
