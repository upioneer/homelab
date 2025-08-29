# Deploying Proxmox a LXC with TrueNAS shares

This guide details the method for running Docker containers inside a Proxmox LXC, with files stored on a separate TrueNAS server via an SMB share

The core principle is to mount the network share on the **Proxmox host** and then pass that directory into the **LXC container** using a bind mount

This is more secure and reliable than trying to mount the share from within the container

---

## Step 1: Mount the SMB Share on the Proxmox Host

First, we need to make the TrueNAS share available to the Proxmox host system. I recommend you create a new, least privilege TrueNAS user for this

### Install CIFS Utilities
```bash
apt update
apt install cifs-utils
```

### Create a Secure Credentials File
```bash
mkdir -p /etc/samba/credentials
nano /etc/samba/credentials/truenas.cred
```

Add the following
```
username=YOUR_SMB_USERNAME
password=YOUR_SMB_PASSWORD
```
Secure it
```bash
chmod 600 /etc/samba/credentials/truenas.cred
```

### Create Mount Point Directories applicable to your app (example below)
```bash
mkdir -p /mnt/truenas_music
mkdir -p /mnt/truenas_photos
```

### Edit /etc/fstab for Automatic Mounting
```bash
nano /etc/fstab
```

Add:
```
//10.0.0.100/music  /mnt/truenas_music  cifs credentials=/etc/samba/credentials/truenas.cred,iocharset=utf8,uid=1000,gid=1000,_netdev,nofail 0 0
//10.0.0.100/photos /mnt/truenas_photos cifs credentials=/etc/samba/credentials/truenas.cred,iocharset=utf8,uid=1000,gid=1000,_netdev,nofail 0 0
```

### Mount and Verify
```bash
mount -a
df -h
```

---

## Step 2: Bind Mount the Host Directory into the LXC

Identify Your LXC ID
```bash
pct list
```

Add the Mount Point(s)
```bash
pct set 101 -mp0 /mnt/truenas_music,mp=/music
pct set 101 -mp1 /mnt/truenas_photos,mp=/photos
```

Reboot the LXC
```bash
pct reboot 101
```

---

## Step 3: Configure docker-compose.yml for Navidrome

When defining the Docker container for Navidrome, map the `/music` directory from the LXC into the container

Example `docker-compose.yml` snippet:

```yaml
    volumes:
      - /music:/music:ro
      - /photos:/photos:ro
```

### Notes on docker-compose.yml Volumes
- `/music:/music:ro` Maps the SMB-mounted share (read-only for safety)
- `/srv/navidrome/data:/data` → Maps a local persistent folder for Navidrome’s database and settings
- Always keep media read-only in Docker containers to avoid accidental changes

---

## Summary

- Mount SMB shares on the Proxmox host using **fstab** and secure credentials
- Bind mount those host directories into the LXC container with `pct set`
- In Docker, map the mounted directories as volumes for Navidrome in `docker-compose.yml`

This method ensures reliable, persistent access to TrueNAS media while maintaining clean separation between host, container, and application layers
