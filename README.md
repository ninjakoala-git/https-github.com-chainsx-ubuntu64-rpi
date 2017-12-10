# rpi3-ubuntu-aarch64

A project of ubuntu aarch64 for Raspberrypi3

## 前言：

ubuntu官方居然不给RaspberrPi3出官方镜像（官方推荐的镜像是Electron752移植的。。。。），太不厚道了。（但据说是因为16.04何rpi3发布时间隔的太近了）

那现在17.04都出来了你还有什么理由解释呢(17.04优先适配pi2，pi3现在还没消息。。你可以出门左转找到对于pi3的17.04的版本https://github.com/chainsx/ubuntu-17.04-for-RaspberryPi3

在此呢，感谢bamarni提供的思路，他也有一个64位树莓派系统的项目debian arm64，项目地址https://github.com/bamarni/pi64

## 内置：

* 集成了基于树莓派基金会的`raspi-config`
使用命令: `raspi-config`

* 添加了`chainsx-config`
使用命令: `chainsx-config`

## 关于:

* 本系统由以下组成

firmware：由树莓派基金会官方提供的linux-rpi-4.9.y编译的aarch64内核

rootfs：ubuntu 16.04.3 arm64

* `apt`的源默认为cn.ports.ubuntu.com

* 默认用户：ubuntu      密码：ubuntu       root用户密码：root      

* 默认开启ssh，不想要的自己去关

* 默认为命令行，想要图形界面的自己装（当然，我在想装一个unity，官方说不行，的却在armhf上会只显示一个空白桌面，是因为没有硬件加速）

* 第一次开机时不会拓展rootfs分区，意思是你需要自己拓展，用fdisk或gparted来拓展吧。

* 下载，在百度云上下载，github下载速度慢，百度云可以更慢（无力吐槽了）。。。。。。。。。

* 还有什么的，，，联系我吧，毕竟我能力有限，有能力有精力有时间的可以帮忙一起完善这个项目。

QQ:1396219808(CX_rootfs)

E-mail:chainsx@outlook.com    i@chainsx.cn

## 下载地址：

