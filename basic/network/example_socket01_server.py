from socket import *

# AF(Address Family): 주소 체계
# AF_INET: ipv4 AF_INET6: ipv6
# 소켓 타입: SOCK_STREAM, SOCK_DGRAM
serverSock = socket(AF_INET, SOCK_STREAM)

# 생성된 소켓 번호와 실제 어드레스 패밀리를 연결
# (,) 투플에서 앞부분은 IP, 뒷부분은 포트번호
# ''는 INADDR_ANY: 모든 인터페이스와 연결하고 싶을 때 사용
serverSock.bind(('', 8080))

# 해당 소켓은 1개의 동시접속만 허용
# client의 접속을 기다리는 단계
serverSock.listen(1)

# 접속을 받아들이는 단계
# accept을 하게 되면 return으로 상대의 소켓과, 상대의 AF를 전달받음
# 이후 accept으로 생성된 connectionSock라는 소켓을 이용해서 데이터를 주고받음
connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속이 확인되었습니다.')

# recv: 소켓의 메시지가 실제로 수신될때까지 대기
# 수신할 소켓에서 1024byte만큼 가져옴
# 1024보다 많다면 다시 recv(1024)를 실행할때 남은 것을 가져옴
data = connectionSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))

connectionSock.send('I am a server.'.encode('utf-8'))
print('메시지를 보냈습니다.')

# https://seolin.tistory.com/97