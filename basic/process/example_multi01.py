import multiprocessing as mp

if __name__ == "__main__":
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid) # PID란 운영체제가 각 프로세스에게 부여한 고유번호

# https://wikidocs.net/85603