# Install Docker
```bash
sudo apt-get update
sudo apt-get install docker.io
```
# Install cURL
```bash
sudo apt-get update
sudo apt-get install curl
```
# Install Docker Compose
```bash
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
# Grant permissions (optional)
To remove need for `sudo` prefix
```bash
sudo usermod -aG userName
```
# Apply new group memberships
To remove need to log out/in
```bash
newgrp docker
```
# Start and enable Docker Service
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

---
# Nuclear destroy all Docker artifacts
```bash
sudo docker stop $(sudo docker ps -aq) 2>/dev/null
sudo docker rm -f $(sudo docker ps -aq) 2>/dev/null
sudo docker rmi -f $(sudo docker images -aq) 2>/dev/null
sudo docker volume rm -f $(sudo docker volume ls -q) 2>/dev/null
sudo docker network rm $(sudo docker network ls -q | grep -v 'bridge\|host\|none') 2>/dev/null
```
