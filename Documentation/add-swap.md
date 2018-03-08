* 添加swap分区
 
编辑/etc/dphys-swapfile
```
sudo vi /etc/dphys-swapfile
``` 
将 CONF_SWAPSIZE 的值修改成你想要的大小。 一般在内存小于2G的情况下，交换分区应为内存的2倍!(树莓派的话是2G最好)
 
然后，重新启动 dphys-swapfile 文件服务
``` 
sudo /etc/init.d/dphys-swapfile restart
```
