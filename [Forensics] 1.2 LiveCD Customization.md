# LiveCD Customization Guide

This tiny definitely-not-complete-guide was written to demonstrate the basic principle 
of customizing bootable LiveCD images for Ubuntu Desktop, Kali Linux, and Windows 10. 


## I. Ubuntu
**N.B.** The following was checked with `ubuntu-22.04.3-desktop-amd64.iso` image and `Ubuntu 22.04.3 Desktop` host 
environment on 19.11.2023 23:43 SAMT.

The best way to set up your host environment for customization is to use the same OS distro and version 
and update the host.

### 0. Update the host
Update the host environment:
```bash
sudo apt-get update
sudo apt-get upgrade
sudo reboot
```

### 1. Install the requirements
```bash
sudo apt-get install -y squashfs-tools xorriso isolinux schroot
```

### 2. Get the iso and mount it
```bash
wget "https://ubuntu.com/download/desktop/thank-you?version=22.04.3&architecture=amd64" -o /tmp/ubuntu-22.04.3-desktop-amd64.iso
export IMAGE_NAME="ubuntu-22.04.3-desktop-amd64"
```
```bash
mkdir /tmp/livecd
sudo mount -o loop /tmp/$IMAGE_NAME.iso /tmp/livecd
```

### 3. Create the installation root and copy the contents
```bash
mkdir -p /tmp/rootfs && cd /tmp/rootfs
mkdir cd squashfs custom

rsync --exclude=/casper/filesystem.squashfs -a /tmp/livecd/ /tmp/rootfs/cd --progress
sudo modprobe squashfs
sudo mount -t squashfs -o loop /tmp/livecd/casper/filesystem.squashfs /tmp/rootfs/squashfs/
sudo cp -a /tmp/rootfs/squashfs/* /tmp/rootfs/custom
```

### 4. Make sure DNS resolve will work after chroot
```bash
sudo cp /etc/resolv.conf /etc/hosts /tmp/rootfs/custom/etc/
```

### 5. Chroot and create pseudo fs roots
```bash
sudo chroot /tmp/rootfs/custom /bin/bash -l
mount -t proc none /proc/
mount -t sysfs none /sys/
```

### 6. Customizing
Install the packages:
```bash
cp /etc/apt/sources.list /etc/apt/sources.list.original
echo "deb http://archive.ubuntu.com/ubuntu/ jammy universe restricted" >> /etc/apt/sources.list
apt-get update

apt-get -y install sleuthkit
apt-get -y install dc3dd

mv /etc/apt/sources.list.original /etc/apt/sources.list
apt-get update
```
Disable disks automounting service:
```bash
systemctl disable udisks2.service
```

### 7. Cleanup
```bash
apt-get clean
rm -rf /tmp/*
rm -f /etc/hosts /etc/resolv.conf
umount /proc/
umount /sys/

# sudo mv /etc/resolv.conf.original /etc/resolv.conf
cd /etc/
ln -s ../run/systemd/resolve/stub-resolv.conf resolv.conf

exit
```

### 8. Set up the .iso
```bash
# fix manifest files
chmod +w /tmp/rootfs/cd/casper/filesystem.manifest
sudo chroot /tmp/rootfs/custom dpkg-query -W --showformat='${Package} ${Version}\n' > /tmp/rootfs/cd/casper/filesystem.manifest
sudo cp /tmp/rootfs/cd/casper/filesystem.manifest /tmp/rootfs/cd/casper/filesystem.manifest-desktop

# regenerate the squashfs file
sudo mksquashfs /tmp/rootfs/custom /tmp/rootfs/cd/casper/filesystem.squashfs

# update md5 sums
cd /tmp/rootfs
sudo rm /tmp/rootfs/cd/md5sum.txt
sudo bash -c 'cd /tmp/rootfs/cd && find . -type f -exec md5sum {} +' > md5sum.txt
sudo mv md5sum.txt /tmp/rootfs/cd
```

