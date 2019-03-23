import threading
from time import sleep, ctime

loop = [4,2]

class ThreadFunc:

    def __init__(self):
        self.name = name

    def loop(self, nloop, naec):
        '''

        :param nloop: loop函数的名称
        :param naec: 系统睡眠时间
        :return:
        '''
        print('Start loop', nloop, 'at', ctime())
        sleep(nsec)
        print('Done loop', nloop, 'at', ctime())

def main():
    print("Strarting at:", ctime())

    # ThreadFunc("loop").loop：跟以下两个式子相等：
    # t = ThreadFunc("loop")
    # t.loop
    # 以下 t1 和 t2 的定义方式相等
    t = ThreadFunc("loop")
    t1 = threading.Thread(target = t.loop, args=("LOOP1", 4))
    # 以下这种写法更西方人，工业化一点
    t2 = threading.Thread(target = ThreadFunc("loop").loop, args=("LOOP2", 2))

    # 常见错误写法
    # t1 = threading.Thread(target = t.loop(100, 4))
    # t2 = threading.Thread(target = t.loop(100, 2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('All done at :', ctime())


if __name__ == '__main__':
    main()
    # 一定要有while语句
    # 因为启动多线程后，本程序就作为主线程存在
    # 如果主线程执行完毕，则子线程可能也需要终止
    while True:             #等待loop，loop2完成，如果不等待则不知道是否完成
        sleep(10)       #每1s醒来一次，查看是否完成