* 为不同的架构指定不同的源，你需要编辑`/etc/apt/sources.list`为如下模样（只是举个例子）：

```
deb [arch=armel] http://cn.ports.ubuntu.com/ubuntu-ports quantal main universe   #ubuntu官方中国源
deb [arch=armhf] http://ftp.cn.debian.org/ubuntu-ports quantal main universe    #科大源
deb [arch=arm64] http://ftp2.cn.debian.org/ubuntu-ports quantal main universe    #清华源
```

#### [官方帮助文档MultiArch](https://wiki.debian.org/Multiarch/HOWTO)
