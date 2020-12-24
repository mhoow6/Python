import ctypes

# 타이틀 감지 함수
def gettitle():
    # 윈도우 기본 라이브러리 user32.dll 로드
    lib = ctypes.windll.LoadLibrary('user32.dll')
    handle = lib.GetForegroundWindow() # 활성화된 윈도우의 핸들얻음
    buffer = ctypes.create_unicode_buffer(255) # 타이틀을 저장할 버퍼
    lib.GetWindowTextW(handle, buffer, ctypes.sizeof(buffer)) # 버퍼에 타이틀 저장

    return buffer.value

# https://www.youtube.com/watch?v=BkMtK-cyyEE&list=WL&index=3&t=4s