import threading
import time

# 参数定义最多有几个线程可以同时使用资源
# 其他线程要等待有线程释放，才能开始执行

semaphore = threading.Semaphore(3)
# 定义同时只能3个线程

def func():
    if semaphore.acquire():
        for i in range(5):
            print(threading.currentThread().getName() + "get semaphore")
        time.sleep(15)
        semaphore.release()
        print(threading.currentThread().getName() + "release semaphore")


for i in range(8):
    t1 = threading.Thread(target=func)
    t1.start()