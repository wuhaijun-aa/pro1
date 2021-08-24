import pickle

import serial
import os
import time

data = {
	"REGVER": "02",
	"MEID": "860411049916222",
	"MODEL": "LET-SWINLJ8000000001",
	"SWVER": "0000000000000006.3.1",
	"SIM1ICCID": "89861119204008906567",
	"SIM1LTEIMS": "460113034401775"
}

byteDATA = pickle.dumps(data)
def byteToHex(byteDATA):
    return (''.join(["%02X"% x for x in byteDATA]).strip())
sendData = byteToHex(byteDATA)
print(sendData)

print(len(sendData))



str = "AT+NMGS="+str(len(sendData))+","+sendData
print(str)
ser = serial.Serial(port="COM6", baudrate=9600, timeout=5)
ser.flushInput()
ser.write(bytes(str + "\r\n", encoding="utf-8"))

time.sleep(5)
print("等待5s")
redata = []
i = 0
while i < 2:

    count = ser.inWaiting()
    if count != 0:
        resv = ser.read(count).decode("utf-8")
        redata.append(resv)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("输出打印" + resv)
        time.sleep(0.02)
    i = i + 1
