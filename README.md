# rpi3-ubuntu-aarch64          [English](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-17.04-arm64/README-EN.md)

### [64位centos戳这里](https://github.com/chainsx/centos64-rpi)

# 经测试，性能最高提高60倍!!!

## 拒绝伸手党，如果你给我反馈意见及bug的话，我会感激不尽。

## 前言：

ubuntu官方居然不给RaspberrPi3出官方镜像（官方推荐的镜像是Electron752移植的。。。。），太不厚道了。（但据说是因为16.04何rpi3发布时间隔的太近了）

## 声明：

* 本系统由我（chainsx）自行构建的根目录以及boot。

* 本系统为最简化ubuntu，如需桌面请自行安装。

* 如需定制版以及商业用途，请务必与本人联系。

* 本系统使用的内核（kernel）为最简版，不支持xfs/f2fs等文件系统，如需请自行编译。

* 可以转载，推广甚至修改本系统，但必须注明出处。

…………

## 使用说明：

* 因为是64位系统，所以你可以开启32位支持,开启方法：

```
sudo dpkg --add-architecture armhf   #开启armhf支持
sudo apt-get update
sudo apt-get install libc6:armhf
sudo dpkg --add-architechture armel  #开启armel支持
sudo apt-get update
sudo apt-get install libc6-armhf
```

## 关于:

* 本系统是直接基于ubuntu-Base-17.04-arm64构建的根目录，非移植版，所以稳定性有提升，但是整个系统不够完善。
* 现在的开机时间不到10秒，超过了官方raspbian lite,吊打同类的pi64(国外人士移植的debian arm64)，相信我们中国人的实力！！！
* 现在的开机时间（从执行reboot到ssh连上）不到10秒，超过了官方raspbian lite，更超过了同类的pi64
* 本系统由以下组成
**firmware** ：由树莓派基金会官方提供的linux-rpi-4.9.y编译的aarch64内核
**rootfs** ：ubuntu-Base-arm64(根目录构建)
* `apt`的源默认为清华软件源
* 默认用户：`ubuntu`      密码：`ubuntu`
* 默认开启ssh，不想要的自己去关
* 默认为命令行，想要图形界面的自己装
* 第一次开机时不会拓展rootfs分区，意思是你需要自己拓展，用fdisk或gparted来拓展吧。
* 关于ext4的扩容方法，在[这里](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-17.04-arm64/Documentation/expand-file-system.md)，f2fs扩容有点复杂，暂不解释。

## 项目求助：

现在急求大神帮忙一起完善此系统，有意者请联系我

|  联系方式   |           |
|-----------|------------|
|QQ|1396219808(CX_rootfs)|
|E-mail|chainsx@outlook.com i@chainsx.cn|

**********************

## 下载地址：

### 腾讯云(tencent cloud)

#### （如遇公网流量达到上限而不可下载时请使用百度网盘）

#### 注意：公网流量有限，请不要使用例如迅雷，快车，电驴，ADM，aria2等下载工具下载，请使用浏览器内建下载/wget等非分块下载的工具下载，感谢你的支持。

|使用EXT4文件系统| [华南地区](http://chainsx-1253770712.coscd.myqcloud.com/ubuntu-17.04-arm64-ext4-RaspberryPi3.img.xz) | [其他地区(使用cdn)](http://chainsx-1253770712.file.myqcloud.com/ubuntu-17.04-arm64-ext4-RaspberryPi3.img.xz) |
|-------|--------|-------|
|使用F2FS文件系统（不稳定，仅测试用）| [华南地区](http://chainsx-1253770712.coscd.myqcloud.com/ubuntu-17.04-arm64-f2fs-RaspberryPi3.img.xz) | [其他地区(使用cdn)](http://chainsx-1253770712.file.myqcloud.com/ubuntu-17.04-arm64-f2fs-RaspberryPi3.img.xz) |

### 百度网盘(Baidu Netdisk)

|使用EXT4文件系统|[链接](https://pan.baidu.com/s/1c2325k0)|
|------|--------|
|使用F2FS文件系统（不稳定，仅测试用）|[链接](https://pan.baidu.com/s/1skDBpq1)|
