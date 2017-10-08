'''
Created on 2017年9月30日

@author: zheng

所有爬虫的父类 requests版
'''

import requests
from bs4 import BeautifulSoup 
from Tools import MyHeader, MyProxy

class RequestsSpider():
    def __init__(self, start_url):
        self.start_url = start_url
        
    def login(self, url, postdata):
        session = requests.Session()
        try:
            session.post(url, headers=MyHeader.getHeader(), proxies=MyProxy.getProxy(), data=postdata)
        except:
            print('login fail')
        return session

    def getPage(self, url, session=requests):
        try:
            page = session.get(url, headers=MyHeader.getHeader(), proxies=MyProxy.getProxy())
        except:
            print('get page fail')
        soup = BeautifulSoup(page.text, "lxml")
        print(page.status_code)
        return page, soup
