import multiprocessing
from time import sleep, ctime

# 消费者 设置哨兵
def consumer(input_q):
    print("Into consumer:", ctime())
    while True:
        # 处理项
        item = input_q.get()
        if item is None:
            break
        print("pull", item, "out of q") # 此处替换为有用的工作
    print("Out of consumer:", ctime())
    # 此句执行完，再转入主进程

# 生产者
# 把sequence里的东西拿出来，放到output_q里面，每放一次打印一句话
def producer(sequence, output_q):
    print("Into producer:", ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item, "into q")
    print("Out of producer:", ctime())

# 建立进程
if __name__ == "__main__":
    q = multiprocessing.Queue()
    # 运行消费者进程
    cons_p = multiprocessing.Process(target = consumer, args=(q,))
    cons_p.start()

    sequence = [1, 2, 3, 4]
    producer(sequence, q)
    # 等待所有项被处理
    q.put(None)
    cons_p.join()