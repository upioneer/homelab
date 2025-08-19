# Rid the Non Valid License prompt
![screenshot](/assets/Screenshot 2025-08-19 112519.png)
## Manually update `proxmoxlib.js` (needs to be modified after each update)
Connect to your PVE
```bash
ssh root@your-proxmox-ip
nano /usr/share/javascript/proxmox-widget-toolkit/proxmoxlib.js
```
Delete or comment out this block of code (wrap in /* */ to comment the block)
```bash
Ext.Msg.show({
    title: gettext('No valid subscription'),
    ...
});
```
Or comment out
```bash
/*
Ext.Msg.show({
    title: gettext('No valid subscription'),
    ...
});
*/
```
Clear browser cache or restart Proxmox web service
```bash
systemctl restart pveproxy
```
