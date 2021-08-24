import serial
import  time

def getbate():
    # global ser
    i = 0

    redata = []
    while i <2:

        count = ser.inWaiting()
        if count != 0:
            resv = ser.read(count).decode("utf-8")
            redata.append(resv)
            print("输出打印"+resv)
            time.sleep(0.02)
        i = i +1
    return ''.join(redata)

# #7号版
def testGetFreq():
    global ser
    TIMES = 0
    try:
        ser = serial.Serial(port="COM9", baudrate=9600, timeout=5)
        ser.flushInput()
        str = "AT+CFUN=0"
        str1 = "AT+CFUN=1"
        str2 = "AT+CGPADDR"
        m = 0
        while m < 600:
            print("第{}次循环".format(m + 1))
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print("输入:" + str1)
            ser.write(bytes(str1 + "\r\n", encoding="utf-8"))

            time.sleep(3)

            while ('OK' not in getbate()):
                print("未开机，等待60s")
                TIMES =TIMES +1
                if TIMES ==10:
                    break
                time.sleep(60)
                ser.write(bytes(str1 + "\r\n", encoding="utf-8"))
                time.sleep(5)
            time.sleep(60)
            print("等待60s")
            while ('ADDR' not in getbate()):
                print("未入网，等待60s")
                time.sleep(60)
                TIMES = TIMES + 1
                if TIMES == 5 or TIMES == 10:
                    ser.write(bytes(str1 + "\r\n", encoding="utf-8"))
                    print("再次发送开机命令，并等待60S")
                    time.sleep(60)
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                print("输入:" + str2)
                ser.write(bytes(str2 + "\r\n", encoding="utf-8"))
                time.sleep(3)
            # a = True
            # while a:
            #     # global ser
            #     # aa = ""
            #     aa = getbate()
            #     if 'IPADDR' in aa:
            #         a = False
            #         break
            #     print("未入网，等待5s")
            #     time.sleep(5)

            print('已入网,等待60S后关机，\n 关机')
            time.sleep(60)
            print("第{}次循环".format(m + 1))
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print("关机:" + str)
            ser.write(bytes(str + "\r\n", encoding="utf-8"))
            time.sleep(10)
            print("等待10s")

            while ('OK' not in getbate()):
                print("未关机，等待5s")
                TIMES =TIMES +1
                if TIMES ==10:
                    break
                time.sleep(5)
            # b = True
            # while b:
            #     # global ser
            #     # bb = ""
            #     bb = getbate()
            #     if 'OK' in bb:
            #         a = False
            #         break
            #     print("未关机，等待5s")
            #     time.sleep(5)
            time.sleep(60)
            m = m + 1
    finally:
        ser.close()

if __name__ == '__main__':
    testGetFreq()