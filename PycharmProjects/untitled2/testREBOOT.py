import serial
import  time


# 1号版
def getDate():
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


def testGetFreq():
    global ser
    TIMES = 0
    try:
        ser = serial.Serial(port="COM3", baudrate=9600, timeout=5)
        ser.flushInput()
        str = "AT+REBOOT"
        Data1=""
        m = 0

        while m < 8:
            print("第{}次循环".format(m + 1))
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print("输入:" + str)
            ser.write(bytes(str + "\r\n", encoding="utf-8"))
            time.sleep(7.3)
            # T = True
            # while T:
            #     ser.write(bytes("AT+CGPADDR" + "\r\n", encoding="utf-8"))
            #     time.sleep(2)
            #     while tbl:
            #         tem = getDate()
            #         print(tem)
            #         if 'OK' in tem:
            #             tbl =False
            #             print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "AT+CGPADDR 已OK")
            #
            #
            #         time.sleep(0.05)
            #         if ('ADDR' in tem):
            #             T = False
            #             print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "已入网")
            #
            #
            #         time.sleep(1)
            #         print("等待1S,再次循环判断cgpaddr的OK是否返回")
            #
            #
            #
            #
            #     print("未入网，等待3s")
            #     time.sleep(3)
            #     # ser.write(bytes(str1 + "\r\n", encoding="utf-8"))
            #
            # time.sleep(5)
            print("等待10s重启")
            m = m + 1
    finally:
        ser.close()

if __name__ == '__main__':
    testGetFreq()