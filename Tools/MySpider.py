'''
Created on 2017年9月30日

@author: zheng
'''
# 所有爬虫的父类

class MySpider():
    import requests
    from bs4 import BeautifulSoup
    from Tools import MyHeader, MyProxy
