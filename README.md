# RaspberryPi3-ubuntu-16.04-aarch64          [English](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-16.04-arm64/README-EN.md)
***************
###### 插播一段广告。。。。。
### ubuntu-18.04-arm64预览版，[项目分支](https://github.com/chainsx/ubuntu64-rpi/tree/ubuntu-bonic(18.04)-preview)

### [64位centos戳这里(尚未完成，仅供测试用)](https://github.com/chainsx/centos64-rpi)
### [64位debian(非pi64,此版本可以吊打pi64)](https://github.com/UMRnInside/RPi-arm64)
***************

# 经测试，ubuntu-arm64的性能最高提高60倍!!!

****************
![example1](https://github.com/chainsx/ubuntu64-rpi/raw/ubuntu-16.04.3-arm64/imagine/321.jpg "example1")

## 前言：
#### ubuntu官方居然不给RaspberrPi3出官方镜像（官方推荐的镜像是Electron752移植的，对，移植版，ubuntu官方不会直接给支持的），而rpi2都有16.04/17.04/17.10的官方镜像……

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
|添加树莓派官方软件源镜像安装树莓派官方提供的特有的软件包   |   [帮助文档](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-16.04.3-arm64/Documentation/offical-support.md)|
|添加swap分区以增加性能   |   [帮助文档](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-16.04.3-arm64/Documentation/add-swap.md)|
|安装preload以加快开机速度 |   [帮助文档](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-16.04.3-arm64/Documentation/preload.md)

## 关于:

* 本系统是直接基于ubuntu-Base-16.04-arm64构建的根目录， **非移植版** ，所以稳定性有提升，但是整个系统不够完善。
* ubuntu官方为bcm2837给了支持的，只不过是以raspi2命名，原因是晚期的raspi2是使用的bcm2837芯片。
* 本系统为了支持ubuntu为bcm2837的支持高度锲合ubuntu官方系统，包括挂载点，label等。
* 现在的开机时间不到10秒，超过了官方raspbian lite,吊打同类的pi64(国外人士移植的debian arm64)。
* 本系统由以下组成
#### **firmware** ：由树莓派基金会官方提供的linux-rpi-4.11.y编译的aarch64内核
#### **rootfs** ：ubuntu-Base-arm64(根目录构建)

## 使用说明

* `apt`的源默认为清华软件源
* 默认用户：`ubuntu`      密码：`ubuntu`
* 支持wifi，wifi配置方法[在这里](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-16.04.3-arm64/Documentation/wifi-config.md)。
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
| ubuntu-16.04-arm64-stable-with-wifi(稳定版带wifi，使用方法在上面。) | [链接](https://pan.baidu.com/s/1snt6ByX) |
| ubuntu-16.04-arm64-nightly-with-wifi-auto-expand-rootfs(Night开发版) | [链接]() |
#### 关于Night版，是没有经过测试的，很多东西都可能会出问题，甚至不能开机，仅大家测试后反馈bug和意见用。
##### 如果百度云限速的问题你无法解决的话（至少是要下载1h以上的话），请联系我，我会给你提供腾讯云计算对象储存内容分发式网络高速下载通道的。

## 特别鸣谢
[UMRnInside](https://github.com/UMRnInside)（提供了开机自动扩容脚本）

# 欢迎加入树莓派64位系统交流群，QQ群号码：697381661
