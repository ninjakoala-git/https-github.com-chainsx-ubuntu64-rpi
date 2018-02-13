# 最新的ubuntu-16.04.3(64-Bit)支持wifi

ubuntu-16.04.3使用 NetworkManager 工具来管理网络，其在命令行下对应的命令是 nmcli，要连接WiFi，相关的命令如下：

查看网络设备列表

`$ sudo nmcli dev`

注意，如果列出的设备状态是 unmanaged 的，说明网络设备不受NetworkManager管理，你需要清空 /etc/network/interfaces下的网络设置,然后重启.

开启WiFi

`$ sudo nmcli r wifi on`

扫描附近的 WiFi 热点

`$ sudo nmcli dev wifi`

连接到指定的 WiFi 热点

`$ sudo nmcli dev wifi connect "SSID" password "PASSWORD"`

请将 SSID和 PASSWORD 替换成实际的 WiFi名称和密码。

连接成功后，下次开机，WiFi 也会自动连接。

[关于更多](https://wiki.archlinux.org/index.php?title=NetworkManager_(简体中文)&mobileaction=toggle_view_desktop)
