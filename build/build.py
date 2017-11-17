#!/usr/bin/python
#Filename:build.py
import os
print('updating list')
os.system('apt update')
print('installing software')
os.system('apt install git')
import('clone')
os.system('git clone https://github.com/raspberrypi/linux')
