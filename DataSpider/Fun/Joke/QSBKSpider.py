'''
Created on 2017年10月3日

@author: zheng
'''
from Tools.MySpider import MySpider

class QSBKSpider(MySpider):
    def __init__(self):
        MySpider.__init__(self,'https://www.baidu.com/')


if __name__ == '__main__':
    t = QSBKSpider()
    print(t.getPage(t.start_url))
