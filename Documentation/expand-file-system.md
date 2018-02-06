## 树莓派手动扩容

### 我觉得这篇文章会在下一次更新时作废，因为我在解决自动扩容的问题。

# 如果你觉得中文看起来困难，你可以看[英语](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-17.04-arm64/Documentation/expand-file-system-en.md)


步骤1: 重新启动你的树莓派，用ssh登陆

步骤2: $ sudo fdisk /dev/mmcblk0 

* 命令：按p（印刷） 你应该会看到两个分区，现在把分区2的信息写下来（/dev/mmcblk0p2）。 

* 命令：按d（删除分区2） 

* 命令：按p（印刷） 现在应该会看到2个分区 

* 命令：按n（加分区） 

* 选择p (主要) 分区2

* 选择2 第一空格输入原来分区2的开始位置 最后的空格输入默认值 

* 命令：按p（印刷） 你应该会看到分区2填满所有空间 

* 命令：按w（保存） 

步驟3: $sudo reboot 

重新启动后，使用resize2fs来修复分区2 

步驟4: $ sudo resize2fs /dev/mmcblk0p2 等待约2-3分钟 
