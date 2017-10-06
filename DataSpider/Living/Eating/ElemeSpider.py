'''
Created on 2017年10月6日

@author: zheng
'''
from Tools.MySpider import MySpider

class ElemeSpider(MySpider):
    def __init__(self):
        MySpider.__init__(self, 'https://www.ele.me/place/ws7gpbcqw80?latitude=24.43883&longitude=118.11601')
        
    def getRestaurant(self):
        _, soup = self.getPage(self.start_url)
        allRestaurant = soup.select('div[class="clearfix"]')
        print(allRestaurant)


if __name__ == '__main__':
    t = ElemeSpider()
    t.getRestaurant()
