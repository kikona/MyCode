# 环境
- xubuntu 16.04
- anaconda
- pycharm
- python 3.6
# 文章参考
- http://www.cnblogs.com/jokerbj/p/7460260.html
- http://www.dabeaz.com/pyhton/UnderstandingGIL.pdf

# 多线程 vs 多进程
- 程序：一堆代码以文本形式存入一个文档
- 进程：程序运行的一个状态
    - 包含地址空间，内存，数据栈等
    - 每个进程由自己完全独立的运行环境，多进程共享数据是一个问题
- 线程
    - 一个进程的独立运行片段，一个进程可以有多个线程
    - 可以理解为轻量化的进程
    - 一个进程的多个线程之间共享数据和上下文运行环境
    - 这样就会产生共享互斥问题
- 全局解释器锁(GIL)
    - Python代码的执行是由python虚拟机进行控制
    - python有多线程的概念，但是实际上在主循环中只能有一个控制线程在执行，所以被称为是伪多线程

- Python包
    - thread: 有问题，不好用，python3 改成了 _thread
    - threading: 通行的包，经常使用的包
    - 案例01：顺序执行，耗时较长
    - 案例02：改用多线程，缩短总时间，使用_thread
    - 案例03：多线程传参数

- threading 的使用
    - 直接利用 threading.Thread 生成 Thread实例
        -1. t = theadinig.Thread(target=xxx, args=(xxx,))
            - target:后面只能是函数名
            - args：是使用的函数的参数，空的也要写
        -2. t.start()：启动多线程
        -3. t.join()：等待多线程执行完成
        - 案例04
        - 案例05: 加入join之后比较跟案例04的结果的异同
        - 守护线程-daemo
            - 如果在程序中将子线程设置成守护线程，则子线程会在主线程结束的时候自动退出
            - 一般认为，守护线程不重要或者不允许离开主线程独立运行
            - 守护线程案例能否有效果跟环境相关
            - 案例06非守护线程
            - 案例07守护线程
        - 线程常用属性
            - threading.currentThread：返回当前线程变量
            - threading.enumerate：返回一个包含正在运行的线程的list，正在运行的线程指的是线程启动
                                    后，结束前的状态
            - threading.activeCount：返回正在运行的线程数量，效果跟len(threading.enumerate)相同
            - thr.setName：给线程设置名字
            - thr.getName：等到线程的名字
            - 案例08
    - 直接继承自threading.Thread
        - 直接继承 Thread
        - 重写 run函数
        - 类实例可以直接运行
        - 案例09
        - 案例10  工业风案例