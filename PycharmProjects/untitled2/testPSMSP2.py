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

# 4号版
def testGetFreq():
    global ser
    # global tem
    TIMES = 0
    tal = 0
    tbl = True
    try:

        ser = serial.Serial(port="COM3", baudrate=9600, timeout=5)
        ser.flushInput()
        str = "AT+CFUN=0"
        str1 = "AT+CFUN=1"
        str2 = "AT+CGPADDR"
        psm = 'AT+CPSMS=1,,,"10100001","00000010"'
        m = 0
        while m < 10:
            print("第{}次循环".format(m + 1))
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print("输入:" + str1)
            # 开机CFUN=1
            ser.write(bytes(str1 + "\r\n", encoding="utf-8"))

            time.sleep(3)

            while (('OK' or "H") not in getbate()):
                print("未开机，等待60s")
                # TIMES =TIMES +1
                # if TIMES ==10:
                #     break
                time.sleep(15)
                # ser.write(bytes(str1 + "\r\n", encoding="utf-8"))
                # time.sleep(5)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "已开机，下一步已入网")

            time.sleep(15)
            print("等待15s")
            while tal==0:
                if "ADDR" in getbate():
                    tal = 1
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"已入网")
                    break
                print("未入网，等待15s")
                time.sleep(15)
                TIMES = TIMES + 1
                if TIMES == 5 or TIMES == 10:
                    ser.write(bytes(str1 + "\r\n", encoding="utf-8"))
                    print("再次发送开机命令，并等待60S")

                    time.sleep(15)
                    while ('OK' not in getbate()):
                        print("未开机，等待60s")
                        # TIMES = TIMES + 1
                        # if TIMES == 10:
                        #     break
                        time.sleep(15)

                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                print("输入:" + str2)


                #         str2 = "AT+CGPADDR"
                ser.write(bytes(str2 + "\r\n", encoding="utf-8"))
                time.sleep(3)


                while tbl:
                    tem = getbate()
                    print(tem)
                    if 'OK' in tem:
                        tbl =False


                    time.sleep(1)
                    if ('ADDR' in tem):
                        tal = 1
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "已入网")
                        print("tal=")
                        print(tal)

                    time.sleep(15)
                    print("等待15S,再次循环判断cgpaddr的OK是否返回")
                time.sleep(3)

            print('已入网,等待15S进入psm，\n psm')




            time.sleep(15)

            print("进入psm:" + psm)
            ser.write(bytes(psm + "\r\n", encoding="utf-8"))
            time.sleep(2)

            # while ('OK' not in getbate()):
            #     print("未返回PSM OK，等待3s")
            #     # TIMES =TIMES +1
            #     # if TIMES ==10:
            #     #     break
            #     time.sleep(3)
            time.sleep(10)
            print("等待10s")

            print("唤醒PSM")
            ser.write(bytes(str2 + "\r\n", encoding="utf-8"))


            time.sleep(15)



            print("第{}次循环".format(m + 1))
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print("关机:" + str)
            ser.write(bytes(str + "\r\n", encoding="utf-8"))
            time.sleep(10)
            print("等待10s")

            while ('OK' not in getbate()):
                print("未关机，等待5s")
                # TIMES =TIMES +1
                # if TIMES ==10:
                #     break
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