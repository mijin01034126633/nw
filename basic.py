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

