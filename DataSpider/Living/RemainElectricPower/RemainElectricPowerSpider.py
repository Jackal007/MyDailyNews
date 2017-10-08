'''
Created on 2017年9月19日
Last Modify 2017年10月8日

@author: jack
'''
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
from Tools.SeleniumSpider import SeleniumSpider

class RemainElectricPowerSpider(SeleniumSpider):
    def __init__(self):
        SeleniumSpider.__init__(self, 'http://elec.xmu.edu.cn/PdmlWebSetup/Pages/SMSMain.aspx')
      
    def getPage(self):
        driver = self.driver
        
        # 选择校区
        xiaoqu = Select(driver.find_element_by_id("drxiaoqu"))
        xiaoqu.select_by_visible_text('曾厝安学生公寓')
        # 选择楼名
        lou = Select(driver.find_element_by_id("drlou"))
        lou.select_by_visible_text('2号楼')
        # 输入房间号
        room = driver.find_element_by_id("txtRoomid")
        room.send_keys('0609')
        # 点击提交按钮
        submit = driver.find_element_by_id("dxbtnQuery_CD")
        submit.click()
        
        page, soup = driver.page_source, BeautifulSoup(driver.page_source)
        return page, soup
    
    def getRemainElectricPower(self):
        _, soup = self.getPage()
        remain=soup.select('#lableft')[0].string
        return remain
        
    
if __name__ == '__main__':
    t = RemainElectricPowerSpider()
    print(t.getRemainElectricPower())
#     t.tearDown()
