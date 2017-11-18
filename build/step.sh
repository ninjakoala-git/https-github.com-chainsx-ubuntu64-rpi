#!/bin/bash
cd linux
make ARCH=arm64 bcmrpi3_defconfig
make -j4 dtbs modules Image ARCH=arm64
