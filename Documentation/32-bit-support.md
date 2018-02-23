* 因为是64位系统，所以你可以开启32位支持,开启方法：


```
root@ubuntu:~# dpkg --add-architecture armhf   #开启armhf支持
root@ubuntu:~# apt-get update
root@ubuntu:~# apt-get install libc6:armhf
root@ubuntu:~# dpkg --add-architecture armel  #开启armel支持
root@ubuntu:~# apt-get update
root@ubuntu:~# apt-get install libc6-armel
```
