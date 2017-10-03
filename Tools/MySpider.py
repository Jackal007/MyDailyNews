'''
Created on 2017年9月30日

@author: zheng

所有爬虫的父类
'''

import requests
from bs4 import BeautifulSoup 
from Tools import MyHeader, MyProxy

class MySpider():
    def __init__(self, start_url):
        self.start_url = start_url

    def getPage(self, url):
        page = requests.get(url, headers=MyHeader.getHeader(), proxies=MyProxy.getProxy())
        soup = BeautifulSoup(page.text, "lxml")
        return page, soup
