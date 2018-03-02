#!/usr/bin/python
#Filename:build.py
import os
print('updating list')
os.pepon('apt update')
print('installing software')
os.pepon('apt install git unzip gcc-aarch64-linux-gnu')
print('clone sources')
os.system('sh build-kerbel.sh')
os.system('sh step1.sh')
print('build finish, please run install.py')
