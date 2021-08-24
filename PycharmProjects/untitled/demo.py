# import os
#
# def test_arg(f_arg,*args):
#     print(f_arg)
#     for n in  args:
#
#         print(n)
# def test_kwargs(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
# if __name__ == '__main__':
#     # test_arg("参数1","参数2")
#     test_kwargs(name = "cehi1")

import requests

html = requests.get(
    "https://iot-dev.huaweicloud.com/#/applications/mZjc8WNvcLU3AMMvaB3uXMbwl5sa/products/5f9a857f22768f094c74b224/device-debugger?from=online-test")
print(html)
o = open("printHtml", "a", encoding="utf-8")
o.write(html)
o.close()
