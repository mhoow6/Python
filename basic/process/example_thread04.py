import threading
import time


class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name            # thread 이름 지정

    def run(self):
        print("sub thread start ", threading.currentThread().getName())
        time.sleep(5)
        print("sub thread end ", threading.currentThread().getName())


print("main thread start")

# fork: 메인 스레드가 서브 스레드를 생성하는 것
t1 = Worker("1")        # sub thread 생성
t1.start()              # sub thread의 run 메서드를 호출

t2 = Worker("2")        # sub thread 생성
t2.start()              # sub thread의 run 메서드를 호출

# join: 모든 스레드가 작업을 마칠 때까지 기다리는 것
t1.join()
t2.join()

print("main thread post job")
print("main thread end")

# https://wikidocs.net/82581