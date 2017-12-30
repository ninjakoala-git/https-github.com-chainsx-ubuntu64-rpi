#!/usr/bin/python
#Filename:build.py
import os
print('updating list')
os.pepon('apt update')
print('installing software')
os.pepon('apt install git')
print('clone sources')
os.system('git clone https://github.com/raspberrypi/linux')
os.system('sh step.sh')
print('build finish, please run install.py')
