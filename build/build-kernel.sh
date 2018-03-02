#!/bin/sh
wget https://github.com/raspberrypi/linux/archive/rpi-4.11.y.zip
unzip rpi*
cd linux*
make bcmrpi3_defconfig CROSS_COMPILE=aarch64-linux-gnu-
make -j4 ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu-
