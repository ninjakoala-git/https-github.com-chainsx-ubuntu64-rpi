# RaspberryPi3-ubuntu-16.04-aarch64          [English](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-16.04-arm64/README-EN.md)
### [64位centos戳这里](https://github.com/chainsx/centos64-rpi)
# 经测试，性能最高提高60倍!!!

****************

## 前言：
#### ubuntu官方居然不给RaspberrPi3出官方镜像（官方推荐的镜像是Electron752移植的。。。。），太不厚道了。（但据说是因为16.04何rpi3发布时间隔的太近了）

## 声明：
* 本系统由我（chainsx）自行构建的根目录以及boot。
* 本系统为最简化ubuntu，如需桌面请自行安装。
* 如需定制版以及商业用途，请**务必**与本人联系。
* 基于ext4文件系统的ubuntu使用的内核（kernel）为**最简版**，不支持xfs/f2fs等文件系统，也不支持wifi和蓝牙，如需请**自行**编译。
* 基于f2fs文件系统的ubuntu使用的是pi64的内核，支持wifi，蓝牙，xfs/f2fs等文件系统。
* 可以转载，推广甚至修改本系统，但**必须注明出处**。
* 你可以基于本系统打造更加完善的系统，但**必须注明出处**。
#### …………

## 使用说明：

* 因为是64位系统，所以你可以开启32位支持,开启方法：

```
root@ubuntu:~# dpkg --add-architecture armhf   #开启armhf支持
root@ubuntu:~# apt-get update
root@ubuntu:~# apt-get install libc6:armhf
root@ubuntu:~# dpkg --add-architechture armel  #开启armel支持
root@ubuntu:~# apt-get update
root@ubuntu:~# apt-get install libc6-armhf
```

* 为不同的架构指定不同的源，你需要编辑`/etc/apt/sources.list`

```
deb [arch=armel] http://cn.ports.ubuntu.com/ubuntu-ports quantal main universe   #ubuntu官方中国源
deb [arch=armhf] http://ftp.cn.debian.org/ubuntu-ports quantal main universe    #科大源
deb [arch=arm64] http://ftp2.cn.debian.org/ubuntu-ports quantal main universe    #清华源
```

#### [官方帮助文档MultiArch](https://wiki.debian.org/Multiarch/HOWTO)

* 添加树莓派官方软件源镜像（安装树莓派官方提供的特有软件包）

```
root@ubuntu:~# apt-get update
root@ubuntu:~# apt-get install debian-keyring
root@ubuntu:~# echo "deb [arch=armhf] http://mirrors.ustc.edu.cn/archive.raspberrypi.org main ui untested staging" >> /etc/apt/sources.list
root@ubuntu:~# echo "deb [arch=armhf] http://mirrors.ustc.edu.cn/raspbian/raspbian main contrib firmware non-free rpi" >> /etc/apt/sources.list
```

* 添加swap分区

```
root@ubuntu:~# dd if=/dev/zero of=/swapfile bs=2048 count=1M     #创建一个大小为2G的文件
root@ubuntu:~# mkswap /swapfile     #把这个文件变成swap文件
root@ubuntu:~# swapon /swapfile     #启用这个swap文件
#编辑/etc/fstab文件，使在每次开机时自动加载swap文件：
/swapfile swap swap default 0 0
```
********

## 关于:

* 本系统是直接基于ubuntu-Base-16.04-arm64构建的根目录， **非移植版** ，所以稳定性有提升，但是整个系统不够完善。
* 现在的开机时间不到10秒，超过了官方raspbian lite,吊打同类的pi64(国外人士移植的debian arm64)，相信我们中国人的实力！！！
* 现在的开机时间（从执行reboot到ssh连上）不到10秒，超过了官方raspbian lite，更超过了同类的pi64
* 本系统由以下组成
#### **firmware** ：由树莓派基金会官方提供的linux-rpi-4.9.y编译的aarch64内核
#### **rootfs** ：ubuntu-Base-arm64(根目录构建)
* `apt`的源默认为清华软件源
* 默认用户：`ubuntu`      密码：`ubuntu`
* 默认开启ssh，不想要的自己去关
* 默认为命令行，想要图形界面的自己装
* 第一次开机时不会拓展rootfs分区，意思是**需要你自己拓展**，用fdisk或gparted来拓展吧。
* 关于ext4的扩容方法，在[这里](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-17.04-arm64/Documentation/expand-file-system.md)，f2fs扩容有点复杂，暂不解释。


|  联系方式   |           |
|-----------|------------|
|QQ|1396219808(CX_rootfs)|
|E-mail|chainsx@outlook.com i@chainsx.cn|

**********************

## 下载地址：

### 腾讯云(tencent cloud)
##### （如遇公网流量达到上限而不可下载时请使用百度网盘）
##### 注意：公网流量有限，请不要使用例如迅雷，快车，电驴，ADM，aria2等下载工具下载，请使用浏览器内建下载/wget等非分块下载的工具下载，感谢你的支持。
### 发现有人恶意下载耗费大量公网流量，现暂时关闭腾讯云下载方式。

|文件系统 | 普通下载 |cdn下载 |
|-----|------|---------|
|使用EXT4文件系统|  |  |
|使用F2FS文件系统（不稳定，仅测试用）|  | |

### 百度网盘(Baidu Netdisk)

|文件系统 | 下载链接 |
|--------|--------|
|使用EXT4文件系统| [链接](https://pan.baidu.com/s/1qY9OpWC) |
|使用F2FS文件系统（不稳定，仅测试用）| |

## 经测试的稳定版还未发布，请加群获取更多信息。

# 欢迎加入树莓派64位系统交流群，QQ群号码：697381661
