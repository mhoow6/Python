from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)

# client는 서버에 접속하기 위해 connect만 해주면 된다.
# (,) 투플에서 앞 부분은 서버 주소, 뒷 부분은 포트
clientSock.connect(('127.0.0.1', 8080))

print('연결 확인 됐습니다.')

# encode 메소드를 통해 문자열을 byte로 변환해주어서 보내준다.
# 문자열을 바로 transport에 싣는 것은 불가능
clientSock.send('I am a client'.encode('utf-8'))

print('메시지를 전송했습니다.')

# recv: 소켓의 메시지가 실제로 수신될때까지 대기
# 수신할 소켓에서 1024byte만큼 가져옴
# 1024보다 많다면 다시 recv(1024)를 실행할때 남은 것을 가져옴
data = clientSock.recv(1024)

# byte로 encode된것을 다시 decode하여 문자열로
print('받은 데이터 : ', data.decode('utf-8'))

# https://seolin.tistory.com/97