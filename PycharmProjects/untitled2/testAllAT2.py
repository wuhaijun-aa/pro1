import serial
import time

import  os

cont = []

def writeAndRead(str):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print("写入命令："+str)

    ser.write(bytes(str+"\r\n",encoding="utf-8"))

    time.sleep(2)

    cond = ser.inWaiting()
    res = ser.read(cond).decode("utf-8")
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"输出："+res)
    if "ERR" in res:
        cont.append(str)


if __name__ == '__main__':
    global ser
    ser = serial.Serial("com7", 9600, timeout=5)
    ser.flushInput()

    str = "AT+CGSN"
    writeAndRead(str)

    str = "AT+FWVER"
    writeAndRead(str)

    str = "AT+IMEI?"
    writeAndRead(str)

    str = "AT+CGMR"
    writeAndRead(str)

    str = "AT+CGATT?"
    writeAndRead(str)

    str = "AT+CIMI"
    writeAndRead(str)

    str = "AT+CFUN?"
    writeAndRead(str)


    for i in  cont:
        print("不支持的AT："+i)