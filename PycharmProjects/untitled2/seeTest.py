import os
import sys
import unittest
from pathlib import Path
import serial
import time
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
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

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


class caseTest(unittest.TestCase):
    # def __init__(self,name):
    #      self.name = os.path.basename(sys.argv[0].replace(".py",""))
    #      # self.namepath = Path("d:\\test\\test")
    #      pass
    def setUp(self) -> None:
        self.ser = serial.Serial(port="COM5", baudrate=9600, timeout=5)
        self.ser.flushInput()
        logger.info("--------------->setUp(self)")


    def tearDown(self) -> None:
        self.ser.close()
        logger.info("--------------->tearDown(self)")

    def test_GetFreq(self):
        # global ser
        # TIMES = 0
        try:
            # ser = serial.Serial(port="COM3", baudrate=9600, timeout=5)
            # ser.flushInput()
            str0 = "AT+CFUN=0"
            str1 = "AT+CFUN=1"
            str2 = "AT+CGPADDR"
            m = 0
            while m < 4096:
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


if __name__ == '__main__':
    unittest.main()

