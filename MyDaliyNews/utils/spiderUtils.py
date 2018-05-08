'''
Created on 2017年9月30日

@author: zheng

'''

import os
import requests
import unittest
from random import randint
from bs4 import BeautifulSoup
from selenium import webdriver
from random import randint


def getHeader():
    headers = {'opera': ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
                         'Opera/8.0 (Windows NT 5.1; U; en)',
                         'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
                         'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
                         ],
               'firefox': ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
                           'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
                           ],
               'safari': ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
                          ],
               'chrome': ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
                          'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                          'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
                          ],
               }
    allheaders = []
    for i in headers.values():
        for j in i:
            allheaders.append(j)
    return {'User-Agent': allheaders[randint(0, len(allheaders) - 1)]}


class MyProxy():
    def __init__(self):
        self.start_url = 'http://www.xicidaili.com/'
        self.headers = getHeader()
        # 解决别的脚本调用本脚本出现的文件路径问题
        module_path = os.path.dirname(__file__)
        self.file = module_path + '/Myproxy.txt'

    def get_page(self, url):
        page = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(page.text, "lxml")
        return page, soup

    def download_proxy(self):
        # firstly get our proxies
        proxies = self.get_proxy(type='dict')

        # then get proxies from remote server
        _, soup = self.get_page(self.start_url)
        ip_list = soup.select('#ip_list')[0]
        ips = ip_list.select('tr')
        for i in ips:
            i = i.select('td')
            if len(i) > 3:
                proxies[i[1].text] = i[2].text

        # save them
        with open(self.file, 'w') as f:
            for ip, port in proxies.items():
                f.write(ip + ',' + port + '\n')

    def get_proxy(self, type='list'):
        with open(self.file, 'r') as f:
            if type == 'list':
                proxies = []
                for i in f.readlines():
                    i = i.strip()
                    ip = i.split(',')[0]
                    port = i.split(',')[1]
                    proxies.append({'ip': ip, 'port': port})
            else:
                proxies = {}
                for i in f.readlines():
                    i = i.strip()
                    ip = i.split(',')[0]
                    port = i.split(',')[1]
                    proxies[ip] = port

        return proxies

    def get_a_proxy(self):
        proxies = self.get_proxy()
        proxy = proxies[randint(0, len(proxies) - 1)]
        return {'proxy': 'http:\\' + proxy['ip'] + ':' + proxy['port']}


def get_proxy():
    t = MyProxy()
    return t.get_a_proxy()


class RequestsSpider():
    '''
        所有爬虫的父类 requests版
    '''

    def __init__(self, baseURL):
        self.baseURL = baseURL

    def login(self, url, postdata):
        from .MyExceptions import LoginFailException

        session = requests.Session()
        try:
            session.post(url, headers=getHeader(),
                         proxies=get_proxy(), data=postdata)
        except:
            raise LoginFailException
        return session

    def get_page(self, url, session=requests):
        from .MyExceptions import GetPageFailException

        try:
            page = session.get(
                url, headers=getHeader(), proxies=get_proxy())
        except:
            raise GetPageFailException
        soup = BeautifulSoup(page.text)
        print(page.status_code)
        return page, soup


class SeleniumSpider(unittest.TestCase):
    '''
        所有爬虫的父类 selenium版
    '''

    def __init__(self, baseURL):
        self.baseURL = baseURL
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)

    def get_page(self):
        pass

    def tearDown(self):
        self.driver.close()
