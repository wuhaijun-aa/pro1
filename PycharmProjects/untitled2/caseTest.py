import os
import sys
import unittest
from pathlib import Path
import serial
import time
from selenium import webdriver
import  numbers
import requests

name = os.path.basename(sys.argv[0]).replace(".py", "")
print(name)
newPath = Path("D:test\\test")

str = ""
def getbate():
    i = 0

    redata = []
    while i < 2:

        count = ser.inWaiting()
        if count != 0:
            # resv = ser.read(count).decode("utf-8")
            resv = ser.read(count)
            # print("======")
            # print(resv)
            # print("======")
            resv = str(resv)
            redata.append(resv)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ";  输出打印" + resv)
            time.sleep(0.01)
        i = i + 1
    fialData = ''.join(redata)
    # 防止出现b'\r\nO'b'K\r\n'
    if "O'b'K" in fialData:
        fialData = fialData + "OK"
    return fialData


# 创建保存文件，如果不存在则创建路径
def creatTest():
    global f
    textneam = time.strftime("%Y%m%d%H%M%S",time.localtime())+name+'txt'
    #  检查保存路径是否存在
    if newPath.exists():
        orgpath = os.chdir(r"d:\\test\\test")

        f = open(textneam,'a',encoding='utf-8')
    else:
        os.makedirs(r"d:\\test\\test")
        orgpath = os.chdir(r"d:\\test\\test")
        # global f
        f = open(textneam, 'a', encoding='utf-8')

''' 
获取华为云网站的数据，用于判断UE命令是否发送上去
'''
def getWebData():
    # 获取华为云的URL
    url = "https://iot-dev.huaweicloud.com/#/developer-overview"
    # 启动模拟浏览器
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\letswin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
    # 传入地址
    res = driver.get(url)
    driver.set_window_size(1000, 800)
    # 等待浏览器的刷新
    time.sleep(3)
    # 点击"华为云"
    ele = driver.find_element_by_xpath('//*[@id="HWAccount"]/span')
    ele.click()
    time.sleep(3)
    # 点击"手机号登录"
    ele = driver.find_element_by_xpath('//*[@id="typeSwitchBtn"]')
    ele.click()
    time.sleep(2)
    # 输入手机号
    ele = driver.find_element_by_xpath('//*[@id="mobileInputId"]/input')
    ele.send_keys("18702056557")
    time.sleep(1)
    # 输入密码
    ele = driver.find_element_by_xpath('//*[@id="mobilePasswordInputId"]/input')
    ele.send_keys("letswin666!")
    time.sleep(1)
    # 登录
    ele = driver.find_element_by_xpath('//*[@id="btn_submit"]')
    ele.click()
    time.sleep(10)

    # 点击最近开发的产品
    ele = driver.find_element_by_xpath(
        '/html/body/app/pages/div/div/div/developer-overview/div/div[2]/div[1]/div/div[1]/div[2]/div/ul/li/div[2]/div/img')
    ele.click()
    time.sleep(10)
    # 点击对应的产品
    ele = driver.find_element_by_xpath(
        '/html/body/app/pages/div/div/div/applications/main/section/products/product-development/div/div[2]/div[3]/div/online-test/div/div[2]/div/table/tbody/tr[3]/td[3]/span')

    ele.click()
    # driver.close()
    time.sleep(10)

    time.sleep(30)
    eleTime = driver.find_elements_by_class_name("logTime")
    time.sleep(5)
    cont = len(eleTime)
    # print(len(eleTime))
    # print(type(eleTime))
    # print(eleTime)
    # print(type(cont))

    eleTimeValu = driver.find_elements_by_class_name("logTime")[(cont - 1)].text
    eleLogValu = driver.find_elements_by_class_name("prepLog")[(cont - 1)].text
    print(eleTimeValu)
    print(eleLogValu)
    return eleTimeValu+eleLogValu

    pass










def serPort():
    global ser
    ser = serial.Serial(port="com",baudrate=9600,timeout=5)



