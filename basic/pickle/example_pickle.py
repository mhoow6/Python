# 일반 텍스트를 파일로 저장할 때는 파일 입출력 함수를 이용하지만
# 리스트나 클래스트 같은 텍스트가 아닌 자료형은 pickle 모듈을 이용한다

# 오류 예시: 텍스트가 아닌 자료형을 파일로 저장
# list = ['a', 'b', 'c']
#
# with open("list.txt", "w") as f:
#     f.write(list)

import pickle

list = ['a', 'b', 'c']

# pickle로 데이터를 저장하거나 불러올 경우 byte형식으로 읽거나 써야한다.
# wb로 데이터를 입력하는 경우 .bin 확장자를 사용하는 것이 좋음
with open("../list.txt", "wb") as f:
    pickle.dump(list, f)

# pickle.dump를 사용해서 데이터를 입력한 파일이여야 load가 가능하다.
with open("../list.txt", "rb") as f:
    print(pickle.load(f))