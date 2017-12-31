# ubuntu-rpi64

ubuntu-rpi64 is an experimental 64-bit OS for the Raspberry Pi 3. It is based on ubuntu 17.04 and backed by a 4.9 Linux kernel.

## About

There are three versions: ubuntu 15.10 , ubuntu 16.04 and ubuntu 17.04.

But the stable one is ubuntu 16.04.3.

## How to install this system?

You can follow this [instructions](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) to write the image to your SD-card.

## How to getting started?

The username is `ubuntu`,and password is `ubuntu`.

For root,password is `root`.

Once logged in, you might want to run sudo `raspi-config` or `chainsx-config` in order to get assisted with your setup!

On the lite version, SSH is enabled by default.

## Others

* You can follow this step to enable the 32-bit support.

`sudo dpkg --add-architecture armhf`

`sudo apt-get update`

`sudo apt-get install libc6:armhf`

* This system buiding based ubuntu-Base-17.04

************************
# Download link

onedrive:https://1drv.ms/u/s!Aj2tyhuVKq9-c6eH_pbiP2gUnI8

yandex.disk:https://yadi.sk/d/ysdTPoeF3R7LCU

mega:https://mega.nz/#!wqwUgSrY!5a-0gcJecn9X94_Ahr6g4OBISl7CbFNk_ZJXkKvIHr4

sandisk.cloud:https://sandisk.upthere.com/loop/c0fe40d8a0919986d822e8754e0c5553c3049b6ba244f9ee3d0edcdbeecb3a1c