class caseTest(unittest.TestCase):
    # def __init__(self,name):
    #      self.name = os.path.basename(sys.argv[0].replace(".py",""))
    #      # self.namepath = Path("d:\\test\\test")
    #      pass
    def setUp(self) -> None:
        # self.ser = serial.Serial(port="COM6",baudrate=9600,timeout=5)
        # self.ser.flush()
        pass
    def tearDown(self) -> None:
        pass

    def creaText(self):
        print("cera")

    '''
    测试目的：模组发送的数据，云平台接收，并且验证数据的准确性
    用力步骤：
        1、创建SER端口对象，将UE的端口号和波特率传入
        ２、清空端口内的缓存数据
        ３、创建发送的数据
        ４、发送数据
        ５、获取网页云平台和端口返回的数据
        ６、判断条件：（１）端口返回ＯＫ，（２）云平台数据接收的时间和发送时间接近（３）云平台的接收的数据和发送的数据一致
    '''
    def test_coap(self):
        try:
            global ser
            ser = serial.Serial(port="COM3", baudrate=9600, timeout=5)
            ser.flushInput()
            # str = "AT+NMGS=3,002300"
            str = "AT+COAPSEND=007800,3"
            creatTest()
            m = 0
            while m < 1:
                print("第{}次循环".format(m+1))
                startTime = int(time.time())
                print(startTime)
                ser.write(bytes(str+"\r\n",encoding="utf-8"))
                f.write("输入:"+str)
                print("输入:"+str)
                time.sleep(1)
                print("等待1s")
                s =getbate()

                print(s)
                self.assertIn("OK", s, msg="通信失败")
                # if "ERROR" in s:
                #     break



                # 获取网页抓取的数据:例如:命令发送: 2020/11/14 14:34:43 GMT+08:00命令状态:超时
                webStr = getWebData()
                # 截取时间字符串并按字符串格式转换成元组,在强转换成整型S的单位
                endtime = int(time.mktime(time.strptime(webStr[6:25],"%Y/%m/%d %H:%M:%S")))
                print(endtime)
                # 判断网页时间在实际下发命令的2min之内
                self.assertFalse(endtime > (startTime+120), msg="上报时间超过2min")
                self.assertTrue(endtime+10 >= startTime, msg="华为云上还未上报{}命令".format(str))

                # if 120 < (endtime - startTime) or (endtime - startTime) < 0:
                #     print("网页数据不存在此次发送的数据,请检查")
                #     break
                # 获取上报的数据内容
                exprStr = webStr[56:59]
                print(exprStr)
                self.assertEqual("120", exprStr, msg="还未上报{}命令".format(str))

                m = m + 1
        finally:
            ser.close()
            f.close()



    def test_atCfun(self):
        try:
            global ser
            ser = serial.Serial(port="COM6", baudrate=9600, timeout=5)
            ser.flushInput()

            m = 0
            while m < 1000:
                str = "AT+CFUN=0"
                print("第{}次循环".format(m+1))

                ser.write(bytes(str+"\r\n", encoding="utf-8"))
                print("输入:"+str)
                time.sleep(10)
                print("等待10s")
                s =getbate()

                print(s)
                self.assertIn("OK", s, msg="通信失败")
                if "OK" not in s:
                    break
                m = m + 1
        finally:
            ser.close()

    '''
    类别：AT命令
    序号：TC_0000_0001
    测试场景：UE上电测试帮助指令
    测试步骤：1、UE上电下发AT+HELP
    测试预期：返回74个AT指令
    '''
    def test_TC_0000_0001(self):
        global ser
        try:
            ser = serial.Serial(port="COM",baudrate=9600,timeout=5)
            ser.flushInput()
            str = "AT+HELP"
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+ "  输入打印 "+str)
            ser.write(bytes(str+"\r\n", encoding="utf-8"))

            s = getbate()
            n = s.count("AT")/2
            self.assertEqual (72,n,msg="AT命令个数是{}个，和预期不相等".format(n))
        finally:
            ser.close()


    '''
    类别：AT命令
    序号：TC_0000_0002
    测试场景：UE上电测试查询制造商名称指令
    测试步骤：1、上电后下发AT+CGMI
    测试预期：1、返回OK
            2、返回制造商名称和预期一致
            
    '''
    def test_TC_0000_0002(self):
        try:
            # global ser
            # ser = serial.Serial(port="com",)
            str = 'AT+CGMI'

            serPort()

            ser.flushInput()

            ser.write(bytes(str+'\r\n', encoding='utf-8'))

            time.sleep(3)

            data = getbate()




        finally:
            ser.close()


if __name__ == '__main__':



    unittest.main()

