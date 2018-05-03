# -*- coding: utf8 -*-
# 문자열 출력
print "python"

# 변수 선언 
msg = "hello python"
print msg
# 문자열 슬라이싱
print msg[1:3]
print msg[-3:] 
print msg[:-2]
print msg[::-1]

# 리스트
data = []
# 리스트 자료 입력
data.append("hi")
data.append(123)
data.append(1.2)
# 리스트 출력
print data
# 리스트 데이터 제거
data.pop()
print data
data.pop()
print data
# 리스트 요소 인덱스 검색
print data.index("hi")
# index 메소드 실패 시 에러 발생
# print data.index("hi222")

# 사전(딕셔너리)
# { 키 : 값 }
user = {}
user['me'] = {'age': 30, 'address': 'daejoen'}
user['you'] = {'age': 22, 'address': 'seoul'}
# 사전 출력
print user
# 사전 데이터 검색 키 활용
print user['me']
print "user keys:", user.keys()
print "me" in user.keys()

# 제어
# if, if else, if elfi else
num = 4
if num > 0:
    print "num > 0"

if num > 5:
    print "num > 5"
else:
    print "num < 5"

if num % 2 == 0:
    print "even"
elif num % 2 == 1:
    print "odd"
else:
    print "????" 

# 함수
def addition(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

data = [1, 2, 3]
print addition(data)

def help():
    print "id ------ print user id"
    print "pwd ------ print current path"
    print "quit ----- exit program"
    print "ip ------ print ip address"

help()
# 라이브러리 불러오기
import os
import platform
import subprocess

def shell(): 
# 무한루프
    while True:
        cmd = raw_input('>>> ')
        if cmd == 'id':
            if platform.system() == 'Windows':
                print os.environ.get('USERNAME')
            else:
                print os.getenv('USER')
        elif cmd == 'pwd':
            print os.getcwd()
        elif cmd == 'quit':
            print "bye~"
            break
        elif cmd == 'ip':
            if platform.system() == 'Windows':
                buf = subprocess.check_output('ipconfig')
                index = buf.find("IPv4")
                newline = buf[index:].find("\n")
                print index, newline
                ipline = buf[index:index+newline]
                ip = ipline.split(':')
                print ip[1].strip()
            else:
                buf = subprocess.check_output('ifconfig')
                target = 'addr:'
                index = buf.find(target) + len(target)
                space = buf[index:].find(' ')
                # print index, space
                print buf[index:index+space]

        else:
            help()

# urllib2 사용
import urllib2
import re
url = 'https://box.cdpython.com/ezen'
req = urllib2.Request(url)
res = urllib2.urlopen(req)
html = res.read()
# print html
# re 모듈 (정규표현식)을 사용한 패턴 매칭
ipaddress, port = re.findall(r"\d+\.\d+\.\d+\.\d+\/\d+", html)[0].split('/')
print "ip:", ipaddress, "port:", port