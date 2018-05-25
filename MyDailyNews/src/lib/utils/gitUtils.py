'''
    还要增加的功能
    1.输入一个用户名，自动获取他有些什么repo
'''
import platform
from tqdm import tqdm
from git import Repo
# from . import allConfig.Config


class GitConfig():
    '''
        Git工具的配置类
        Git Config Class
    '''
    def get_BackupPath(localSystemUser):

        operatingSystem = platform.system()

        if operatingSystem == 'Windows':
            BackupPath = 'C:\\Users\\{0}\\Desktop\\github_backup\\'.format(
                localSystemUser)
        elif operatingSystem == 'Linux':
            BackupPath = '/home/{0}/'.format(localSystemUser)
        else:
            BackupPath = '/i do not know'

        return BackupPath

    def get_RepositoryHttpsLists():

        return [
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

    Level = 2
    GitHubUserName = 'Jackal007'
    BackupPath = get_BackupPath(localSystemUser='zheng')
    RepositoryHttpsLists = get_RepositoryHttpsLists()

#######################################################################################


def backup_to_local():
    for repoURL in tqdm(GitConfig.RepositoryHttpsLists):
        repoName = repoURL.split('/')[-1].replace('.git', '')
        Repo.clone_from(
            repoURL, GitConfig.BackupPath+repoName)


def local_to_GitHub():
    pass


if __name__ == '__main__':

    backup_to_local()
