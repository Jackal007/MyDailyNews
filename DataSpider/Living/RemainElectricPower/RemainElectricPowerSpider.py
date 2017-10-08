'''
Created on 2017年9月19日
Last Modify 2017年10月8日

@author: jack
'''
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Tools.SeleniumSpider import SeleniumSpider

class RemainElectricPowerSpider(SeleniumSpider):
    def __init__(self):
        SeleniumSpider.__init__(self, 'http://elec.xmu.edu.cn/PdmlWebSetup/Pages/SMSMain.aspx')
      
    def haha(self):
        driver = self.driver
        xiaoqu = Select(driver.find_element_by_id("drxiaoqu"))
        xiaoqu.select_by_visible_text('曾厝安学生公寓')
        lou = Select(driver.find_element_by_id("drlou"))
        lou.select_by_visible_text('2号楼')
        room = driver.find_element_by_id("txtRoomid")
        submit = driver.find_element_by_id("dxbtnQuery_CD")
        
        room.send_keys('0609')
        submit.click()
        return driver.page_source
    
if __name__ == '__main__':
    t = RemainElectricPowerSpider()
    print(t.haha())
    t.hehe()
