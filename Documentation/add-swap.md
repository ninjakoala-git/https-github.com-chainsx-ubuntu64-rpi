* 添加swap分区

```
root@ubuntu:~# dd if=/dev/zero of=/swapfile bs=2048 count=1M     #创建一个大小为2G的文件
root@ubuntu:~# mkswap /swapfile     #把这个文件变成swap文件
root@ubuntu:~# chown root:root /swapfile    #授权root
root@ubuntu:~# chmod 0600 /swapfile    设置权限
root@ubuntu:~# swapon /swapfile     #启用这个swap文件
#编辑/etc/fstab文件，使在每次开机时自动加载swap文件：
/swapfile swap swap default 0 0
```
