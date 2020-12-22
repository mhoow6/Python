import multiprocessing as mp

def worker():
    print("SubProcess End")


if __name__ == "__main__":
    # process spawning: 부모 프로세스(Parent Proecess)가 운영체제에 요청하여 자식 프로세스(Child Process)를 새로 만들어내는 과정
    # MainProcess가 부모
    # SubProcess가 자식
    p = mp.Process(name="SubProcess", target=worker)
    p.start()

# https://wikidocs.net/85603