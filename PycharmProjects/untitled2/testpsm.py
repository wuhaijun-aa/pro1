import serial
import  time
if __name__ == '__main__':
    print("name is :%s"%(__name__))
    ser = serial.Serial(port="COM3", baudrate=9600, timeout=5)
    ser.flushInput()
    str = "AT+CGPADDR"
    m = 0
    while m < 1000:
        print("第{}次循环".format(m + 1))
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("输入:" + str)
        ser.write(bytes(str + "\r\n", encoding="utf-8"))
        time.sleep(1.5)
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
        m = m + 1
