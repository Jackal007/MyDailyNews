'''
Created on 2017年10月8日

@author: zheng

所有爬虫的父类 selenium版
'''

from selenium import webdriver
import unittest

class SeleniumSpider(unittest.TestCase):
    def __init__(self, start_url):
        self.start_url = start_url
        self.driver = webdriver.Chrome()
        self.driver.get(self.start_url)
        
    def tearDown(self):
        self.driver.close()
