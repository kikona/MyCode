import threading
import time

def func():
    print("I am running.......")
    time.sleep(4)
    print("I am done..........")

if __name__ == "__main__":
    t = threading.Timer(6, func)        # 多长时间之后调用函数
    t.start()

    i = 0
    while True:
        print("{0}********".format(i))
        time.sleep(3)
        i += 1

# 结果
# 0********             睡3秒
# 1********             睡3秒
# I am running.......   调用函数，函数睡4s
# 2********
# 3********
# I am done..........   这句打印也有可能打印在3*****之前，时间不一定