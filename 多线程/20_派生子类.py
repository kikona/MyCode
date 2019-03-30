import multiprocessing
from time import sleep, ctime

class ClockProcess(multiprocessing.Process):
    '''
    两个函数比较重要
    1.init构造函数
    2.run
    '''
    def __init__(self, interval):
        super().__init__()          # 调用父类的构造函数
        self.interval = interval

    def run(self):
        print("The time is %s" % ctime())
        sleep(interval)