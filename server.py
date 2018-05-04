# -*- coding: utf8 -*-
# 소켓 라이브러리 로딩
import socket
import threading

def handler(client, address):
    while True: # nc로 접속해서 데이터를 송/수신하면 무한 루프. ctrl + c로 종료해줘야 종료
        try:
            # 클라이언트가 전송한 데이터 수신
            data = client.recv(1024)
        except:
            print "Exception!!!"
            break
        if not data:
            # 데이터를 보내지 않은 클라이언트 연결 종료
            client.close()
            break
        print "address %s send data %s" % (address[0], data)
        # 수신 데이터를 클라이언트에 전송
        client.send(data)

# 서버 정보
info = ("0.0.0.0", 9999)
# 소켓 생성
s = socket.socket()
# 9999번 포트 바인딩
s.bind(info) 
# 바인딩 포트 리스닝
s.listen(5) # 들어오는 것을 지켜본다. 
while True:
     # 접속 요청 승인
    client, address = s.accept() # 수신된 걸 승인한다.
    print "[+] new connection from %s(%d)" % (address[0], address[1])
    th = threading.Thread(target=handler, args=(client, address))
    th.start()


# thread가 많으면 이를 처리하기 위해 메모리를 할당해줘야 함. 한정된 자원을 많이 쓰게 됨. 하드웨어 제약 고려해야 함.