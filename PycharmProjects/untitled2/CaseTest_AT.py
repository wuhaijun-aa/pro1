import os
import sys
import unittest
from pathlib import Path
import serial
import time
import re
import datetime
from selenium import webdriver
import numbers
import requests

import logging

name = os.path.basename(sys.argv[0]).replace(".py", "")
print(name)
newPath = Path("D:test\\test")


'''
设置logging的输出格式
'''
# logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler(time.strftime("%Y%m%d%H%M%S", time.localtime())+name+".txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(funcName)s-%(lineno)d- %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(console)




def getbate(ser):
    i = 0

    redata = []
    while i < 2:

        count = ser.inWaiting()
        if count != 0:
            # resv = ser.read(count).decode("utf-8")
            resv = ser.read(count)
            logger.info("=============-----------------------------=================")
            # logger.info(resv)
            # logger.info("======")
            # logger.info(type(resv))
            resv = str(resv)
            redata.append(resv)
            logger.info("输出打印" + resv)
            time.sleep(0.01)
        i = i + 1
    fialData = ''.join(redata)

    # 防止出现b'\r\nO'b'K\r\n'
    if "O'b'K" in fialData:
        fialData = fialData + "OK"

    logger.info(fialData)
    return fialData
# def senAndrec(str0,ser):
#     logger.info("输入命令： " + str0)
#     ser.write(bytes(str0 + "\r\n", encoding='utf-8'))
#     time.sleep(3)
#     logger.info("等待3s")
#     data = getbate(ser)
#
#     data = data.strip("b'")
#     data = data.strip("\\r\\n")
#
#     return data

def senAndrec(str0,ser,T=3):
    logger.info("输入命令： " + str0)
    ser.write(bytes(str0 + "\r\n", encoding='utf-8'))
    time.sleep(T)
    logger.info("等待{}s".format(T))
    data = getbate(ser)

    data = data.strip("b'")
    data = data.strip("\\r\\n")

    return data

