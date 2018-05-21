from git import Repo
from . import allConfig.Config


class Config(Config):
    '''
        Git工具的配置类
        Git Config Class
    '''
    Level = 2
    GitHubUserName = 'Jackal007'
    RepositoryHttpsLists = [
        "https://github.com/Jackal007/MyDailyNews.git",
        "https://github.com/Jackal007/Python_Notes.git",
        "https://github.com/Jackal007/-Computer-NetWork.git",
        "https://github.com/Jackal007/deep_learning_study.git",
        "https://github.com/Jackal007/-Notes.git",
        "https://github.com/Jackal007/-Linux_Notes.git",
        "https://github.com/Jackal007/database_more.git",
        "https://github.com/Jackal007/my_vim.git",
        "https://github.com/Jackal007/Infomation_Security.git",
        "https://github.com/Jackal007/python-patterns.git",
        "https://github.com/Jackal007/Java_More.git",
        "https://github.com/Jackal007/-Design_Pattern.git",
        "https://github.com/Jackal007/python_spider.git",
        "https://github.com/Jackal007/algorithm.git",
    ]

    def get_RepositorieHttps(self, Repository):
        pass


def backup_to_local():
    for repoURL in Config.repoLists:
        repo = Repo.clone_from(
            repoURL, repoURL)


def local_to_GitHub():
    pass
