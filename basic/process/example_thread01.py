import threading
import time


class BackThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        # 데몬 프로세스일 경우 부모 프로세스가 죽으면 같이 죽는다.
        # self.daemon = True

    def run(self):
        for i in range(10):
            print(threading.currentThread().getName, i)
            time.sleep(0.1)


def threadingtest1():
    for i in range(10):
        print(threading.currentThread().getName, i)
        time.sleep(0.1)


def threadingtest2():
    for i in range(10):
        print(threading.currentThread().getName, i)
        time.sleep(0.1)


thread1 = threading.Thread(target=threadingtest1, args=())
# thread1.daemon = True

thread2 = threading.Thread(target=threadingtest2, args=())
# thread2.daemon = True


thread1.start()
thread2.start()
BackThread().start()

# https://www.jbmpa.com/python_basic/26