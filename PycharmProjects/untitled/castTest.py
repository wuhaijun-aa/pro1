import os
import sys
import unittest
from pathlib import Path
import serial
import time
import  numbers
import requests




def getbate():
    i = 0
    redata = []
    while i < 2:

        count = ser.inWaiting()
        if count != 0:
            resv = ser.read(count).decode("utf-8")
            redata.append(resv)
            print("输出打印"+resv)
            time.sleep(0.02)
        i = i +1
    return  redata

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


    def test_coap(self):
        try:
            global ser
            ser = serial.Serial(port="COM6", baudrate=9600, timeout=5)
            ser.flushInput()
            str = "AT+NMGS=3,002300"

            m = 0
            while m < 1000 :
                print("第{}次循环".format(m+1))

                ser.write(bytes(str+"\r\n",encoding="utf-8"))
                print("输入:"+str)
                time.sleep(1)
                print("等待1s")
                s ="".join (getbate())

                print(s)
                self.assertIn("OK", s, msg="通信失败")
                if "ERROR" in s:
                    break
                m = m + 1
        finally:
            ser.close()

if __name__ == '__main__':



    unittest.main()

