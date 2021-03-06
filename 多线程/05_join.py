'''
利用time函数，生成两个函数
计算总的运行时间
'''
import time
import threading

def loop1(in1):
    # ctime 得到当前时间
    print('Start loop 1 at :', time.ctime())
    # 把参数打印出来
    print("我是参数", in1)
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('End loop 1 at :', time.ctime())

def loop2(in1, in2):
    # ctime 得到当前时间
    print('Start loop 2 at :', time.ctime())
    # 把参数打印出来
    print("我是参数", in1, "和参数", in2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print('End loop 2 at :', time.ctime())

def main():
    print('Start at :', time.ctime())
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程的函数为 start_new_thread: 启动一个新的线程
    # 参数两个：一个是需要运行的函数名，第二个是运行函数的参数作为元组使用，为空则使用空元组
    # 注意：如果函数只有一个参数，需要参数后有一个逗号
    t1 = threading.Thread(target=loop1, args=("wyx",))
    t1.start()

    t2 = threading.Thread(target=loop2, args=("jjy", "yy"))
    t2.start()

    t1.join()
    t2.join()

    print('All done at :', time.ctime())


if __name__ == '__main__':
    main()
    # 一定要有while语句
    # 因为启动多线程后，本程序就作为主线程存在
    # 如果主线程执行完毕，则子线程可能也需要终止
    while True:             #等待loop，loop2完成，如果不等待则不知道是否完成
        time.sleep(10)       #每1s醒来一次，查看是否完成

