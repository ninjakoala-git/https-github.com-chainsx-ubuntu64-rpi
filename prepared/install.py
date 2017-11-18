#!/usr/bin/python
#Filename:install.py
import os
print('untar files')
os.popen('tar -zxvf Image.tar.gz')
os.popen('tar -zxvf dtbs.tar.gz')
os.popen('tar -zxvf modiles.tar.gz')
os.popen('tar -zxvf firmware.tar.gz')
