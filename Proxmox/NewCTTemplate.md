# Create LXC
Go thru the new CT wizard and size appropriately

Install apps, files and configs as needed via Terminal
# Prep for template creation
Clean apt, logs and temp
```bash
apt-get clean

find /var/log -type f -exec truncate -s 0 {} \;

journalctl --rotate
journalctl --vacuum-time=1s

rm -rf /tmp/*
rm -rf /var/tmp/*
```
Remove machine-specific configs
```bash
rm -rf /etc/ssh/*_key*

rm -f /etc/machine-id
rm -f /var/lib/dbus/machine-id

echo "localhost" > /etc/hostname
```
# Template creation
Stop the CT
```bash
pct stop [container number]
```
Create the backup
```bash
vzdump [container number] --dumpdir /var/lib/vz/template/cache --compress zstd
```
Rename (optional)
```bash
mv /var/lib/vz/template/cache/vzdump-lxc-<containernumber>-<timestamp>.tar.zst /var/lib/vz/template/cache/new-template-name.tar.zst
```
Verify template
```bash
ls /var/lib/vz/template/cache/
```
# CT Template as Code
```bash
#!/bin/bash

# Usage: sudo ./build-lxc-template.sh <CTID> <TEMPLATE_NAME>
# Example: sudo ./build-lxc-template.sh 100 ubuntu-24.04-minbase

set -e

CTID="$1"
TEMPLATE_NAME="$2"
CACHE_DIR="/var/lib/vz/template/cache"

if [[ -z "$CTID" || -z "$TEMPLATE_NAME" ]]; then
  echo "Usage: $0 <container_id> <template_name (no extension)>"
  exit 1
fi

echo "==> Installing packages and configuring container $CTID..."

# Define packages to install (one per line for easy editing)
INSTALL_PACKAGES=$(cat <<EOF
curl
git
htop
vim
ufw
EOF
)

while read -r pkg; do
  if [[ -n "$pkg" ]]; then
    echo "Installing: $pkg"
    pct exec "$CTID" -- apt-get install -y "$pkg"
  fi
done <<< "$INSTALL_PACKAGES"

# OPTIONAL: Copy config files or other resources
# Example: pct push "$CTID" ./myconfig.conf /etc/myapp/

echo "==> Cleaning up container $CTID before templating..."

pct exec "$CTID" -- bash -c "
  set -e
  echo 'Cleaning apt cache...'
  apt-get clean

  echo 'Truncating log files...'
  find /var/log -type f -exec truncate -s 0 {} \;

  echo 'Rotating and vacuuming journal logs...'
  journalctl --rotate
  journalctl --vacuum-time=1s

  echo 'Clearing temporary files...'
  rm -rf /tmp/* /var/tmp/*

  echo 'Removing SSH keys and unique IDs...'
  rm -rf /etc/ssh/*_key*
  rm -f /etc/machine-id
  rm -f /var/lib/dbus/machine-id
  echo 'localhost' > /etc/hostname

  echo 'Clearing shell history...'
  history -c
  rm -f /root/.bash_history
"

echo "==> Stopping container $CTID..."
pct stop "$CTID"

echo "==> Creating compressed backup in $CACHE_DIR..."
vzdump "$CTID" --dumpdir "$CACHE_DIR" --compress zstd

BACKUP_FILE=$(ls -t "$CACHE_DIR"/vzdump-lxc-"$CTID"-*.tar.zst | head -n 1)
NEW_TEMPLATE_PATH="$CACHE_DIR/$TEMPLATE_NAME.tar.zst"

echo "==> Renaming backup to template: $NEW_TEMPLATE_PATH"
mv "$BACKUP_FILE" "$NEW_TEMPLATE_PATH"

echo "==> Template ready:"
ls -lh "$NEW_TEMPLATE_PATH"
```
# Run CT Template script
```bash
sudo ./build-lxc-template.sh 100 ubuntu-24.04-minbase
```
