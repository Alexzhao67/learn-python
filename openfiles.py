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
    
    
    os.rename('test.txt', 'test0415.txt')
   

# get partial string from the special line of  a file 
def get_partial_txt(path, n, line):
    f= open(path, mode='r')
    list_lines = f.readlines()
    line_txt = list_lines[line-1]
    partial_txt = line_txt[:n]
    return partial_txt
    
    
    
