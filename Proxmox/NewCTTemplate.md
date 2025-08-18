# Create LXC
Install apps, files and configs as needed
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
