# 最新的16.04支持连接WiFi

* 1.开启wifi
```
sudo ip link set wlan0 up
```

* 2.周围的wifi
```
sudo iw dev wlan0 scan
```
#### 这个把WiFi信息都显示得非常清楚了

* 3.连接wifi

如果您想连接的网络是没有加密的，您可以用下面的命令直接连接：
```
sudo iw dev wlan0 connect [网络 SSID]
```

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
我建议你在文件的末尾添加它，并确保其他配置都注释掉。要注意 SSID 和密码字串都是大小写敏感的。在技术上您也可以把接入点的名称当做是 SSID，使用 wpa_supplicant 工具的话会有合适的 SSID 来替代这个名字。

一旦配置文件修改完成后，在后台启动此命令：

```
sudo wpa_supplicant -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf
```

最后，无论是连到开放的网络还是加密的安全网络，您都得获取 IP 地址。简单地使用如下命令：

```
sudo dhcpcd wlan0
```

如果一切顺利的话，您应该已经通过 DHCP 获取到了一个全新的本地 IP，这个过程是在后台自动完成的。如果想确认下是否真正连接上的话，您可以再一次输入如下命令检查：

```
iwconfig
```
