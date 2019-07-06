

from selenium import webdriver

class Base_Page:
    def __init__(self,browserType,url):
        if browserType=="IE":
            self.get_drvier=webdriver.Ie()
        elif browserType=="Chrome":
            self.get_drvier=webdriver.Chrome()
        elif browserType=="FireFox":
            self.get_drvier=webdriver.Firefox()
        self.get_drvier.get(url)

