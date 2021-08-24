import serial
import  time


# 1号版
def getbate():
    # global ser
    i = 0

    redata = []
    while i <2:

        count = ser.inWaiting()
        if count != 0:
            resv = ser.read(count).decode("utf-8")
            # resv = ser.read(count)
            # print("======")
            # print(resv)
            # print("======")
            # resv = str(resv)
            redata.append(resv)
            print("输出打印"+resv)
            time.sleep(0.01)
        i = i +1
    return ''.join(redata)


def testGetFreq():
    global ser
    TIMES = 0
    try:
        ser = serial.Serial(port="COM3", baudrate=9600, timeout=5)
        ser.flushInput()
        str = "AT+CFUN=0"
        str1 = "AT+CFUN=1"
        str2 = "AT+CGPADDR"
        m = 0
        while m < 10:
            n = 0
            print("第{}次循环".format(m + 1))
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print("输入:" + str1)
            ser.write(bytes(str1 + "\r\n", encoding="utf-8"))
            n = (m+1) *2
            time.sleep(15+n)
            getbate()

            # while ('OK' not in getbate()):
            #     print("未开机，等待2s")
            #     time.sleep(2)

            # while ('ADDR' not in getbate()):
            #     print("未入网，等待1s")
            #     time.sleep(3)
            #
            #     print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            #     print("输入:" + str2)
            #     ser.write(bytes(str2 + "\r\n", encoding="utf-8"))
            #     time.sleep(1)
            #
            # print("等待1s")
            # print('已入网，\n下面关机')
            # time.sleep(1)

            print("第{}次循环".format(m + 1))
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print("关机:" + str)
            ser.write(bytes(str + "\r\n", encoding="utf-8"))
            time.sleep(5)
            getbate()
            print("等待1.5s")

            # while ('OK' not in getbate()):
            #     print("未关机，等待2s")
            #
            #     time.sleep(2)
            #
            # time.sleep(5)
            time.sleep(3)
            m = m + 1
    finally:
        ser.close()

if __name__ == '__main__':
    testGetFreq()