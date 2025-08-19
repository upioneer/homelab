# Install Cloudflared
## Add cloudflare gpg key
```bash
sudo mkdir -p --mode=0755 /usr/share/keyrings
curl -fsSL https://pkg.cloudflare.com/cloudflare-main.gpg | sudo tee /usr/share/keyrings/cloudflare-main.gpg >/dev/null
```
## Add this repo to your apt repositories
```bash
echo 'deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] https://pkg.cloudflare.com/cloudflared any main' | sudo tee /etc/apt/sources.list.d/cloudflared.list
```
## Install Cloudflared
```bash
sudo apt-get update
sudo apt-get install cloudflared
```
# Run Cloudflared tunnel on startup
```bash
sudo cloudflared service install <YOUR_TOKEN_HERE>
```

---
# Baseline config
## Cloudflare Tunnel
Dashboard > Zero Trust > Networks > Tunnels > Create tunnel

Tunnel name `whatever you want`

Connector type `cloudflared`

### Public hostnames
**Hostname**

Subdomain `*`

Domain `yourdomain.com`

Path `*optional*`

**Service**

Type `HTTP`

URL `nginx proxy manager internal IP:80`

## Cloudflare DNS
Dashboard > DNS > Records > Add record

Type `CNAME`

Name `*`

Target `TunnelID.cfargotunnel.com`

Proxy status `Proxied`

TTL `Auto`

## Cloudflare Application
Dashboard > Zero Trust > Access > Applications > Add an application

**Basic information**

Application name `whatever you want`

Session Duration `whatevr you want`

**Public hostname**

Input method `Default`

Subdomain `*`

Domain `yourdomain.com`

Path `*optional*`

**Login method**

Will refer you to this [YouTube video](https://youtu.be/wdmbAo02ktQ?si=lMP74ypMOZK9ka9q&t=360) for GitHub auth setup
