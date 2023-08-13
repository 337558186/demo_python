"""
设置守护线程【可选】
线程是程序执行的最小单位，Python在进程启动起来后，会自动创建一个主线程，
之后使用多线程机制可以在此基础上进行分支，产生新的子线程。
子线程启动起来后，主线程默认会等待所有线程执行完成之后再退出。
可以将子线程设置为守护线程，此时主线程任务一旦完成，所有子线程将会和主线程一起结束（就算子线程没有执行完也会退出）
thread01.setDaemon(True)
"""
import time
from threading import Thread, Lock,current_thread
from time import sleep

book_num = 100  # 图书馆最开始有100本图书
bookLock = Lock()


def books_return():
    global book_num
    while True:
        bookLock.acquire()
        book_num += 1
        print("归还1本，现有图书{}本".format(book_num))
        bookLock.release()
        sleep(1)  # 模拟事件发生周期

def books_lease():
    global book_num
    while True:
        bookLock.acquire()
        book_num -= 1
        print("借走1本，现有图书{}本".format(book_num))
        bookLock.release()
        sleep(2)  # 模拟事件发生周期

def target():

    if current_thread().name == "1":
        print("线程{}正在执行".format(current_thread().name))
        time.sleep(2)
    else:
        time.sleep(6)
    print("线程{}已退出".format(current_thread().name))



if __name__ == "__main__":

    thread_target = Thread(target=target,name="1")
    thread_lease = Thread(target=books_lease)
    thread_return = Thread(target=books_return)

    thread_target.start()
    # 阻塞线程
    thread_target.join(timeout=3)

    thread_lease.start()
    thread_return.start()
