# -*- coding: utf8 -*-
# 소켓 라이브러리 로딩
import socket
# 접속 서버 정보
info = ("127.0.0.1", 9999) # 내가 아닌 다른 사람이 접속하게 하기 위해서는 *(혹은 0.0.0.0 wild card), 나 혼자만 사용하면 127.0.0.1 (loopback)
# TCP 소켓 생성
s = socket.socket()
# 서버 접속
s.connect(info)
# 데이터 전송
s.send("hello server\n")
# 데이터 수신 및 출력
print s.recv(1024)
# 접속 종료
s.close() # nc와 다르게 종료 코드