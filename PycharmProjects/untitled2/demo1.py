from selenium import webdriver
import time
import requests
import urllib3
import os
from urllib import request
from bs4 import BeautifulSoup



urllib3.disable_warnings()



# ses= requests.Session()
# url = "https://iot-dev.huaweicloud.com/#/applications/mZjc8WNvcLU3AMMvaB3uXMbwl5sa/products/5f9a857f22768f094c74b224/device-debugger?from=online-test"
#
# headers = {
#     'Content-Type': 'application/json',
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
#     'Cookie' : 'sid=104937f4365ac5e9ad08993c857030bc582d3923427bae967793419551bcbcc58c2dc917ea1c36d63713; _ga=GA1.2.980483325.1604908725; _gid=GA1.2.258401325.1604908725; vk=25d48cff-2ce3-4d7d-85f3-e558e8d73440; ua=07669a8cf20010d60fd9c00688077ec0; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; SessionID=02da7672-fc52-45f8-9fa0-562de270fb27; ad_tm=; ad_sc=; ad_mdm=; ad_ctt=; ad_cmp=; ad_adp=; cf=Direct; domain_tag=07669a8cf20010d60fd9c00688077ec0; user_tag=07669a8e0b80251b1f3dc00623e1044e; masked_domain=h****22987; masked_user=h****22987; masked_phone=187****6557; usite=cn; popup_max_time=60; x-framework-ob=""; Hm_lvt_e54a2fc4480e89d897e7b3c1c4dfe648=1604908774,1604913699,1605007085,1605057851; IOIAS_JSESSIONID=66c8183e-63fc-4170-b069-a3cb781743a3; locale=zh-cn; __ozlvd1791=1605081795; IOBPS_JSESSIONID=275cea02-f752-4883-a28e-f9f5992d3c84; NSSL_JSESSIONID=e56eee14-e727-4a17-956d-d6583fb6a663; TGC="eyJhbGciOiJIUzUxMiJ9.ZXlKNmFYQWlPaUpFUlVZaUxDSmhiR2NpT2lKa2FYSWlMQ0psYm1NaU9pSkJNVEk0UTBKRExVaFRNalUySW4wLi5iYjlaVHg5Y2JXT0lUS2pMUWNkNlZRLmlxUzQyTURVaFpCbDdMSFd5dzlXVmpKblNpNTBzNW5Bd0lkenpwd1NkQVJEcHdpdWVJcWlPTUtteHpGTG50VGQ1MVVXS2NhYU8wOFFsbW9rcFZPcGVVQS1iay10ZFJZMFVTQmJ6NWwySEU5MkhaeG1adDBMVXFQMFF0NHRQU19EOXI2a2c2WlpWVU9lNUVqMWVBU0xqbVpBakQ2YTZmdTFPVjBkVzlPeVZZU2dLM0twWkgwMDFWRTNVbHNSalBUY2JEMFZVa1loNU9lUk9qSmVFcTlVQnlRYW51WEM5bGM1LTlDS0p4akVCRVN5WjNoNlRHLUtxYjh4VGRlVUVVQkZqdk5EX1gzaXhCaHpLOE50UTdDak5RLnEzbkxMY0hYeWVoa1lNVTI5TVFuREE=.mAqLTzjYnfitirV8RMhg3Q1hzGy0nSnO0C37W9nrtAy1q60lckagzoRC1jrTh3qU9dbaHoq5Z2iTWTPNDbdaOA"; JSESSIONID=96ACDBDD59F9A437CA1C800A2D0392E0; Hm_lpvt_e54a2fc4480e89d897e7b3c1c4dfe648=1605081815'}
#
# res = ses.get(url,headers=headers,verify=False)
# res.encoding = 'gb2312'
# # time.sleep(20)
# print(res.text)

# python抓取网页源码时，打印的源码不解析，哪位大神有解决办法呀，还说让使用google浏览器   ,phcram和电脑默认的浏览器已修改了，还是不行






