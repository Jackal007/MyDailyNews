import requests
from random import randint
from bs4 import BeautifulSoup
from Tools import MyHeader 
import os

class MyProxy():
    def __init__(self):
        self.start_url = 'http://www.xicidaili.com/'
        self.headers = MyHeader.getHeader()
        #解决别的脚本调用本脚本出现的文件路径问题
        module_path = os.path.dirname(__file__)   
        self.file = module_path + '/Myproxy.txt'
    
    def getPage(self, url):
        page = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(page.text, "lxml")
        return page, soup
    
    def downloadProxy(self):
        # firstly get our proxies
        proxies = self.getProxy(type='dict')  
        
        # then get proxies from remote server
        _, soup = self.getPage(self.start_url)
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
    
    def getProxy(self, type='list'):  
        with open(self.file, 'r') as f:
            if type == 'list':
                proxies = []
                for i in f.readlines():
                    i = i.strip()
                    ip = i.split(',')[0]
                    port = i.split(',')[1]
                    proxies.append({'ip':ip, 'port':port})
            else:
                proxies = {}
                for i in f.readlines():
                    i = i.strip()
                    ip = i.split(',')[0]
                    port = i.split(',')[1]
                    proxies[ip] = port
                
        return proxies
    
    def getAProxy(self):
        proxies = self.getProxy()
        proxy = proxies[randint(0, len(proxies) - 1)]
        return {'proxy':'http:\\' + proxy['ip'] + ':' + proxy['port']}

def getProxy():
    t = MyProxy()
    return t.getAProxy()

if __name__ == '__main__':
    t = MyProxy()
    t.downloadProxy()
    print(t.getAProxy())

    
