# iVentoy
# Method 1
## Proxmox Help Script
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/iventoy.sh)"
```
I recommend this way. Less fuss.

---
# Method 2
## Download the latest release (win32, win64 and linux packages avail)
[GitHub](https://github.com/ventoy/PXE/releases)

## ISOs
Copy ISOs into the extracted /ISO directory. You can create subdirs as needed for organization. Unicode **not** supported.

## Run iVentory
Windows x86
```cmd
iVentoy_32.exe
```
Windows x64
```cmd
iVentoy_64.exe
```
Linux
```bash
sudo bash iventoy.sh start
```
## Open the console
Open the browser and point to the host, port 26000. It should look like one of the following:

`http://x.x.x.x:26000` 

`http://127.0.0.1:26000`

`http://localhost:26000`
## Start the PXE service
You will find this in the console
# Notes
Paraphrased from the [official documentation](https://www.iventoy.com/en/doc_start.html)
