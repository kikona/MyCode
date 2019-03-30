from multiprocessing import Process
import os

def info(title):
    print(title)
    # 当前模块的名称
    print('module name:', __name__)
    # 打印父进程id
    print('parent process:', os.getppid())
    # 打印本身进程，也就是子进程的id
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == "__main__":
    info('main line')
    # 创建子进程，调用函数 f()，其父进程是 main
    p = Process(target=f, args=('bob',))

    p.start()
    p.join()

# 结果

# main line
# module name: __main__
# parent process: 16908     # main 的父进程的id，就是启动 21.py这个文件的进程
# process id: 1824          # main 进程的id

# function f                # 启动 子进程p
# module name: __mp_main__
# parent process: 1824      # p的父进程id和上面的main 进程的一样，意味着是同一个进程
# process id: 11788         # p进程的id
# hello bob