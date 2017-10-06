'''
Created on 2017年10月6日
爬取附近的外卖信息
@author: zheng
'''
from Tools.MySpider import MySpider

class ElemeSpider(MySpider):
    def __init__(self):
        MySpider.__init__(self, 'http://waimai.meituan.com/home/ws7gpfn21jvq')
        
    def getRestaurant(self):
        #=======================================================================
        # 返回所有的商家名和链接
        #=======================================================================
        _, soup = self.getPage(self.start_url)
        allRestaurants = soup.select('ul[class="list clearfix"]')[0].select('li[class="fl rest-li"]')
       
        restaurants = {}
        for i in allRestaurants:
            name = i.select('.name span')[0].string.strip()
            link = i.select('.rest-atag')[0]['href']
            restaurants[name] = link
        return restaurants


if __name__ == '__main__':
    t = ElemeSpider()
    print(t.getRestaurant())
