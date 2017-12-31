# rpi3-ubuntu-aarch64          [English](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-17.04-arm64/README-EN.md)

### [64位centos戳这里](https://github.com/chainsx/centos64-rpi)




## 前言：

ubuntu官方居然不给RaspberrPi3出官方镜像（官方推荐的镜像是Electron752移植的。。。。），太不厚道了。（但据说是因为16.04何rpi3发布时间隔的太近了）


在此呢，感谢bamarni提供的思路，他也有一个64位树莓派系统的项目debian arm64，项目地址https://github.com/bamarni/pi64

## 使用说明：

* 因为是64位系统，所以你可以开启32位支持,开启方法：

`sudo dpkg --add-architecture armhf`

`sudo apt-get update`

`sudo apt-get install libc6:armhf`

## 关于:

* 本系统是直接基于ubuntu-Base-17.04-arm64构建的根目录，非移植版，所以稳定性有提升，但是整个系统不够完善。


* 现在的开机时间不到10秒，超过了官方raspbian lite

* 现在的开机时间（从执行reboot到ssh连上）不到10秒，超过了官方raspbian lite，更超过了同类的pi64


* 本系统由以下组成

firmware：由树莓派基金会官方提供的linux-rpi-4.9.y编译的aarch64内核

rootfs：ubuntu-Base-arm64(根目录构建)

* `apt`的源默认为清华软件源


* 默认用户：ubuntu      密码：ubuntu          

* 默认用户：ubuntu      密码：ubuntu       root用户密码：root      


* 默认开启ssh，不想要的自己去关

* 默认为命令行，想要图形界面的自己装

* 关于unity，官方说armhf不能显示桌面是因为没有硬件加速。

* 关于vnc，在arm64上安装unity后可以用vnc连上并显示桌面，实际情况我没有试过。

(安装unity命令：

`sudo apt-get install --no-install-recommends ubuntu-desktop gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal`

使用vnc时要替换掉xstartup，命令：

`cd .ssh && wget https://github.com/chainsx/ubuntu64-rpi/raw/ubuntu-17.04-arm64/vnc/xstartup`)

* 第一次开机时不会拓展rootfs分区，意思是你需要自己拓展，用fdisk或gparted来拓展吧。

* 还有什么的，，，联系我吧，毕竟我能力有限，有能力有精力有时间的可以帮忙一起完善这个项目。

QQ:1396219808(CX_rootfs)

E-mail:chainsx@outlook.com    i@chainsx.cn

**********************

## 下载地址：


百度云链接:https://pan.baidu.com/s/1nvoWsNB 密码:v54r

yandex.disk:https://yadi.sk/d/ysdTPoeF3R7LCU

mega网盘:https://mega.nz/#!wqwUgSrY!5a-0gcJecn9X94_Ahr6g4OBISl7CbFNk_ZJXkKvIHr4

sandisk cloud:https://sandisk.upthere.com/loop/c0fe40d8a0919986d822e8754e0c5553c3049b6ba244f9ee3d0edcdbeecb3a1c
