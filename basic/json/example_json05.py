import json
from io import StringIO

# UTF-16 인코딩으로 파일을 열어줘야 됨
with open("../event.json", encoding='UTF-16') as j:
    data = json.load(j)

    io = StringIO()

    json.dump(data, io, indent="\t")

    print(io.getvalue())

# 에러 발생 코드
# with open("settings.json") as j:
#     data = json.load(j)

# 에러 내용
# Traceback (most recent call last):
#   File "E:\github\TIL\Python\basic\example_json05.py", line 6, in <module>
#     data = json.load(j)
#   File "C:\Users\mhoow\AppData\Local\Programs\Python\Python39\lib\json\__init__.py", line 293, in load
#     return loads(fp.read(),
# UnicodeDecodeError: 'cp949' codec can't decode byte 0xff in position 0: illegal multibyte sequence

# 에러 해결 참고 자료
# https://nackwon.tistory.com/120
# http://blog.naver.com/PostView.nhn?blogId=chandong83&logNo=220979166817&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
# https://ssoondata.tistory.com/12