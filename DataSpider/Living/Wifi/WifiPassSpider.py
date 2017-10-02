'''
Created on 2017年10月2日

@author: zheng

获取附近的wifi密码
'''
import pywifi 
from pywifi import const
import time
import sys

'''
pywifi是一个用来搞wifi的模块

下一章我们将用他破解wifi密码

pywifi安装

pip install pywifi

下列代码判断是否有无限网卡

 1 import pywifi
 2 import sys
 3 import time
 4 from pywifi import const
 5 
 6 def gic():
 7   wifi=pywifi.PyWifi()#创建一个无线对象
 8   ifaces=wifi.interifaces()[0]#取第一个无限网卡
 9   if ifaces in [const.IFACE_DISCONNECTED,
10                    const.IFACE_INACTIVE]
11      print(‘已连接‘)
12   else:
13     print(‘未连接‘)
14 
15 
16 gic()
扫描附近的wifi

import pywifi
import sys
import time
from pywifi import const
def bies():
  wifi=pywifi.PyWifi()#创建一个无限对象
  ifaces=wifi.interifaces()[0]#取一个无限网卡
  ifaces.scan()#扫描
  bessis=ifaces.scan_results()
 for data in bessis:
    print(data.ssid)#输出wifi名称
尝试并连接wifi

import pywifi
import sys
import time
from pywfi import const

def deswifi():
  wifi=pywifi.PyWifi()#创建一个wifi对象
  ifaces=wifi.iinterifaces()[0]#取第一个无限网卡
  print(ifaces.name())#输出无线网卡名称
  ifaces.disconnect()#断开网卡连接
  time.sleep(3)#缓冲3秒
  
 profile=pywifi.profile()#配置文件
 profile.ssid="TP-LINK_489"#wifi名称
 profile.auth=const.AUTH_ASG_OPEN#需要密码
 profile.akm.append(const.AKM_TYPE_WPA2SK)#加密类型
 profile.cipher=const.CIPHER_TYPE_CCMP#加密单元

 ifaces.remove_all_network_profiles()#删除其他配置文件
 tmp_profile=ifaces.add_network_profile(profile)#加载配置文件

 ifaces.connect(tmp_profile)#连接
 time.sleep(10)#尝试10秒能否成功连接
 isok=True
 if ifaces.status()==const.IFACE_CONNECTED:
   print("成功连接")
else:
  print("失败")
  ifaces.disconnect()#断开连接
  time.sleep(1)
  return isok

deswifi()
'''









































