from django.db import models

# Create your models here.
class SimplifyNews():
    '''
        精简版的新闻类
    '''

    def __init__(self, title, summary, url):
        self.title = title
        self.summary = summary
        self.url = url

    def __str__(self):
        return '{0}:\n{1}'.format(self.title, self.summary)

    # def get_title(self):
    #     return self.title

    # def get_summary(self):
    #     return self.__summary

    # def get_url(self):
    #     pass


class News(SimplifyNews):
    '''
        基本版的新闻类
    '''

    def __init__(self, title, datetime, sumary,
                 content, pictures, url):
        SimplifyNews.__init__(self,title, sumary, url)
        self.content = content
        self.datetime = datetime
        self.pictures = pictures
