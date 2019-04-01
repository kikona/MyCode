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
    for item in sequence:
        print("Into producer:", ctime())
        output_q.put(item)
        print("Out of producer:", ctime())

# 建立进程
if __name__ == "__main__":
    q = multiprocessing.Queue()
    # 运行消费者进程
    cons_p1 = multiprocessing.Process(target = consumer, args=(q,))
    cons_p1.start()

    cons_p2 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p2.start()

    sequence = [1, 2, 3, 4]
    producer(sequence, q)

    # 哨兵值
    q.put(None)
    q.put(None)

    cons_p1.join()
    cons_p2.join()