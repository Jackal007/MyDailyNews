'''
Created on 2017年10月6日
天天美剧新闻查看
@author: zheng
'''
from Tools.MySpider import MySpider

class TTMJSpider(MySpider):
    def __init__(self):
        MySpider.__init__(self, 'http://www.ttmeiju.com/index.php/user/login.html')
        
    def getNews(self):
        postdata = {
            'username':'jackal007',
            'password':'1123581321',
            'referurl':'/',
            }
        session = self.login(self.start_url, postdata)
        _, soup = self.getPage('http://www.ttmeiju.com/', session=session)
        print(soup.select('.content'))
#         weekHot = soup.select('.weekhot')
#         return weekHot
        
if __name__ == '__main__':
    t = TTMJSpider()
    t.getNews()
