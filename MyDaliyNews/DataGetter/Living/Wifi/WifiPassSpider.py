'''
Created on 2017年10月2日

@author: zheng

获取附近的wifi密码
'''
import pywifi 
import time
import sys

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

profile = pywifi.Profile()
profile.ssid = '0000'
profile.auth = pywifi.const.AUTH_ALG_OPEN
profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
profile.key = '123456789'

tmp_profile = iface.add_network_profile(profile)
iface.remove_all_network_profiles()
iface.connect(tmp_profile)
time.sleep(15)
print(iface.status() == pywifi.const.IFACE_CONNECTED)

