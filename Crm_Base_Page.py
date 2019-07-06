#Coding:utf-8
#Author:MuTou<****@163.com>
#Time:2019/6/24 0024 上午 11:43
#File:Crm_Base_Page.py
#Project_Name:
#Content:此页面是获取驱动器对象页面

from selenium import webdriver
#还可以额外自己封装，可以传入任意的浏览器参数即可通过不同的浏览实现自动化
class Base_Page:
    def __init__(self,browserType,url):
        if browserType=="IE":
            self.get_drvier=webdriver.Ie()
        elif browserType=="Chrome":
            self.get_drvier=webdriver.Chrome()
        elif browserType=="FireFox":
            self.get_drvier=webdriver.Firefox()
        self.get_drvier.get(url)

