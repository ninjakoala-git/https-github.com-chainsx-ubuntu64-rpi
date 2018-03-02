#!/bin/sh
echo 'wget rootfs'
wget -O rootfs.tar.gz http://cdimage.ubuntu.com/ubuntu-base/releases/16.04.4/release/ubuntu-base-16.04.3-base-arm64.tar.gz
tar -zxvf rootfs.tar.gz
