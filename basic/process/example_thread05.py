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

threads = []
for i in range(3):
    thread = Worker(i)
    thread.start()              # sub thread의 run 메서드를 호출
    threads.append(thread)      # threads 리스트에 생성된 thread 객체 추가

# thread 객체를 join
for thread in threads:
    thread.join()

print("main thread post job")
print("main thread end")

# https://wikidocs.net/82581