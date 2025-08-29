## Ensure you use the same user and group ID (UID, GID) in the docker-compose.yaml as you did when mapping on the Proxmox host

Map snippet
```bash
//10.0.0.100/music  /mnt/truenas_music  cifs credentials=/etc/samba/credentials/truenas.cred,iocharset=utf8,uid=1000,gid=1000,_netdev,nofail 0 0
//10.0.0.100/photos /mnt/truenas_photos cifs credentials=/etc/samba/credentials/truenas.cred,iocharset=utf8,uid=1000,gid=1000,_netdev,nofail 0 0
```
Yaml snippet
```yml
    user: 1000:1000 
```
## Reference
[Map SMB share](../Proxmox/SMBmap.md)
