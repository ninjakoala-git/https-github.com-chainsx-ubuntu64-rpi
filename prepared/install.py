#!/usr/bin/python
#Filename:install.py
import os
print('安装中文字库')
os.popen('apt update')
os.popen('apt install ttf-wqy-zenhei')
print('untar files')
os.popen('tar -zxvf Image.tar.gz')
os.popen('tar -zxvf dtbs.tar.gz')
os.popen('tar -zxvf modiles.tar.gz')
os.popen('tar -zxvf firmware.tar.gz')
os.popen('mkdir images')
print('请把将要移植的镜像放入images文件夹中')
os.popen('apt install kpartx')
os.popen('kpartx -av images/*.img')
os.popen('mount /dev/mapper/*2 /img')
os.popen('mount /dev/mapper/*1 /img/boot')

