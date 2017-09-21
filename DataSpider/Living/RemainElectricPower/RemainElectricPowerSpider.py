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
            '__EVENTTARGET':'',
            '__EVENTARGUMENT':'',
            '__LASTFOCUS':'',
            '__VIEWSTATE':'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',
            '__EVENTVALIDATION':'/wEWMwK8i4vCCgLM+ZZaAsz5lloC3JbwtwwC3Jb0twwC3JbItwwC3JbMtwwC3JbAtwwC3JbEtwwC3JbYtwwCwpbEtwwC3JactAwC3JaQtAwCwpbwtwwCwpb0twwCwpbItwwCwpbMtwwCwpbAtwwCwpbYtwwCwpactAwCwpaQtAwCwZb8twwCwZbwtwwCwZb0twwCwZbItwwCwZbMtwwCwZbAtwwCwJb0twwCwJbwtwwCwJb8twwCw5b8twwCw5bwtwwCw5b0twwCx5b8twwCx5bwtwwCx5b0twwCg8HlgQYCt7qC2QgCmrSCyAgC16zlnwsC7Jf7sgECiYHZyQcC2LrwiQYCuK2/egKlg/68CALC6tzTDgLUsbrtBgKJoMPiDQLE4IbRAwKXqKQUApunmcIIKBl3wpO7YkcxFjOOy89p4zBb5BY=',
            'drxiaoqu':'04',
            'drlou':'凌云1号公寓',
            'txtRoomid':'0202',
            'dxdateStart_Raw':'1504224000000',
            'dxdateStart':'2017-09-01',
            'dxdateStart_DDDWS':'0:0:-1:-10000:-10000:0:-10000:-10000:1',
            'dxdateStart_DDD_C_FNPWS':'0:0:-1:-10000:-10000:0:0px:-10000:1',
            'dxdateStart$DDD$C':'09/01/2017:09/01/2017',
            'dxdateEnd_Raw':'1505779200000',
            'dxdateEnd':'2017-09-19',
            'dxdateEnd_DDDWS':'0:0:-1:-10000:-10000:0:-10000:-10000:1',
            'dxdateEnd_DDD_C_FNPWS':'0:0:-1:-10000:-10000:0:0px:-10000:1',
            'dxdateEnd$DDD$C':'09/19/2017:09/19/2017',
            'dxbtnQuery':'',
            'dxgvSubInfo$DXSelInput':'',
            'dxgvSubInfo$CallbackState':'/wEWBB4ERGF0YQUsQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBSEFBY0EeBVN0YXRlBVRCd1VIQUFJQkJ3RUNBUWNCQWdFSEFRSUJCd0lDQVFjQUJ3QUhBQWNBQlFBQUFJQUpBZ0FKQWdBQ0FBTUhCQUlBQndBQ0FRY0FCd0FDQVFjQUJ3QT0=',
            'dxgvElec$DXSelInput':'',
            'dxgvElec$CallbackState':'/wEWBB4ERGF0YQUsQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBSEFBY0EeBVN0YXRlBVhCd1lIQUFJQkJ3RUNBUWNCQWdFSEFRSUJCd0VDQVFjQ0FnRUhBQWNBQndBSEFBVUFBQUNBQ1FJQUNRSUFBZ0FEQndRQ0FBY0FBZ0VIQUFjQUFnRUhBQWNB',
            'DXScript':'1_42,1_74,2_22,2_29,1_46,1_54,2_21,1_67,1_64,2_16,2_15,1_52,1_65,3_7',
            
            }
        
    def getPage(self):
        header = {
            'User-Agent':MyHeader.getHeader()
        }
        proxy = {
            'http':MyProxy.getProxy()
        }
        r = requests.put(self.start_url, headers=header, data=self.postdata)
        return r.content
    
    def getRemainElectricPower(self):
        r = self.getPage()
        soup = BeautifulSoup(r)
        with open('temp', 'wb')as f:
            f.write(r)
        remainElectricPower = soup.select('tr[id="dxgvElec_DXDataRow0"]')
        print(remainElectricPower)  # .select('td')[-1].string
        return remainElectricPower          

t = RemainElectricPowerSpider('09', '2号楼', '0609', '2017-9-1', '2017-9-19')
print(t.getRemainElectricPower())
