# RaspberryPi3-ubuntu-16.04-aarch64          [English](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-16.04-arm64/README-EN.md)
***************
###### 插播一段广告。。。。。
### ubuntu-18.04-arm64预览版，[项目分支](https://github.com/chainsx/ubuntu64-rpi/tree/ubuntu-bonic(18.04)-preview)

### [64位centos戳这里](https://github.com/chainsx/centos64-rpi)
***************

# 经测试，ubuntu-arm64的性能最高提高60倍!!!

****************

## 前言：
#### ubuntu官方居然不给RaspberrPi3出官方镜像（官方推荐的镜像是Electron752移植的，对，移植版，ubuntu官方不会直接给支持的），太不厚道了。（但据说是因为16.04何rpi3发布时间隔的太近了）

## 声明：
* 本系统由我（chainsx）自行构建的根目录以及boot。
* 注意，是自行构建的系统，而非移植系统！！！
* 如需定制版以及商业用途，请**务必**与本人联系。
* 可以转载，推广甚至修改本系统，但**必须注明出处**。
* 你可以基于本系统打造更加完善的系统，但**必须注明出处**。
#### …………

## 一些拓展功能（没必要的话就别用）：

|功能名称  |  方法|
|------|-------|
|64位系统开启32位支持   |   [帮助文档](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-16.04.3-arm64/Documentation/32-bit-support.md)|
|为不同的架构指定不同的源   |   [帮助文档](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-16.04.3-arm64/Documentation/multi-arch.md)|
|添加树莓派官方软件源镜像安装树莓派官方提供的特有的软件包   |   [帮助文档](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-16.04.3-arm64/Documentation/multi-arch.md)|
|添加swap分区以增加性能   |   [帮助文档](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-16.04.3-arm64/Documentation/multi-arch.md)|

## 关于:

* 本系统是直接基于ubuntu-Base-16.04-arm64构建的根目录， **非移植版** ，所以稳定性有提升，但是整个系统不够完善。
* 现在的开机时间不到10秒，超过了官方raspbian lite,吊打同类的pi64(国外人士移植的debian arm64)。
* 本系统由以下组成
#### **firmware** ：由树莓派基金会官方提供的linux-rpi-4.11.y编译的aarch64内核
#### **rootfs** ：ubuntu-Base-arm64(根目录构建)

## 使用说明

* `apt`的源默认为清华软件源
* 默认用户：`ubuntu`      密码：`ubuntu`
* 支持蓝牙和wifi，wifi配置方法[在这里](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-16.04.3-arm64/Documentation/wifi-config.md)。
* 如果你需要安装桌面的话，[看这里](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-16.04.3-arm64/Documentation/install-desktop.md)
* 默认开启ssh，不想要的自己去关。
* 第一次开机时不会拓展rootfs分区，意思是**需要你自己拓展**，用fdisk或gparted来拓展吧，用fdisk拓展方法如下。
* 关于ext4的扩容方法，在[这里](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-17.04-arm64/Documentation/expand-file-system.md)。


|  联系方式   |           |
|-----------|------------|
|QQ|1396219808(CX_rootfs)|
|E-mail|chainsx@outlook.com i@chainsx.cn|

**********************

## 下载地址：

### 百度网盘(Baidu Netdisk)

| 版本 | 下载链接 |
|--------|--------|
| ubuntu-16.04-arm64-stable-with-blutooth-and-wifi(稳定版带蓝牙和wifi，使用方法在上面。) | [链接](https://pan.baidu.com/s/1snt6ByX) |
##### 如果百度云限速的问题你无法解决的话（至少是要下载1h以上的话），请联系我，我会给你提供腾讯云计算对象储存内容分发式网络高速下载通道的。


# 欢迎加入树莓派64位系统交流群，QQ群号码：697381661
