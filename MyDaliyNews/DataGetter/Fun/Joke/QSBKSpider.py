'''
Created on 2017年10月3日

@author: jack
'''
from MyDaliyNews.utils.spiderUtils import RequestsSpider


class QSBKSpider(RequestsSpider):
    def __init__(self):
        RequestsSpider.__init__(self, 'https://www.qiushibaike.com/')


if __name__ == '__main__':
    t = QSBKSpider()
    print(t.get_page(t.baseURL))