### 9. Create the .iso
Now we need to use the original `.iso` to extract the MBR and the EFI partition. 
The location and size of the latter can be found using `fdisk -l /tmp/$IMAGE_NAME.iso` in the second line 
of the partitions list:
```bash
cd /tmp/rootfs/cd

sudo fdisk -l /tmp/$IMAGE_NAME.iso
# ...
# Device                                   Start     End Sectors  Size Type
# /tmp/ubuntu-22.04.3-desktop-amd64.iso1      64 9828451 9828388  4,7G Microsoft basic data
# /tmp/ubuntu-22.04.3-desktop-amd64.iso2 9828452 9838519   10068  4,9M EFI System
# /tmp/ubuntu-22.04.3-desktop-amd64.iso3 9838520 9839119     600  300K Microsoft basic data

# extract the MBR template for --grub2-mbr
# we only need the x86 code. All partition stuff will be newly created.
dd if=/tmp/$IMAGE_NAME.iso bs=1 count=432 of=/tmp/boot_hybrid.img

# the EFI partition is not a data file inside the ISO any more.
# so extract the EFI partition image image for -append_partition
dd if=/tmp/$IMAGE_NAME.iso bs=512 skip=9828452 count=10068 of=/tmp/efi.img

# create .iso
sudo xorriso -as mkisofs -r \
    -V 'Ubuntu 22.04 Forensics Live' \
    -o /tmp/$IMAGE_NAME-live-forensics-custom.iso \
    --grub2-mbr /tmp/boot_hybrid.img \
    -partition_cyl_align off \
    -partition_offset 16 \
    --mbr-force-bootable \
    -append_partition 2 28732ac11ff8d211ba4b00a0c93ec93b /tmp/efi.img \
    -appended_part_as_gpt \
    -iso_mbr_part_type a2a0d0ebe5b9334487c068b6b72699c7 \
    -c '/boot.catalog' \
    -b '/boot/grub/i386-pc/eltorito.img' \
    -no-emul-boot -boot-load-size 4 -boot-info-table --grub2-boot-info \
    -eltorito-alt-boot \
    -e '--interval:appended_partition_2:::' \
    -no-emul-boot \
    -boot-load-size 10068 \
    .

# change the file's mode
sudo chmod 0755 /tmp/$IMAGE_NAME-live-forensics-custom.iso
```

### References
1. [StackOverflow: Creating your own Custom Live CD - the manual way](https://askubuntu.com/a/49679)
1. [StackOverflow:Ubuntu 22.04 build ISO (Both: MBR and EFI )](https://askubuntu.com/a/1403669)
1. [Disable disks automounting](https://unix.stackexchange.com/questions/333721/how-to-stop-auto-mounting-of-devices-in-ubuntu)
1. [Community Help Wiki: LiveCDCustomizationFromScratch](https://help.ubuntu.com/community/LiveCDCustomizationFromScratch)
1. [Customizing the Ubuntu Live CD: Adding Packages and Making Changes](https://devicetests.com/customizing-ubuntu-live-cd-adding-packages-and-making-changes)
1. [Ubuntu livecd customization (long story)](https://sysdl132.github.io/blogcc/2021/03/29/livecd.html)



## II. Kali Linux
**N.B.** The following tested on `Kali Linux 2024.4` host environment at 27.02.2025 22:45 SAMT.

The best way to set up your host environment for customization is to use the same OS distro and version 
and update the host.

##### Update the host environment
Uncomment additional sources:
```bash
sudo nano /etc/apt/sources.list

# See https://www.kali.org/docs/general-use/kali-linux-sources-list-repositories/
deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware

# Additional line for source packages
deb-src http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware
```
Update the host system:
```bash
sudo apt update
sudo apt upgrade
sudo reboot
```

##### Install the dependencies and download the buidl script
```bash
mkdir ~/tmp && cd ~/tmp
sudo apt update
sudo apt install -y git live-build simple-cdd cdebootstrap curl devscripts
git clone https://gitlab.com/kalilinux/build-scripts/live-build-config.git
```

##### Add meta-package `kali-tools-forensics` to the liveCD build config
```bash
cd live-build-config/
nano kali-config/variant-default/package-lists/kali.list.chroot
...
#kali-tools-top10
kali-linux-default
kali-tools-forensics
```

##### Start building
**N.B.**: change different version if required (or skip this setting altogether).
```bash
time ./build.sh
mkdir: created directory './images/'

***
GENERATED KALI IMAGE: ~/tmp/live-build-config/images/kali-linux-rolling-live-amd64.iso
***

real    2690.69s
user    0.22s
sys     0.09s
cpu     0%
```

##### Grab your (hopefully correctly built image) at
`~/tmp/live-build-config/images/kali-linux-rolling-live-amd64.iso`


### References
1. [Building Custom Kali ISOs](https://www.kali.org/docs/development/dojo-mastering-live-build/)
1. [Creating A Custom Kali ISO](https://www.kali.org/docs/development/live-build-a-custom-kali-iso/)
3. [kali-tools-forensics meta-package](https://www.kali.org/tools/kali-meta/#kali-tools-forensics)



## 3. Windows
**N.B.** The following was checked with `Win10_22H2_Russian_x64` image on 20.11.2023 02:15 SAMT.
**N.B.** These instructions will only created a **modified installer iso image**. To create a bootable Win10 
USB image one needs to use this image and install 

Follow the instructions in [this manual](https://www.youtube.com/watch?v=-tIO4B8q8sk).
Before syspreping install `AccessData_FTK_Imager_4.7.1.exe`.

### References
1. [Create Custom Windows 10 Image With Applications Pre-installed](https://www.youtube.com/watch?v=-tIO4B8q8sk)
1. [Hiren's BootCD PE Logo](https://www.hirensbootcd.org/download/)
1. [AnyBurn](https://www.anyburn.com/download.php)
1. [How to create a custom ISO for Windows 10](https://www.techtarget.com/searchenterprisedesktop/tip/How-to-create-a-custom-ISO-for-Windows-10)
