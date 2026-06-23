# SSH Hardening Guide

This guide provides the technical steps to establish secure key based authentication between a Windows workstation and a Proxmox host

## Phase 1 Local Key Generation

Perform these steps in a Windows PowerShell terminal to create your identity

### Generate the Ed25519 key pair
```powershell
ssh-keygen -t ed25519
```

### Display the public key to copy it
```powershell
cat $env:USERPROFILE/.ssh/id_ed25519.pub
```

## Phase 2 Server Side Configuration

Perform these steps on the Proxmox host terminal to authorize your local key

### Create the secure directory and file structure
```bash
mkdir -p /root/.ssh
chmod 700 /root/.ssh
touch /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys
```

### Add your public key to the authorized list
```bash
echo "PASTE_YOUR_KEY_STRING_HERE" >> /root/.ssh/authorized_keys
```

### Ensure correct file permissions
```bash
chmod 600 /root/.ssh/authorized_keys
```

## Phase 3 System Hardening

Modify the SSH configuration on the Proxmox host to disable password access

### Configure the SSH daemon settings
```bash
sed -i 's/^#?PermitRootLogin./PermitRootLogin prohibit-password/' /etc/ssh/sshd_config
sed -i 's/^#?PasswordAuthentication./PasswordAuthentication no/' /etc/ssh/sshd_config
```

### Restart the service to apply changes
```bash
systemctl restart ssh
```

## Phase 4 Simplified Access

Update the configuration file on your Windows machine at `$env:USERPROFILE/.ssh/config` to enable fast login

```text
Host proxmox
    HostName <PROXMOX_IP_ADDRESS>
    User root
    IdentityFile ~/.ssh/id_ed25519
```

## Phase 5 Verification

Test the new configuration from a new Windows PowerShell window

```powershell
ssh proxmox
```
