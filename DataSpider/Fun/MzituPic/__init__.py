import requests
import time

proxylist = (
            '123.134.185.11',
            '115.228.107.142',
            '180.76.135.145',
            '58.218.198.61',
            '110.72.43.148',
            )

url = 'https://answers.microsoft.com/zh-hans/windows/forum/apps_windows_10-msedge/edge%E5%AF%B9qpub%E7%94%B5%E5%AD%90%E4%B9%A6/3f25068e-bd2a-4b11-8099-2051ce32b1ea?tm=1501140941092'
while True:
    for proxy in proxylist:
        proxies = {'': proxy}
        print(requests.get(url, proxies=proxies).status_code)
        time.sleep(5)
        time.sleep(0)
        
print("一个可以把mzitu.com上所有图片都下载下来的小程序")
