class News():
    def __init__(self, title, summary, url):
        self.title = title
        self.summary = summary
        self.url = url

    def __str__(self):
        return '{0}:\n{1}'.format(self.title, self.summary)
