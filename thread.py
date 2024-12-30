
from threading import Thread
import main2
import main1

thread1 = Thread(target=main2.main2)  # 线程1
thread2 = Thread(target=main1.main1)  # 线程2
thread1.start()  # 线程1开始
print("摄像头窗口启动\n------------------")
thread2.start()  # 线程2开始
print("人脸识别启动\n--------------------")

thread1.join()  # 等待线程1结束
print("main stop")
thread2.join()  # 等待线程2结束
print("main1 stop")