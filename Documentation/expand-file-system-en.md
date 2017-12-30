# Manually resizing the SD card on Raspberry Pi

You can also resize the partitions of the SD card that your Pi is running on.

First you need to change the partition table with fdisk. You need to remove the existing partition entries and then create a single new partition than takes the whole free space of the disk. This will only change the partition table, not the partitions data on disk. The start of the new partition needs to be aligned with the old partition!

Start fdisk:

sudo fdisk /dev/mmcblk0 

Then delete partitions with d and create a new with n. You can view the existing table with p.

* p to see the current start of the main partition
* d, 3 to delete the swap partition
* d, 2 to delete the main partitionn
* p 2 to create a new primary partition, next you need to enter the start of the old main partition and then the size (enter for complete SD card). The main partition on the Debian image from 2012-04-19 starts at 157696, but the start of your partition might be different. Check the p output!
* w write the new partition table

Now you need to reboot:

sudo shutdown -r now 

After the reboot you need to resize the filesystem on the partition. The resize2fs command will resize your filesystem to the new size from the changed partition table.

sudo resize2fs /dev/mmcblk0p2 

This will take a few minutes, depending on the size and speed of your SD card.

When it is done, you can check the new size with:

df -h
