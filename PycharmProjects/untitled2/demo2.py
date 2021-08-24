from selenium import webdriver
from bs4 import BeautifulSoup
import time



url = "https://iot-dev.huaweicloud.com/#/developer-overview"

driver = webdriver.Chrome(executable_path="C:\\Users\\letswin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")

res = driver.get(url)
driver.set_window_size(1000,800)

time.sleep(3)
# driver.set_window_size(1000,800)

# print(res)
# ele = driver.find_element_by_link_text("华为云帐号")
ele = driver.find_element_by_xpath('//*[@id="HWAccount"]/span')
ele.click()
time.sleep(3)

ele = driver.find_element_by_xpath('//*[@id="typeSwitchBtn"]')
ele.click()
time.sleep(2)

ele = driver.find_element_by_xpath('//*[@id="mobileInputId"]/input')
ele.send_keys("18702056557")
time.sleep(1)

ele = driver.find_element_by_xpath('//*[@id="mobilePasswordInputId"]/input')
ele.send_keys("letswin666!")
time.sleep(1)
# 登录
ele = driver.find_element_by_xpath('//*[@id="btn_submit"]')
ele.click()
time.sleep(10)

# 点击最近开发的产品
ele = driver.find_element_by_xpath('/html/body/app/pages/div/div/div/developer-overview/div/div[2]/div[1]/div/div[1]/div[2]/div/ul/li/div[2]/div/img')
ele.click()
time.sleep(10)


# 进入产品的收发数据页面
# ele = driver.find_element_by_xpath('/html/body/app/pages/div/div/div/applications/main/section/products/product-development/div/div[2]/div[3]/div/online-test/div/div[2]/div/table/tbody/tr[2]')
# ele = driver.find_element_by_xpath('/html/body/app/pages/div/div/div/applications/main/section/products/product-development/div/div[2]/div[3]/div/online-test/div/div[2]/div/table/tbody/tr[2]/td[3]/span')
ele = driver.find_element_by_xpath('/html/body/app/pages/div/div/div/applications/main/section/products/product-development/div/div[2]/div[3]/div/online-test/div/div[2]/div/table/tbody/tr[3]/td[3]/span')

ele.click()
# driver.close()
time.sleep(10)

# elea = driver.find_element_by_class_name('ng-star-inserted')
# print(len(elea.text))
# print(elea.text)

time.sleep(30)
eleTime = driver.find_elements_by_class_name("logTime")
time.sleep(5)
cont = len(eleTime)
# print(len(eleTime))
# print(type(eleTime))
# print(eleTime)
# print(type(cont))

# i = 0
# while i < 1000:
#     eleTimes = driver.find_elements_by_class_name("logTime")[i]
#     print(i)
#     print(eleTimes)
#     print(eleTimes.text)
#
#     i = i+1
#     time.sleep(10)
eleTimeValu = driver.find_elements_by_class_name("logTime")[(cont - 1)].text
eleLogValu = driver.find_elements_by_class_name("prepLog")[(cont - 1)].text
print(eleTimeValu)
print(eleLogValu)
print("********************************************************")
STR1 = eleTimeValu+eleLogValu
print(eleTimeValu+eleLogValu)
print("@2009399")

print("********************************************************")
STR2 = STR1[6:25]
STR3 = STR1[56:59]

print(STR2)
print(STR3)




# print(len(eleLog)-1)


# print(eleLog[len(eleLog)-1].text)

# eleTimeStr = "".join(eleTime)
# print(eleTimeStr)
#
# eleLog = driver.find_elements_by_class_name("prepLog")
# print(len(eleLog))
# eleLogStr = "".join(eleLog)
# print(eleLogStr)


# eleTime = driver.find_element_by_xpath("//p[@class='logTime']")
# # print(len(eleTime))
# print(type(eleTime))
# print(eleTime.text)
# eleTimeStr = "".join(eleTime)
# print(eleTimeStr)

# eleLog = driver.find_elements_by_class_name("prepLog")
# print(len(eleLog))
# eleLogStr = "".join(eleLog)
# print(eleLogStr)

# i = 0
# while i < 50:
#     eleTime = driver.find_element_by_class_name("logTime")
#     print(eleTime.text)
#     eleLog = driver.find_element_by_class_name("prepLog")
#     print(eleLog.text)
#     time.sleep(0.5)
#     i = i+1
# driver.close()