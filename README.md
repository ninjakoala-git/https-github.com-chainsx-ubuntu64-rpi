# rpi3-ubuntu-aarch64
A project of ubuntu aarch64 for Raspberrypi3

## 前言：

ubuntu官方居然不给RaspberrPi3出官方镜像（官方推荐的镜像是Electron752移植的。。。。），太不厚道了。（但据说是因为16.04何rpi3发布时间隔的太近了）

那现在17.04都出来了你还有什么理由解释呢(17.04优先适配pi2，pi3现在还没消息。。你可以在这里找到对于pi3的17.04的版本https://github.com/chainsx/ubuntu-17.04-for-RaspberryPi3)。。。。。。。。。

基于一篇贴子的开导，，，，我成功的移植了ubuntu 15.10 aarch64到rpi3上（虽然不是长期支持版，而且现在已经停止支持了，Debian有一个健壮的arm64移植版，但ubuntu不一样，所以我找了很久,现在考虑交叉升级到17.04）

在此呢，感谢bamarni提供的思路，嗯，他本人也移植了一个debian arm64，项目地址https://github.com/bamarni/pi64

我以前就是搞Android Recovery移植的，后来搞坏了。。。。。(无力吐槽)没得搞的了，就玩树莓派了。。。。。。。

## 关于:

* 本系统三个部分由以下组成

boot:由ubuntu 16.04 armhf for rpi2（官方镜像）移植

firmware：由树莓派基金会官方提供的linux-rpi-4.9.y编译的aarch64内核

rootfs：ubuntu 15.10 arm64 for powerpc

* 当然了，这个系统肯定不稳定（废话，当然知道），如开机时会连接某个被墙的服务器，会等很久，目前还未解决。

* 前面想移植centos arm64 的，但是始终没解决EFI分区挂载不了和rootfs分区readonly的问题，但目前此系统基本上没什么太大的问题。

* `apt`的源默认为cn.ports.ubuntu.com（科大源太坑了）

* 默认用户：ubuntu      密码：ubuntu       root用户密码：root      (这里不得不多说两句，我大多数时间都卡在这里，下载的rootfs镜像又不告诉我默认用户名密码。。。。`cat /etc/shadow` 后知道默认用户为ubuntu,按照官方的说法ubuntu的默认密码要么为空，要么为ubuntu，但两者都不对，哼哼，华军你改过的吧。。幸好有`chroot`这么个命令，我用raspbian执行chroot之后才把密码改了，才登陆了上去)

* 默认开启ssh，不想要的自己去关

* 默认为命令行，想要图形界面的自己装（当然，我在想装一个unity，官方说不行，的却在armhf上会只显示一个空白桌面，但arm64呢？我试试）

* 第一次开机时不会拓展rootfs分区，意思是你需要自己拓展，用fdisk或gparted来拓展吧。

* 移植好后我只安装了一个软件，那就是screenfetch，找成就感的，，，，屡屡失败，都没信心了，随便更新了一下软件源

* 下载，在百度云上下载，github下载速度慢，百度云可以更慢（无力吐槽了）。。。。。。。。。

* 还有什么的，，，联系我吧，毕竟我能力有限，有能力有精力有时间的可以帮忙一起完善这个项目。

QQ:1396219808(CX_rootfs)

E-mail:chainsx@outlook.com(不常用)    1396219808@qq.com(我登qq时就会接受电子信件了)

## 声明：

这里只提供学术交流，所以，转载请注明。。。。。。。。。。。。。

不得用于商业用途（我都不知道可以怎么作为商业用途。。。。。。。）

## 链接：

啰嗦了一大堆，最后，附上百度云链接http://pan.baidu.com/s/1bp8NnvL
