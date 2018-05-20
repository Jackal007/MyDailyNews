'''
Created on 2017年10月3日

@author: jack
'''
from lib.utils.spiderUtils import RequestsSpider
from lib.core.myTypes import News


class QSBKSpider(RequestsSpider):
    def __init__(self):
        RequestsSpider.__init__(self, 'https://www.qiushibaike.com/')

    def get_QSs(self):
        ''' 
            获取多个糗事
            get many Jokes from QSBK
        '''
        QS_list = []

        _, page = self.get_page(self.baseURL)
        rawQSs = page.select('div.article.block.untagged.mb15')
        for rawQS in rawQSs:
            QS_list.append(self.get_QS(rawQS))

        return QS_list

    def get_QS(self, rawQS):
        '''
            获取一个糗事
            get a Jokes from QSBK
        '''
        text = self.get_text(rawQS)
        pitures = self.get_pictures(rawQS)

        QS = News(title=1, datetime=None, sumary=None,
                  content=text, pictures=pitures, url='none'
                  )

        return QS

    def get_text(self, rawQS):
        text = rawQS.select('.content')[0].span.string
        try:
            return text.strip()
        except:
            return text

    def get_pictures(self, rawQS):
        picture_list = []
        pictures = rawQS.select('img')
        for p in pictures:
            picture_list.append(p['src'])

        return picture_list

class other(RequestsSpider):
    def __init__(self):
        RequestsSpider.__init__(self, 'https://www.qiushibaike.com/')

    def get_QSs(self):
        ''' 
            获取多个糗事
            get many Jokes from QSBK
        '''
        QS_list = []

        _, page = self.get_page(self.baseURL)
        rawQSs = page.select('div.article.block.untagged.mb15')
        for rawQS in rawQSs:
            QS_list.append(self.get_QS(rawQS))

        return QS_list

    def get_QS(self, rawQS):
        '''
            获取一个糗事
            get a Jokes from QSBK
        '''
        text = self.get_text(rawQS)
        pitures = self.get_pictures(rawQS)

        QS = News(title=1, datetime=None, sumary=None,
                  content=text, pictures=pitures, url='none'
                  )

        return QS

    def get_text(self, rawQS):
        text = rawQS.select('.content')[0].span.string
        try:
            return text.strip()
        except:
            return text

    def get_pictures(self, rawQS):
        picture_list = []
        pictures = rawQS.select('img')
        for p in pictures:
            picture_list.append(p['src'])

        return picture_list



if __name__ == '__main__':
    t = QSBKSpider()
    t.get_QSs()
