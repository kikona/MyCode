import time

import threading

def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")

# 主线程
print("Main thraed")

t1 = threading.Thread(target=fun, args=())
# 设为守护线程的方法，必须在 start 之前设置，否则无效
t1.setDaemon(True)
# 也可以这样写：t1.daemon = True
t1.start()

time.sleep(1)
print("Main thread end")


