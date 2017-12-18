# ubuntu-rpi64

ubuntu-rpi64 is an experimental 64-bit OS for the Raspberry Pi 3. It is based on ubuntu 16.04.3 and backed by a 4.9 Linux kernel.

## About

There are two versions: ubuntu 15.10 and ubuntu 16.04.

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

* This system add a swap file at the rootfs,

* I use the `preload` to prelod softwares.
