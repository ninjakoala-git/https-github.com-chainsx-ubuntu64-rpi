# RaspberryPi3-ubuntu-16.04-aarch64          [English](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-16.04-arm64/README-EN.md)
***************
####### 插播一段广告。。。。。
##### [ubuntu-18.04-arm64预览版](https://github.com/chainsx/ubuntu64-rpi/tree/ubuntu-bonic(18.04)-preview)
#### [最新版mainline(4.16)内核（适用于所有树莓派3系统）](https://github.com/chainsx/firmware64-rpi)

##### [64位centos戳这里(做服务器建议使用此版本)](https://github.com/chainsx/centos64-rpi)
##### [64位debian(非pi64)](https://github.com/UMRnInside/RPi-arm64)
***************

# 经测试，ubuntu-arm64的性能最高提高60倍!!!

****************
![example1](https://github.com/chainsx/ubuntu64-rpi/raw/ubuntu-16.04.3-arm64/imagine/321.jpg "example1")
##### (⬆图为u盘启动实例，可以看到，根目录文件系统为btrfs，挂载于/)

## 前言：
#### ubuntu官方居然不给RaspberrPi3出官方镜像（官方推荐的镜像是Electron752移植的，对，移植版，ubuntu官方不会直接给支持的），而rpi2都有16.04/17.04/17.10的官方镜像……

## 声明：
* 本系统由我（chainsx）**自行构建**的根目录以及boot。
* 注意，是自行构建的系统，而**非移植**系统！！！
* 如需定制版以及商业用途，请**务必**与本人联系。
* 可以转载，推广甚至修改本系统，但**必须注明出处**。
* 你可以基于本系统打造更加完善的系统，但**必须注明出处**。
* 帮助文档在[这里](https://github.com/chainsx/ubuntu64-rpi/wiki)
#### …………


## 关于:

* 本系统是直接基于ubuntu-Base-16.04-arm64构建的根目录， **非移植版** ，所以稳定性有提升，但是整个系统不够完善。
* **ubuntu官方为bcm2837给了支持**，只不过是以raspi2命名，原因是晚期的raspi2是使用的bcm2837芯片。
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
* **第一次开机时会自动拓展根目录，然后会自动重启，重启后会配置系统，请耐心等待**。
* 默认使用清华源，**如果你的树莓派无法解析清华源的地址**(apt时提示404或者卡住不动)，看[这里](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-16.04.3-arm64/Documentation/dns-setting.md)
* 集成了`raspi-config`,`chainsx-tools`系统集成管理工具，使用方法：
```
sudo raspi-config

sudo chainsx-tools
```

## 关于内核(测试版使用[maimline4.16内核](https://github.com/chainsx/firmware64-rpi))

- [X] wifi
- [X] bluetooth(蓝牙使用前需要配置)
- [X] GPIO

|  联系方式   |           |
|-----------|------------|
|QQ|1396219808(CX_rootfs)|
|E-mail|chainsx@outlook.com i@chainsx.cn|

**********************

## 下载地址：

### 百度网盘(Baidu Netdisk)

| 版本 | 下载链接 |
|--------|--------|
| ubuntu-16.04-arm64-stable-with-wifi(稳定版带wifi，使用方法在上面。) | [链接](https://pan.baidu.com/s/1htHqn7Q) |
| ubuntu-16.04-arm64-nightly-4.16-kernel(Alpha测试版) | [链接](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-16.04.3-arm64/Documentation/about-test.md) |

##### 如果百度云限速的问题你无法解决的话（至少是要下载1h以上的话），请联系我，我会给你提供腾讯云计算对象储存高速下载通道。

## 特别鸣谢
[UMRnInside](https://github.com/UMRnInside)（提供了开机自动扩容方法)

[树莓派基金会](https://www.raspberrypi.org) (提供了开机自动扩容脚本)

[Armbian](https://armbian.com) (提供了chainsx-tools源码)

@ 束发少年 (提供论坛支持)
 
# 欢迎加入树莓派64位系统交流群，QQ群号码：697381661
# 论坛支持https://raspberrypi.party
## 感谢 @束发少年 的论坛支持