# url = "https://iot-dev.huaweicloud.com/#/applications/mZjc8WNvcLU3AMMvaB3uXMbwl5sa/products/5f9a857f22768f094c74b224/device-debugger?from=online-test"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
#     'Cookie': 'sid=104937f4365ac5e9ad08993c857030bc582d3923427bae967793419551bcbcc58c2dc917ea1c36d63713; _ga=GA1.2.980483325.1604908725; _gid=GA1.2.258401325.1604908725; vk=25d48cff-2ce3-4d7d-85f3-e558e8d73440; ua=07669a8cf20010d60fd9c00688077ec0; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; SessionID=02da7672-fc52-45f8-9fa0-562de270fb27; ad_tm=; ad_ctt=; ad_cmp=; ad_mdm=; ad_sc=; ad_adp=; cf=Direct; domain_tag=07669a8cf20010d60fd9c00688077ec0; user_tag=07669a8e0b80251b1f3dc00623e1044e; masked_domain=h****22987; masked_user=h****22987; masked_phone=187****6557; usite=cn; popup_max_time=60; x-framework-ob=""; Hm_lvt_e54a2fc4480e89d897e7b3c1c4dfe648=1604908774,1604913699; locale=zh-cn; __ozlvd1791=1604972925; IOBPS_JSESSIONID=055a5f4f-6a87-47a0-9e1b-a8c03ee8f313; TGC="eyJhbGciOiJIUzUxMiJ9.ZXlKNmFYQWlPaUpFUlVZaUxDSmhiR2NpT2lKa2FYSWlMQ0psYm1NaU9pSkJNVEk0UTBKRExVaFRNalUySW4wLi4yYW5oTzhsUkQyaERCNlZ5SVJXa3JRLk5KYkREck9HUDhSd1dHSFYycnAyRzZseVFQbXNvRmkwLTVFQ2ZsRHN1UXUzdVhZeUlEbUVUcHB0MGw5UzVyVWtQeEZXSjA5Tmhsd3Z1T0hIV2syZEwyT0J6a2c2VGR5RThuSmN0LU45ZEU2VEdTTlN2RWlxX21YNk9OZUxPR3VFU25jY2tySTE4M0dzQU1PYkZUUlRMd05ZeEU2YWNQNUF4cUlLTV95NEpXX2U5cHBDUkdObVNPVEpVQ3BnNGRjamlhelVWOG4xU1prU0p6TVdEcmNIemM5X2tCVzllUkJmTEZRNUphZjJkMGNKZzhhb1RaMkdHX1Z2SEh0eEN6eGNWN2Y5WklvYTNaVmozX2E0QzZuWWJ3LjR4bDZpTzZ3c3ZCNFJ0aDB0NWJtYVE=.RNA-3FNzZWW19CTnN4Y9rbMP_fHNrgz1DRGYLQICbEf4xt6PfG7QzJcNwMUUrTDnnok5w4R6Dz5N8LhJyDJ7gQ"; IOIAS_JSESSIONID=dde32ab8-3504-4f31-b33c-3b8dee51d507; NSSL_JSESSIONID=adeb6d5f-fca9-4d4d-91f0-86124ceea648; JSESSIONID=796EC28F7AE3EA59DBFD41F10ED9BCF5; Hm_lpvt_e54a2fc4480e89d897e7b3c1c4dfe648=1604985316'}
#
#
# req = requests.Request(url, headers=headers)
# #
# rsp = requests.urlopen
# html = requests.get(url)
# print(html.text)










url = "https://iot-dev.huaweicloud.com/#/applications/mZjc8WNvcLU3AMMvaB3uXMbwl5sa/products/5f9a857f22768f094c74b224/device-debugger?from=online-test"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
    'Cookie': 'sid=104937f4365ac5e9ad08993c857030bc582d3923427bae967793419551bcbcc58c2dc917ea1c36d63713; _ga=GA1.2.980483325.1604908725; _gid=GA1.2.258401325.1604908725; vk=25d48cff-2ce3-4d7d-85f3-e558e8d73440; ua=07669a8cf20010d60fd9c00688077ec0; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; domain_tag=07669a8cf20010d60fd9c00688077ec0; user_tag=07669a8e0b80251b1f3dc00623e1044e; masked_domain=h****22987; masked_user=h****22987; masked_phone=187****6557; usite=cn; popup_max_time=60; x-framework-ob=""; ad_sc=; ad_mdm=; SessionID=1455b94f-94b9-4202-af2b-ff60d7c62fbe; ad_tm=; ad_ctt=; ad_cmp=; ad_adp=; cf=Direct; Hm_lvt_e54a2fc4480e89d897e7b3c1c4dfe648=1605057851,1605088134,1605088388,1605147271; IOIAS_JSESSIONID=8e4fde81-65f0-4455-a030-698c17cf364d; locale=zh-cn; __ozlvd1791=1605162497; IOBPS_JSESSIONID=5025dedf-116f-4bb6-9cd3-5bb1af4120e8; NSSL_JSESSIONID=fe44067f-beda-4382-86d4-9a9c07fd97a2; TGC="eyJhbGciOiJIUzUxMiJ9.ZXlKNmFYQWlPaUpFUlVZaUxDSmhiR2NpT2lKa2FYSWlMQ0psYm1NaU9pSkJNVEk0UTBKRExVaFRNalUySW4wLi5zejdHSkNpMXVIUHFKdEpjNDQtWVVBLkppM2ZodktvX3RsWnpGVGQtU1BSU0tPVUUwcFNoUWpLUnB3Z3ZMMHNoSThCOWlXb09iWmNmZjY1SmlIUThSbFNodzN2UjhxZmQ0Ul93OUduUHNqbk1Tb2I2ZzFNX2p4Z1djV0FQRkFHVjcyNVJxWGVMYXptbWlDU1RQdWd2Tmt5WWFCMFNPN2pwRW5SQVZlWEFPd3l6czYteDkxcnV3WjcxenVkSElDTG9YazhpTlBHR1FWY2prVEhQN25ENDIyVEZhcVB4MUhmamkwZHk0N29YLTJXd2lxdFE1dzYxcG5vdk1laTlydm9CQ25jaVVqbHZPc1N5OGV3MkRoOU1hUmJydVY1ZkpqeWU5eTVuNUtPeXZRMEtBLkdNNHlOUGNQYXFVMmw1d3RyT2RTUWc=.mGDEYNZkH32JlDKnJ6M6MBuIA25nglA2J0nxybVlbv85zYUjx_2B0u-z7QeKzm18X1PhZLcjIxR2U7CP4C2qGw"; JSESSIONID=D382FB3695F505FC03F7783232D86F72; Hm_lpvt_e54a2fc4480e89d897e7b3c1c4dfe648=1605162879'}
req = request.Request(url, headers=headers)
#
rsp = request.urlopen(req)
html = rsp.read().decode()
print(html)

print('*************************************************************************************************')

soup = BeautifulSoup(html, 'lxml')
print(soup.titlt)
# print(soup.p)
# print(soup.p.b)
print(len(soup.find_all('div', calss_='ng-star-inserted')))

# print(soup.find_all('head'))





# o = open("printHtml", "a", encoding="utf-8")
# o.write(res.text)
# o.close()
