wget https://github.com/raspberrypi/linux/archive/rpi-4.11.y.zip
unzip rpi*
cd linux*
make bcmrpi3_defconfig
make -j4 ARCH=arm64
