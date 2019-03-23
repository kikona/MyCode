import time

import threading

def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")

# 主线程
print("Main thraed")

t1 = threading.Thread(target=fun, args=())
t1.start()

time.sleep(1)
print("Main thread end")
