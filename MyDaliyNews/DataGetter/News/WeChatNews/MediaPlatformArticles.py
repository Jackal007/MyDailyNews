from wxpy import Bot
from utils.MyTypes import News


bot = Bot(cache_path=True)


def get_news():
    '''
        获得微信公众号的推送文章
        Get articles from WeChat mp
    '''

    return get_articles()


def get_articles():
    '''
        获得微信公众号的推送文章
        Get articles from WeChat mp
    '''
    news_list = []

    MyMessages = bot.messages
    for m in MyMessages:
        articles = m.articles
        if articles:
            for article in articles:
                news = News(title=article.title,
                            summary=article.summary,
                            url=article.url)
                news_list.append(news)
                print(news)

    return news_list
