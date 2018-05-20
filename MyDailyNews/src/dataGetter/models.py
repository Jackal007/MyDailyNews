from django.db import models

# Create your models here.


class SimplifyNews(models.Model):
    '''
        精简版的新闻类
    '''
    id = models.AutoField(primary_key=True, max_length=10)
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)
    url = models.CharField(max_length=500)

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
    content = models.TextField(max_length=5000)
    datetime = models.DateTimeField()
    pictures = models.CharField(max_length=500)
