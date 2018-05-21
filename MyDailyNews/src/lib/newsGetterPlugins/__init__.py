print("数据的获取爬虫")

#selenium的使用
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#  
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# elem = driver.find_element_by_id("kw")
# elem.send_keys("selenium")
# elem.send_keys(Keys.RETURN)
# print (driver.page_source)
# # driver.close()

#爬虫的登录

# import requests
#  
# params = {'username': 'XXXX', 'password': 'password'}
# s = requests.Session()
# s.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
# r = s.get("http://pythonscraping.com/pages/cookies/profile.php")
# # r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
# # print("Cookie is set to:")
# # print(r.cookies.get_dict())
# # print("-----------")
# # print("Going to profile page...")
# # r = requests.get("http://pythonscraping.com/pages/cookies/profile.php",
# #                  cookies=r.cookies)
# print(r.text)