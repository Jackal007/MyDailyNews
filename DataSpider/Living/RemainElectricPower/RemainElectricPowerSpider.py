'''
Created on 2017年9月19日

@author: jack
'''
import requests
from bs4 import BeautifulSoup
from Tools import MyHeader, MyProxy

class RemainElectricPowerSpider():
    def __init__(self, xiaoqu, lou, roomId, dateStart, dateEnd):
        self.start_url = 'http://elec.xmu.edu.cn/PdmlWebSetup/Pages/SMSMain.aspx'
        self.postdata = {
            'drxiaoqu':xiaoqu,
            'drlou':lou,
            'txtRoomid':roomId,
            'dxdateStart':dateStart,
            'dxdateEnd':dateEnd,
            }
        
    def getPage(self):
        header = {
            'User-Agent':MyHeader.getHeader()
        }
        proxy = {
            'http':MyProxy.getProxy()
        }
        r = requests.put(self.start_url, headers=header, proxies=proxy, data=self.postdata)
        return r.content
    
    def getRemainElectricPower(self):
        r = self.getPage()
        soup = BeautifulSoup(r)
        with open('temp','wb')as f:
            f.write(r)
        remainElectricPower = soup.select('tr[id="dxgvElec_DXDataRow0"]')
        print(remainElectricPower)  # .select('td')[-1].string
        return remainElectricPower          

t = RemainElectricPowerSpider('09', '2号楼', '0609', '2017-9-1', '2017-9-19')
print(t.getRemainElectricPower())
