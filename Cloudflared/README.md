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
