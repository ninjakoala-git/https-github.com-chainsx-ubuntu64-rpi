* 添加树莓派官方软件源镜像（安装树莓派官方提供的特有软件包）

```
root@ubuntu:~# apt-get update
root@ubuntu:~# apt-get install debian-keyring
root@ubuntu:~# echo "deb [arch=armhf] http://mirrors.ustc.edu.cn/archive.raspberrypi.org main ui untested staging" >> /etc/apt/sources.list
root@ubuntu:~# echo "deb [arch=armhf] http://mirrors.ustc.edu.cn/raspbian/raspbian main contrib firmware non-free rpi" >> /etc/apt/sources.list
```
