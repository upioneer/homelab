# Home Assistant OS Setup on Proxmox VE

This guide covers deploying a clean Home Assistant OS instance as a KVM Virtual Machine on Proxmox VE, resolving UEFI Secure Boot conflicts, and troubleshooting browser authentication failures on non RFC1918 subnets.

---

# VM Hardware Specifications

* Memory: 4096 MB
* Cores: 2
* CPU: Host
* BIOS: OVMF UEFI
* Display: Default
* Machine Type: q35
* SCSI Controller: VirtIO SCSI
* Hard Disk: None provisioned initially
* Network Device: VirtIO bridge vmbr0

---

# Step 1 Download and Extract Image

Download and decompress the official KVM OVA image in the Proxmox host shell:

cd /tmp
wget https://github.com/home-assistant/operating-system/releases/download/16.1/haos_ova-16.1.qcow2.xz
unxz haos_ova-16.1.qcow2.xz

---

# Step 2 Create and Provision Virtual Machine

Replace 200 with your target VM ID and local lvm with your storage pool name. Note that qm list identifies VMs, whereas pct list is reserved for LXC containers.

Create the base VM configuration:

qm create 200 \
  --name haos \
  --memory 4096 \
  --cores 2 \
  --cpu host \
  --bios ovmf \
  --machine q35 \
  --net0 virtio,bridge=vmbr0 \
  --scsihw virtio-scsi-pci

Add the EFI disk with Secure Boot enrollment disabled because HAOS does not support Secure Boot:

qm set 200 --efidisk0 local-lvm:0,efitype=4m,pre-enrolled-keys=0

Import the extracted disk into the storage pool:

qm importdisk 200 /tmp/haos_ova-16.1.qcow2 local-lvm

Attach the imported volume as the primary SCSI boot drive:

qm set 200 --scsi0 local-lvm:vm-200-disk-1,discard=on

Set boot priority to scsi0 and start the machine:

qm set 200 --boot order=scsi0
qm start 200

Note on disk layout: HAOS manages its own boot and data partitions on a single disk. Always attach the image as scsi0 rather than secondary storage like scsi1. The 4MB volume belongs strictly on efidisk0.

---

# Step 3 Post Boot Diagnostics and Troubleshooting

## Issue A UEFI Boot Failure Access Denied

Symptom: The console shows BdsDxe failed to load Boot0001 Access Denied.
Root cause: Secure Boot keys are active on the EFI disk.
Resolution: Recreate efidisk0 without enrolled keys:

qm stop 200
qm set 200 --delete efidisk0
qm set 200 --efidisk0 local-lvm:0,efitype=4m,pre-enrolled-keys=0
qm start 200

## Issue B Onboarding Authentication Failure

Symptom: Browser displays Invalid client id or Ah snap something went wrong during initial user setup.
Root cause: Modern Chromium browsers enforce Secure Context rules. Accessing plain HTTP on IP ranges outside RFC 1918 space blocks window crypto subtle, causing OAuth client validation to break.

Resolution Method 1 Enable Insecure Origins in Chromium or Edge:

1. Open chrome://flags/#unsafely-treat-insecure-origin-as-secure in the address bar.
2. Switch the flag to Enabled.
3. Add the exact endpoint into the input box: http://<HA_IP_ADDRESS>:8123
4. Select Relaunch.
5. Reopen http://<HA_IP_ADDRESS>:8123/ in a fresh tab to complete onboarding.

Resolution Method 2 Use Local mDNS:

Browsers automatically treat dot local hostnames as secure environments:

http://homeassistant.local:8123

---

# Step 4 Rapid Disk Reset Procedure

To restore the machine back to a clean factory state without recreating the VM container configuration:

qm stop 200
qm disk unlink 200 --idlist scsi0 --force 1
lvremove -y /dev/pve/vm-200-disk-1
qm importdisk 200 /tmp/haos_ova-16.1.qcow2 local-lvm
qm set 200 --scsi0 local-lvm:vm-200-disk-1,discard=on
qm set 200 --boot order=scsi0
qm start 200

---

# Step 5 Install and Configure HACS

HACS requires downloading the integration files into the HAOS custom components directory, restarting the core service, and completing GitHub device authorization.

## Method A Terminal Download via HAOS Console or SSH

Open the HAOS terminal session or use the Terminal and SSH app:

wget -O - https://get.hacs.xyz | bash -

## Method B App Store GUI Installation

1. Navigate to Settings then Apps.
2. Select the App Store icon.
3. Open the top right context menu and select Repositories.
4. Add the HACS repository URL:
   https://github.com/hacs/addons
5. Locate Get HACS under the new repository section and select Install.
6. Start the app and verify the log shows installation complete.

## Enable the Integration

1. Navigate to Settings then System and trigger a complete Home Assistant restart.
2. Hard refresh the browser session using Ctrl F5 or Cmd Shift R.
3. Navigate to Settings then Devices and Services.
4. Select Add Integration and search for HACS.
5. Accept the warning dialogs.
6. Open the provided GitHub device activation link, supply the eight character validation key, and confirm authorization.
7. Verify that HACS appears on the left navigation sidebar.
