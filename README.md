# rpi3-ubuntu-aarch64

## 为了不辜负大家的star，我将尽快补充内容

A project of ubuntu aarch64 for Raspberrypi3

## 前言：

ubuntu官方居然不给RaspberrPi3出官方镜像（官方推荐的镜像是Electron752移植的。。。。），太不厚道了。（但据说是因为16.04何rpi3发布时间隔的太近了）

那现在17.04都出来了你还有什么理由解释呢(17.04优先适配pi2，pi3现在还没消息。。你可以出门左转找到对于pi3的17.04的版本https://github.com/chainsx/ubuntu-17.04-for-RaspberryPi3

基于一篇贴子的开导，，，，我成功的移植了ubuntu 15.10 aarch64到rpi3上（虽然不是长期支持版，而且现在已经停止支持了，Debian有一个健壮的arm64移植版，但ubuntu不一样）

在此呢，感谢bamarni提供的思路，他本人也有一个64位树莓派系统的项目debian arm64，项目地址https://github.com/bamarni/pi64

## 关于:

* 本系统三个部分由以下组成

boot:由ubuntu 16.04 armhf for rpi2（官方镜像）提取

firmware：由树莓派基金会官方提供的linux-rpi-4.9.y编译的aarch64内核

rootfs：ubuntu 15.10 arm64（你可以交叉升级到16.04，因为有人问什么是交叉升级，[点击这里](https://github.com/chainsx/ubuntu64-rpi/edit/master/cross-upgrade.md)）

* 当然了，这个系统肯定不稳定（废话，当然知道），如开机时会连接某个地址，会等很久，目前还未解决。

* `apt`的源默认为cn.ports.ubuntu.com

* 默认用户：ubuntu      密码：ubuntu       root用户密码：root      

* 默认开启ssh，不想要的自己去关

* 默认为命令行，想要图形界面的自己装（当然，我在想装一个unity，官方说不行，的却在armhf上会只显示一个空白桌面，是因为没有硬件加速）

* 第一次开机时不会拓展rootfs分区，意思是你需要自己拓展，用fdisk或gparted来拓展吧。

* 移植好后我只安装了一个软件，那就是screenfetch，找成就感的，，，，屡屡失败，都没信心了，随便更新了一下软件源

* 下载，在百度云上下载，github下载速度慢，百度云可以更慢（无力吐槽了）。。。。。。。。。

* 还有什么的，，，联系我吧，毕竟我能力有限，有能力有精力有时间的可以帮忙一起完善这个项目。

QQ:1396219808(CX_rootfs)

E-mail:chainsx@outlook.com    1396219808@qq.com

## 链接：

啰嗦了一大堆，最后，附上百度云链接http://pan.baidu.com/s/1bp8NnvL(没打包的)

打包了的:https://pan.baidu.com/s/1mi7PE1E

### 重要 重要 重要
请自行将源换成www.opencas.org/mirrors
不然apt无法使用
