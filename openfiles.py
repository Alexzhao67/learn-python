#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-07-06 14:10
# @Author  : Alex   alexzyq@outlook.com
# @FileName: openfiles.py
# @Software: PyCharm
import os

f=open('test.txt',mode='w')
f.write('Hello world\r\n'*100)
f.close()

f=open('test.txt',mode='r')
# print(f.read(100))
print(f.readlines(9))

with open('test.txt',mode='r') as fp:
    print(fp.read())