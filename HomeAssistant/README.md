
# VM Specs
Memory `4GB`

CPU `2`

BIOS `OVMF (UEFI)`

Display `Default`

Machine `q35`

SCSI `VirtIO SCSI`

Hard Disk `none`

Network Device `virtio`

# Import Image
## Download the image into Proxmox host tmp
Version 16.1 is the latest as of this writing 
```bash
cd /tmp
wget https://github.com/home-assistant/operating-system/releases/download/16.1/haos_ova-16.1.qcow2.xz
xz -d haos_ova-16.1.qcow2.xz
```
## Import to your VM
Find your target VM ID
```bash
pct list
```
Import
```bash
qm importdisk <VM ID> haos_ova-16.1.qcow2 local-lvm
```
Double click and add the attached disk in the hardware panel (SATA or SCSI)