class caseTest(unittest.TestCase):
    # def __init__(self,name):
    #      self.name = os.path.basename(sys.argv[0].replace(".py",""))
    #      # self.namepath = Path("d:\\test\\test")
    #      pass
    def setUp(self) -> None:
        self.ser = serial.Serial(port="COM3", baudrate=9600, timeout=5)
        self.ser.flushInput()
        logger.info("------------------>setUp(self)")


    def tearDown(self) -> None:
        self.ser.close()
        logger.info("--------------->tearDown(self)")
    '''
    类别：AT命令
    序号：TC_0001_0001
    测试场景：UE上电压测UE入网
    测试步骤：1、UE上电下发AT+CFUN=1
            2、获取入网IP
            3、下发AT+CFUN=0
            4、循环1~3 200次
    测试预期：1、返回OK
            2、返回IP地址，OK
            3、返回OK
    '''
    def test_TC_0001_0001(self):
        # global ser
        # TIMES = 0
        try:
            # ser = serial.Serial(port="COM3", baudrate=9600, timeout=5)
            # ser.flushInput()
            str0 = "AT+CFUN=0"
            str1 = "AT+CFUN=1"
            str2 = "AT+CGPADDR"
            m = 0
            while m < 5000:
                logger.info("第{}次循环".format(m + 1))
                logger.info("第{}次循环".format(m + 1))
                logger.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                logger.info("输入:" + str1)
                self.ser.write(bytes(str1 + "\r\n", encoding="utf-8"))
                time.sleep(3)

                while ('OK' not in getbate(self.ser)):
                    logger.info("未开机，等待2s")
                    time.sleep(2)

                while ('ADDR' not in getbate(self.ser)):
                    logger.info("未入网，等待1s")
                    time.sleep(3)

                    logger.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                    logger.info("输入:" + str2)
                    self.ser.write(bytes(str2 + "\r\n", encoding="utf-8"))
                    time.sleep(1)
                    data1 = getbate(self.ser)
                    while ('OK' not in data1):
                        logger.info("CGPADDR未返回OK，等待1s")
                        time.sleep(1)
                        data1 = getbate(self.ser)
                    if 'ADDR' in data1:
                        logger.info("IP地址以获取到，已入网")
                        break
                    time.sleep(1)

                logger.info("等待1s")
                logger.info('已入网，\n下面关机')
                time.sleep(1)

                logger.info("第{}次循环".format(m + 1))
                # logger.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                logger.info("关机:" + str0)
                self.ser.write(bytes(str0 + "\r\n", encoding="utf-8"))
                time.sleep(1.5)
                logger.info("等待1.5s")

                while ('OK' not in getbate(self.ser)):
                    logger.info("未关机，等待2s")

                    time.sleep(2)

                time.sleep(5)
                m = m + 1
        finally:
            logger.info("----------------->finally")


    '''
       类别：AT命令
       序号：TC_0000_0001
       测试场景：UE上电测试帮助指令
       测试步骤：1、UE上电下发AT+HELP
       测试预期：返回74个AT指令
       '''

    def test_TC_0000_0001(self):
        # global ser
        try:
            str0 = "AT+HELP"
            logger.info("输入打印 " + str0)
            self.ser.flushInput()
            self.ser.write(bytes(str0 + "\r\n", encoding="utf-8"))
            time.sleep(0.05)
            logger.info("等待10s")
            s = getbate(self.ser)
            while ('OK' not in s):
                logger.info("AT+HELP 未返回OK，等待5s")
                time.sleep(5)
                s = getbate(self.ser)+s

            n = int(s.count("AT"))
            self.assertEqual(35, n, logger.info(msg="AT命令个数是{}个，和预期指令个数{}".format(n, 35)))
        finally:
            pass


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
            str0 = 'AT+CGMI'
            logger.info("输入命令："+str0)
            self.ser.write(bytes(str0+'\r\n', encoding="UTF-8"))

            time.sleep(2)
            logger.info("等待2s")

            data = getbate(self.ser)

            while ("OK" not in data):
                logger.info("AT+CGMI 未返回OK，等待2s")
                time.sleep(2)
                data = getbate(self.ser)
            self.assertIn("+CGMI:LETSWIN", data, msg="判断失败")

        finally:
            pass

    '''
       类别：AT命令
       序号：TC_0000_0003
       测试场景：UE上电测试查询模块型号指令
       测试步骤：1、上电后下发AT+CGMM=？
               2、下发AT+CGMM
       测试预期：1、返回OK
               2、返回制造商名称和预期一致，返回OK
    
       '''
    def test_TC_0000_0003(self):
        str0 = "AT+CGMM=?"
        str1 = "AT+CGMM"
        logger.info("输入命令："+str0)
        self.ser.write(bytes(str0 + "\r\n", encoding='utf-8'))
        time.sleep(3)
        logger.info("等待3s")
        data = getbate(self.ser)
        # while "OK" not in data:
        #     time.sleep(2)
        #     logger.info("未返回OK，等待2s")
        data = data.strip("b'")
        data = data.strip("\\r\\n")
        logger.info(data)
        self.assertEqual("OK", data, msg="返回的参数值是"+data+"和预期不相符")

        self.ser.write(bytes(str1+"\r\n", encoding='utf-8'))
        time.sleep(3)
        logger.info("等待3s")
        data = getbate(self.ser)
        self.assertIn("+CGMM:LZ800", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("OK", data,msg="返回值{}与预期不符".format(data))

    '''
           类别：AT命令
           序号：TC_0000_0004
           测试场景：UE上电测试查询模块型号指令
           测试步骤：1、上电后下发AT+CGMR=？
                   2、下发AT+CGMR
           测试预期：1、返回OK
                   2、返回模块型号和预期一致，返回OK

           '''

    def test_TC_0000_0004(self):
        str0 = "AT+CGMR=?"
        str1 = "AT+CGMR"
        logger.info("输入命令：" + str0)
        self.ser.write(bytes(str0 + "\r\n", encoding='utf-8'))
        time.sleep(3)
        logger.info("等待3s")
        data = getbate(self.ser)
        # while "OK" not in data:
        #     time.sleep(2)
        #     logger.info("未返回OK，等待2s")
        data = data.strip("b'")
        data = data.strip("\\r\\n")
        logger.info(data)
        self.assertEqual("OK", data, msg="返回的参数值是" + data + "和预期不相符")

        self.ser.write(bytes(str1 + "\r\n", encoding='utf-8'))
        time.sleep(3)
        logger.info("等待3s")
        data = getbate(self.ser)
        self.assertIn("+CGMR:0.1.0", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

    def test_TC_0000_0005(self):
        str0 = "AT+CGSN"
        logger.info("输入命令：" + str0)
        self.ser.write(bytes(str0 + "\r\n", encoding='utf-8'))
        time.sleep(3)
        logger.info("等待3s")
        data = getbate(self.ser)

        data = data.strip("b'")
        logger.info(data)

        data = data.strip("\\r\\n")
        logger.info(data)
        '''
        不加.string  返回值为下面
        2021-02-20 14:37:04,296 - CaseTest_AT - INFO -test_TC_0000_0005-298- <re.Match object; span=(1, 16), match='000000000000000'>
        <re.Match object; span=(1, 16), match='000000000000000'>
        '''
        reData = re.search("[a-zA-Z0-9]{15}", data).string
        logger.info(reData)
        print(reData)
        self.assertIn(reData, data, msg="CGSN返回值与预期不相符{}与预期不符".format(data))
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

    def test_TC_0000_0006(self):
        str0 = "AT+FWVER"
        logger.info("输入命令：" + str0)
        self.ser.write(bytes(str0 + "\r\n", encoding='utf-8'))
        time.sleep(3)
        logger.info("等待3s")
        data = getbate(self.ser)

        data = data.strip("b'")
        data = data.strip("\\r\\n")

        self.assertIn("+FWVER:0.1.0", data, msg="FWVER返回值{}与预期不符".format(data))
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

    def test_TC_0000_0007(self):
        str0 = "AT+SYSTIME"
        logger.info("输入命令：" + str0)
        self.ser.write(bytes(str0 + "\r\n", encoding='utf-8'))
        time.sleep(2)
        # time1 = time.strftime("%Y/%m/%d,%H:%M", time.localtime())
        # logger.info(time1)
        print("*********************************************8")
        time1 = datetime.datetime.now().timetuple()
        time1Info = str(time1.tm_year) + "/" + str(time1.tm_mon) + "/" + str(time1.tm_mday) + "," + str(
            time1.tm_hour) + ":" + str(time1.tm_min)
        logger.info(time1Info)
        time.sleep(1)
        logger.info("等待3s")
        data = getbate(self.ser)
        self.assertIn(time1Info, data, msg="SYSTIME返回值{}与预期不符".format(data))
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

    def test_TC_0000_0008(self):
        str0 = "AT+CIMI"
        logger.info("输入命令：" + str0)
        self.ser.write(bytes(str0 + "\r\n", encoding='utf-8'))
        time.sleep(3)
        logger.info("等待3s")
        data = getbate(self.ser)
        reData = re.search("[0-9]{15}", data).string
        logger.info(reData)
        self.assertIn(reData, data, msg="CIMI返回值与{}与预期不符".format(data))
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

    def test_TC_0000_0009(self):
        str0 = "AT+ICCID?"

        str1 = "AT+ICCID"
        logger.info("输入命令：" + str0)
        self.ser.write(bytes(str0 + "\r\n", encoding='utf-8'))
        time.sleep(3)
        logger.info("等待3s")
        data = getbate(self.ser)
        reData = re.search("[0-9]{20}", data).string
        logger.info(reData)


        self.assertIn(reData, data, msg="ICCID返回值与预期不相符{}与预期不符".format(data))
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str1)
        self.ser.write(bytes(str1 + "\r\n", encoding='utf-8'))
        time.sleep(3)
        logger.info("等待3s")
        data1 = getbate(self.ser)
        print("*****************")
        logger.info(data)
        logger.info(data1)
        self.assertEqual(data, data1, msg="ICCID返回值{}与预期不符".format(data1))

    def test_TC_0000_0010(self):
        str0 = "AT+CSIM=?"
        logger.info("输入命令： "+str0)
        self.ser.write(bytes(str0 + "\r\n", encoding='utf-8'))
        time.sleep(3)
        logger.info("等待3s")

        data = getbate(self.ser)

        data = data.strip("b'")
        data = data.strip("\\r\\n")
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

    def test_TC_0000_0011(self):
        str0 = "AT+CRSM=?"
        logger.info("输入命令： " + str0)
        self.ser.write(bytes(str0 + "\r\n", encoding='utf-8'))
        time.sleep(3)
        logger.info("等待3s")

        data = getbate(self.ser)

        data = data.strip("b'")
        data = data.strip("\\r\\n")
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))


    def test_TC_0000_0012(self):
        str0 = "AT+CFUN=0"
        str1 = "AT+CFUN=1"
        str2 = "AT+BAND=5"
        str3 = "AT+BAND=8"
        str4 = "AT+BAND?"
        i = 0
        while i<20:
            data = senAndrec(str0, self.ser)
            time.sleep(10)
            self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

            data = senAndrec(str2, self.ser)
            self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

            data = senAndrec(str1, self.ser)
            self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
            ##########################################

            data = senAndrec(str4, self.ser)
            self.assertIn("BAND:5", data, msg="返回值{}与预期不符".format(data))
            self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

            data = senAndrec(str0, self.ser)

            time.sleep(10)
            self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

            data = senAndrec(str3, self.ser)
            self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

            data = senAndrec(str1, self.ser)
            self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

            ####################################

            data = senAndrec(str4, self.ser)
            self.assertIn("BAND:8", data, msg="返回值{}与预期不符".format(data))
            self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

            data = senAndrec(str0, self.ser)
            time.sleep(10)
            self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

            data = senAndrec(str2, self.ser)
            self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

            data = senAndrec(str4, self.ser)
            self.assertIn("BAND:5", data, msg="返回值{}与预期不符".format(data))
            self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

            i = i + 1

    def test_TC_0000_0013(self):
        str0 = "AT+CFUN=0"
        str1 = "AT+CFUN=1"
        str2 = "AT+CGPADDR"
        str3 = "AT+CSNR"
        str4 = "AT+CGATT?"
        str5 = "AT+CGATT=0"
        str6 = "AT+CGATT=1"

        data = senAndrec(str0, self.ser,20)

        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        data = senAndrec(str1, self.ser)
        time.sleep(10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        time.sleep(60)
        data = senAndrec(str2, self.ser,60)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("ADDR", data, msg="开机120S未入网")

        data = senAndrec(str3, self.ser)
        time.sleep(10)
        self.assertIn("SNR", data, msg="返回值{}与预期不符".format(data))

        data = senAndrec(str4, self.ser)
        time.sleep(10)
        self.assertIn("+CGATT: 1",data, msg="返回值{}与预期不符".format(data))

        data = senAndrec(str5, self.ser)
        time.sleep(10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        data = senAndrec(str2, self.ser,120)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertNotIn("ADDR", data, msg="已入网，判决失败")

        data = senAndrec(str6, self.ser)
        time.sleep(10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        data = senAndrec(str2, self.ser)
        time.sleep(120)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("ADDR", data, msg="开机120S未入网")

        data = senAndrec(str0, self.ser,20)
        time.sleep(10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

    def test_TC_0000_0014(self):
        str0 = "AT+CFUN=0"
        str1 = "AT+CFUN=1"
        str2 = "AT+CGPADDR"
        str3 = "AT+CEREG=?"
        str4 = "AT+CEREG?"
        str5 = "AT+CEREG=0"
        str6 = "AT+CEREG=1"
        str7 = "AT+CEREG=2"
        str8 = "AT+CEREG=3"
        str9 = "AT+CEREG=4"
        str10 = "AT+CEREG=5"
        logger.info("输入命令： "+str0)
        data = senAndrec(str0, self.ser,20)

        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令： " + str1)
        data = senAndrec(str1, self.ser)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        time.sleep(60)
        logger.info("输入命令： " + str2)
        data = senAndrec(str2, self.ser,60)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("ADDR", data, msg="开机120S未入网")

        logger.info("输入命令： " + str3)
        data = senAndrec(str3, self.ser)
        self.assertIn("+CEREG: (0,1,2,3)", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令： " + str4)
        data = senAndrec(str4, self.ser)
        self.assertIn("+CEREG: 0,1", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令： " + str0)
        data = senAndrec(str0, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令： " + str4)
        data = senAndrec(str4, self.ser)
        self.assertIn("+CEREG: 0,0", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令： " + str1)
        data = senAndrec(str1, self.ser)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        time.sleep(60)
        logger.info("输入命令： " + str2)
        data = senAndrec(str2, self.ser, 60)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("ADDR", data, msg="开机120S未入网")

        data = senAndrec(str5, self.ser)
        time.sleep(10)
        self.assertIn("+CEREG: 0,1", data, msg="返回值{}与预期不符".format(data))

        data = senAndrec(str6, self.ser,120)
        self.assertIn("+CEREG: 1,1", data, msg="返回值{}与预期不符".format(data))


        data = senAndrec(str7, self.ser)

        self.assertIn("+CEREG: 2,1", data, msg="返回值{}与预期不符".format(data))

        data = senAndrec(str8, self.ser)

        self.assertIn("+CEREG: 3,1", data, msg="返回值{}与预期不符".format(data))

        data = senAndrec(str0, self.ser,20)
        time.sleep(10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

    def test_TC_0000_0015(self):
        str0 = "AT+SOCKET"


    def test_TC_0000_0016(self):
        str0 = "AT+CFUN=0"
        str1 = "AT+CFUN=1"
        str2 = "AT+SELFREG=0"
        str3 = "AT+REBOOT"
        str4 = "AT+SELFREG"
        str5 = "AT+SELFREG=1"
        str6 = "AT+CGPADDR"

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str2)
        data = senAndrec(str2, self.ser)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))


        logger.info("输入命令：" + str1)
        data = senAndrec(str1, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        time.sleep(60)
        logger.info("输入命令：" + str6)
        data = senAndrec(str6, self.ser, 60)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("ADDR", data, msg="开机120S未入网")

        logger.info("输入命令：" + str4)
        data = senAndrec(str4, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str5)
        data = senAndrec(str5, self.ser)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str1)
        data = senAndrec(str1, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        time.sleep(60)
        logger.info("输入命令：" + str6)
        data = senAndrec(str6, self.ser, 60)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("ADDR", data, msg="开机120S未入网")

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

    def test_TC_0000_0017(self):
        str0 = "AT+CFUN=0"
        str1 = "AT+CFUN=1"
        str2 = "AT+CGPADDR"
        str3 = "AT+PING=221.229.214.202"
        str4 = "AT+PING=10.11.11.11,60000,64,1"

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str1)
        data = senAndrec(str1, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        time.sleep(60)
        logger.info("输入命令：" + str2)
        data = senAndrec(str2, self.ser, 60)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("ADDR", data, msg="开机120S未入网")

        logger.info("输入命令：" + str3)
        data = senAndrec(str3, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str4)
        data = senAndrec(str4, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

    def test_TC_0000_0018(self):
        str0 = "AT+IMEI?"
        str1 = "AT+FLASHZERO"

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 10)
        # self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))


        send_date= data[0:14]

        logger.info("输入命令：" + str1)
        data = senAndrec(str1, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 10)
        self.assertIn("0000", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + "AT+IMEI="+send_date)
        data = senAndrec("AT+IMEI="+send_date, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 10)
        self.assertIn(send_date, data, msg="返回值{}与预期不符".format(data))
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

    def test_TC_0000_0019(self):
        str0 = "AT+CFUN=0"
        str1 = "AT+CFUN=1"
        str2 = "AT+CGPADDR"
        str3 = "AT+CSNR"

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str1)
        data = senAndrec(str1, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        time.sleep(60)
        logger.info("输入命令：" + str2)
        data = senAndrec(str2, self.ser, 60)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("ADDR", data, msg="开机120S未入网")

        logger.info("输入命令：" + str3)
        data = senAndrec(str3, self.ser, 10)
        logger.info(data[7:10])
        self.assertTrue(-100 < int(data[7:10]) <300, msg="返回值{}与预期不符".format(data))


    def test_TC_0000_0020(self):
        str0 = "AT+CFUN=0"
        str1 = "AT+CFUN=1"
        str2 = "AT+CGPADDR"


        str3 = "AT+SLEEP"

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str1)
        data = senAndrec(str1, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        time.sleep(60)
        logger.info("输入命令：" + str2)
        data = senAndrec(str2, self.ser, 60)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("ADDR", data, msg="开机120S未入网")

        logger.info("输入命令：" + str3)
        data = senAndrec(str3, self.ser, 10)

        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str1)
        data = senAndrec(str1, self.ser, 10)
        # self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

    def test_TC_0000_0021(self):
        str0 = "AT+ECHO=OFF"
        str1 = "AT+ECHO=ON"
        str2 = "AT+ECHO?"
        str3 = "AT+CGPADDR"
        str4 = "AT+BAND?"

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str2)
        data = senAndrec(str2, self.ser)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("+ECHO:OFF", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str3)
        data = senAndrec(str3, self.ser)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str4)
        data = senAndrec(str4, self.ser)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str1)
        data = senAndrec(str1, self.ser)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str2)
        data = senAndrec(str2, self.ser)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("+ECHO:ON", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str3)
        data = senAndrec(str3, self.ser)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn(str3, data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str4)
        data = senAndrec(str4, self.ser)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn(str4, data, msg="返回值{}与预期不符".format(data))

    def test_TC_0000_0022(self):
        str0 = "AT+EVENT"

    def test_TC_0000_0023(self):
        pass

    def test_C_0000_0024(self):
        str0 = "AT+CFUN=0"
        str1 = "AT+CFUN=1"
        str2 = "AT+CGPADDR"
        str3 = "AT+CGDCONT?"
        str4 = 'AT+CGDCONT=0,"IPV4V6","cmnet",,0,0,0,2,0,0,0,1,0,0,0'

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str3)
        data = senAndrec(str3, self.ser, 10)
        self.assertIn('0,"IPV4V6","cmnet",,0,0,0,2,0,0,0,1,0,0,0', data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str4)
        data = senAndrec(str4, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str1)
        data = senAndrec(str1, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        time.sleep(60)
        logger.info("输入命令：" + str2)
        data = senAndrec(str2, self.ser, 60)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("ADDR", data, msg="开机120S未入网")

    def test_C_0000_0025(self):
        str0 = "AT+CFUN=0"
        str1 = "AT+CFUN=1"
        str2 = "AT+CGPADDR"
        str3 = "AT+CESQ=?"
        str4 = "AT+CESQ"

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str1)
        data = senAndrec(str1, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        time.sleep(90)
        logger.info("输入命令：" + str2)
        data = senAndrec(str2, self.ser, 30)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("ADDR", data, msg="开机120S未入网")


        logger.info("输入命令：" + str3)
        data = senAndrec(str3, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("+CESQ", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str4)
        data = senAndrec(str4, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("+CESQ", data, msg="返回值{}与预期不符".format(data))

    def test_C_0000_0026(self):
        str0 = "AT+CFUN=0"
        str1 = "AT+CFUN=1"
        str2 = "AT+CGPADDR"
        str3 = "AT+CGDATA=?"
        str4 = "AT+CGDATA=PPP,0"

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str1)
        data = senAndrec(str1, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        time.sleep(90)
        logger.info("输入命令：" + str2)
        data = senAndrec(str2, self.ser, 30)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("ADDR", data, msg="开机120S未入网")

        logger.info("输入命令：" + str3)
        data = senAndrec(str3, self.ser, 10)
        self.assertIn("+CGDATA:(PPP)", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str4)
        data = senAndrec(str4, self.ser, 10)
        self.assertIn("CONNECT", data, msg="返回值{}与预期不符".format(data))
        # self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

    def test_C_0000_0027(self):
        pass

    def test_C_0000_0028(self):
        pass

    def test_C_0000_0029(self):
        str0 = "AT+CFUN=0"
        str1 = "AT+CFUN=1"
        str2 = "AT+CGPADDR"
        str3 = "AT+CGACT?"
        str4 = "AT+CGACT=0,0"
        str5 = "AT+CGACT=1,0"

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str1)
        data = senAndrec(str1, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        time.sleep(90)
        logger.info("输入命令：" + str2)
        data = senAndrec(str2, self.ser, 30)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("ADDR", data, msg="开机120S未入网")

        logger.info("输入命令：" + str3)
        data = senAndrec(str3, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("+CGACT:1,0", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str4)
        data = senAndrec(str4, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str3)
        data = senAndrec(str3, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("+CGACT:0,0", data, msg="返回值{}与预期不符".format(data))

    def test_C_0000_0030(self):
        str0 = "AT+CFUN=0"
        str1 = "AT+CFUN=1"
        str2 = "AT+CGPADDR"
        str3 = "AT+CEDRX?"

    def test_C_0000_0031(self):
        str0 = "AT+CFUN=0"
        str1 = "AT+CFUN=1"
        str2 = "AT+CGPADDR"
        str3 = "AT+CPSMS?"
        str4 = "AT+CPSMS=0"
        str5 = "AT+CPSMS=1,,,'10100010','00000110'"

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str1)
        data = senAndrec(str1, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        time.sleep(90)
        logger.info("输入命令：" + str2)
        data = senAndrec(str2, self.ser, 30)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("ADDR", data, msg="开机120S未入网")

        logger.info("输入命令：" + str5)
        data = senAndrec(str5, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        time.sleep(115)

        logger.info("输入命令：" + str2)
        data = senAndrec(str2, self.ser, 30)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str4)
        data = senAndrec(str4, self.ser, 10)
        self.assertEqual("", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str2)
        data = senAndrec(str2, self.ser, 30)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))





    def test_C_0000_0059(self):
        str0 = "AT+CFUN=0"
        str1 = "AT+CFUN=1"
        str2 = "AT+CGPADDR"
        str3 = "AT+LDNS=www.baidu.com"

        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        logger.info("输入命令：" + str1)
        data = senAndrec(str1, self.ser, 10)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))

        time.sleep(90)
        logger.info("输入命令：" + str2)
        data = senAndrec(str2, self.ser, 30)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("ADDR", data, msg="开机120S未入网")

        logger.info("输入命令：" + str3)
        data = senAndrec(str3, self.ser, 10)
        self.assertIn("DNS", data, msg="返回值{}与预期不符".format(data))
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))


        logger.info("输入命令：" + str0)
        data = senAndrec(str0, self.ser, 20)
        self.assertIn("OK", data, msg="返回值{}与预期不符".format(data))




if __name__ == '__main__':
    unittest.main()

