import serial

import time
import os
import sys
from pathlib import Path
import threading

name = os.path.basename(sys.argv[0]).replace(".py", "")
print(name)

newPath = Path("D:test\\test")

global cond
cond = 1
error = "ERROR"

def sermothed(port,Baudrate):
    global ser
    ser = serial.Serial(port, Baudrate, timeout=5)
    # 清空缓存区
    ser.flushInput()


# 获取串口数据
def get_data():
    i= 0
    while i <2:
        count = ser.inWaiting()
        if count != 0:
            recv = ser.read(ser.in_wating).decode('utf-8', 'ignore')
            print(time.strftime("%Y-%m-%d %H：%M：%S",time.localtime()),"打印结果",recv)
            f.write("输出打印"+time.strftime("%Y-%m-%d %H：%：M：S",time.localtime())+recv)
        i = i+1

# 创建log存放的路径，和文件，先进行对路径下的文件夹是否存在进性识别
def creatTest():
    textneam = time.strftime("%Y%m%d%H%M%S",time.localtime())+name+'txt'
    if newPath.exists():
        orgpath = os.chdir(r"d:\\test\\test")
        global f
        f = open(textneam,'a',encoding='utf-8')
    else:
        os.makedirs(r"d:\\test\\test")
        orgpath = os.chdir(r"d:\\test\\test")

        orgpath = os.chdir(r"d:\\test\\test")
        # global f
        f = open(textneam, 'a', encoding='utf-8')

def get_data_Time():

    QTime = time.time()
    while (QTime+100) > time.time():
        count = ser.inWaiting()
        if count != 0:
            recv = ser.read(ser.in_wating).decode('utf-8', 'ignore')
            print(time.strftime("%Y-%m-%d %H：%M：%S",time.localtime()),"打印结果",recv)
            f.write("输出打印"+time.strftime("%Y-%m-%d %H：%：M：S",time.localtime())+recv)
        time.sleep(0.03)

def writeData(str):
    str = str +"\r\n"
    print(str)
    ser.write(bytes(str,encoding='utf-8'))
    f.write(str)
def AT_NMGS():
    try:
        sermothed('COM6', 9600)
        print("1")
        str1 = "AT+NMGS=3,002300"

        writeData(str1)
        print("2")
        time.sleep(1)
        get_data()

    except:
        pass

    finally:
        ser.close()
        f.close()


if __name__ == '__main__':
    creatTest()
    t = threading.Thread(target="AT_NMGS", name="COPA协议")
    t.start()
    t.join()















































































































































































































































































































































































































