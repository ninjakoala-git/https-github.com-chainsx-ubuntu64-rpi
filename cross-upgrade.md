其实你可以直接执行`do-release-updrade -d`就行了

以下是复制的官方的说明

Cross-upgrading 14.04 to 16.04

You can upgrade an old unofficial 14.04 installation to the official 16.04 installation, though it takes a number of additional steps.

Note that Ubuntu's setup uses u-boot as an intermediary bootloader, which is different from the previous system of the RPI2 booting the kernel directly. This will be reflected in the upgrade procedure.

 Once you begin this procedure, if you reboot the installation without completing the entire upgrade procedure, you will be left with an unbootable system. 

First, remove a number of PPA packages which are obsoleted / incompatible with the 16.04.

`apt-get --purge remove rpi2-ubuntu-errata raspberrypi-bootloader-nokernel \ linux-image-rpi2 flash-kernel`

Back up and remove the apt PPA configuration and module blacklists (the latter will be provided directly by the 4.4.0 kernel package).

`mkdir -p /root/xenial-upgrade tar zcvf /root/xenial-upgrade/etc.tar.gz \ /etc/modprobe.d/rpi2.conf \ /lib/modules-load.d/rpi2.conf \ /etc/apt/preferences.d/rpi2-ppa \ /etc/apt/sources.list.d/fo0bar-rpi2* \ /etc/apt/trusted.gpg.d/fo0bar-rpi2* rm -f \ /etc/modprobe.d/rpi2.conf \ /lib/modules-load.d/rpi2.conf \ /etc/apt/preferences.d/rpi2-ppa \ /etc/apt/sources.list.d/fo0bar-rpi2* \ /etc/apt/trusted.gpg.d/fo0bar-rpi2*`

Back up and remove the contents of /boot/firmware, which will be recreated.

`tar zcvf /root/xenial-upgrade/firmware.tar.gz /boot/firmware/* rm -rf /boot/firmware/*`

Update apt sources without the old PPA configuration.

`apt-get update`

Run do-release-upgrade as normal. When asked to reboot at the end, do not, and select "n" instead.

`do-release-upgrade -d` # -d will be unneeded once 16.04.1 is released

Install new firmware, u-boot and 4.4.0 kernel metapackages.

`apt-get install u-boot-rpi u-boot-tools linux-raspi2 linux-firmware-raspi2 \ linux-firmware flash-kernel`

Install the RPI2 DT-compatible u-boot image.

`apt-get install binutils` # for "strings" 

`wget -O /tmp/mkknlimg https://raw.githubusercontent.com/raspberrypi/linux/rpi-4.4.y/scripts/mkknlimg`

`chmod 0755 /tmp/mkknlimg` 

`/tmp/mkknlimg --dtok /usr/lib/u-boot/rpi_2/u-boot.bin /boot/firmware/uboot.bin`

Install basic config.txt and cmdline.txt configurations. If your root device is not on the second SD partition (uncommon) or you have a more advanced configuration, recreate them here.

`cat <<"EOM" >/boot/firmware/config.txt kernel=uboot.bin dtparam=i2c_arm=on dtparam=spi=on EOM cat <<"EOM" >/boot/firmware/cmdline.txt net.ifnames=0 dwc_otg.lpm_enable=0 console=ttyAMA0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait EOM`

Update the initrd and re-flash the kernel configuration.

`update-initramfs -u flash-kernel`

Reboot!

`reboot`

Optionally add ppa:ubuntu-raspi2/ppa as described above.

