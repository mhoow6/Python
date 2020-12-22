# import time
#
# # 시작 시간
# start_time = time.time()
#
# # 1~50000까지 반복
# def count(name):
#     for i in range(1, 50001):
#         print(name," : ", i)
#
# # 실행을 구분하기 위한 list
# num_list = ['p1', 'p2', 'p3', 'p4', 'p5']
#
# # num_list 크기만큼 실행
# for num in num_list:
#     count(num)
#
# # 프로그램 종료 후 최종 시간 출력
# print("--- %s seconds ---" % (time.time() - start_time))

import multiprocessing
import time

start_time = time.time()


def count(name):
    for i in range(1, 50001):
        print(name, " : ", i)


num_list = ['p1', 'p2', 'p3', 'p4']

if __name__ == '__main__':
    # 멀티 쓰레딩 Pool 사용해서 함수 실행을 병렬
    pool = multiprocessing.Pool(processes=2)  # 현재 시스템에서 사용 할 프로세스 개수
    pool.map(count, num_list)
    pool.close()
    pool.join()

print("--- %s seconds ---" % (time.time() - start_time))

# https://niceman.tistory.com/145
