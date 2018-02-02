# 最新的16.04支持链接WiFi

首先，你需要更改/etc/network/interfaces

改为如下

```
# interfaces(5) file used by ifup(8) and ifdown(8)
# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d
#allow-hotplug eth0
#iface eth0 inet manual

#allow-hotplug wlan0
#iface wlan0 inet manual
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp
```

这里，注意去掉`wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf`前的注释。

然后，新建一个文件`/etc/wpa_supplicant/wpa_supplicant.conf`按照如下填写：

```
country=CN
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
 
network={
ssid="WiFi-A"
psk="12345678"
key_mgmt=WPA-PSK
priority=1
}
 
network={
ssid="WiFi-B"
psk="12345678"
key_mgmt=WPA-PSK
priority=2
scan_ssid=1
}
```

说明以及不同安全性的 WiFi 配置示例：

#ssid:网络的ssid

#psk:密码

#priority:连接优先级，数字越大优先级越高（不可以是负数）

#scan_ssid:连接隐藏WiFi时需要指定该值为1

如果你的 WiFi 没有密码

```
network={
ssid="你的无线网络名称（ssid）"
key_mgmt=NONE
}
```

如果你的 WiFi 使用WEP加密

```
network={
ssid="你的无线网络名称（ssid）"
key_mgmt=NONE
wep_key0="你的wifi密码"
}
```

如果你的 WiFi 使用WPA/WPA2加密

```
network={
ssid="你的无线网络名称（ssid）"
key_mgmt=WPA-PSK
psk="你的wifi密码"
}
```

如果你不清楚 WiFi 的加密模式，可以在安卓手机上用 root explorer 打开 /data/misc/wifi/wpa/wpa_supplicant.conf，查看 WiFi 的信息。
