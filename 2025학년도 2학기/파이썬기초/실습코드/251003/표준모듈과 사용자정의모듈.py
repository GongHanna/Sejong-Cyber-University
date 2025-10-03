## 표준모듈
# - 프로그래밍을 개발하기 위해 기본적으로 사용해야 하는 문자 처리, 웹, 수학과 관련된 다양한 내장 모듈을 말함
    # -> 추가 설치 없이 import문 한 줄로 사용함

## sys 모듈
# - 시스템과 관련된 정보를 가진 모듈로 파이썬 인터프리터가 제공하는 변수나 함수를 제어할 수 있는 방법을 제공함

import sys

print("sys.getwindowsversion()\n", sys.getwindowsversion())
print("---------------------")
print("sys.copyright\n", sys.copyright)
print("-----------------------")
print("sys.version\n", sys.version)


## os 모듈
# - 운영체제에서 제공되는 여러 기능을 실행할 수 있는 방법을 제공하는 모듈로, 새로운 폴더를 만들거나 폴더 내부 파일 목록 등을 확인하는 기능 등을 제공함

import os

#운영체제의 기본 정보 출력
print("os.name: ", os.name)
print("os.getcwd(): ", os.getcwd())
print("os.listdir(): ", os.listdir())
#디렉터리 생성 및 삭제
#디렉터리 내부가 비어 있어야 삭제가능
os.mkdir("newDir") #폴더생성
os.rmdir("newDir") #폴더삭제


## math 모듈
# - 수학과 관련된 다양한 함수들과 상수들을 제공하는 모듈

import math

#사인
print("math.sin(1): ", math.sin(1)) #math.sin(1):  0.8414709848078965
#내림
print("math.floor(3.14): ", math.floor(3.14)) #math.floor(3.14):  3
#올림
print("math.ceil(3.14): ", math.ceil(3.14)) #math.ceil(3.14):  4


## random 모듈
# - 난수 생성 모듈로, 정수 모듈을 생성하는 randint() 함수와 임의의 난수를 생성하는 random() 함수가 있음

import random

#random() -> 0.0 <= r <1.0 사이의 float 숫자 반환
print("random.random(): ", random.random()) #random.random():  0.7839677122818584
#uniform(start,end) -> start~end 범위의 float 반환
print("random.uniform(1,10): ", random.uniform(1,10)) #random.uniform(1,10):  8.136585384579462
#random.randrange(end) : 0 ~ end 범위의 int 반환
print("random.randrange(10): ", random.randrange(10)) #random.randrange(10):  3
#random.randrange(start,end) : start ~ end 범위의 int 반환
print("random.randrange(1,45): ", random.randrange(1,45)) #random.randrange(1,45):  18
#random.choice(list) : list 내부의 요소를 랜덤하게 반환
print("random.choice([10,20,30,40]): ", random.choice([10,20,30,40])) #random.choice([10,20,30,40]):  10

list_temp = [10,20,30,40]
#random.shuffle(list) : list의 요소를 랜덤에서 섞음.
random.shuffle(list_temp)
print("list_temp: ", list_temp) #list_temp:  [40, 30, 10, 20]
#random.sample(list, k=개수) : 리스트 중에 개수만큼 추출
print("random.sample([10,20,30,40], k=2): ", random.sample([10,20,30,40], k=2)) #random.sample([10,20,30,40], k=2):  [30, 40]


## datetime 모듈
# - date(날짜) 및 time(시간)과 관련된 모듈로, 날짜 형식을 만들 때 자주 사용함

import datetime
#현재 날짜-시간 출력
now = datetime.datetime.now()
print(now.year, "년", end=" ")
print(now.month, "월", end=" ")
print(now.day, "일", end=" ")
print(now.hour, "시", end=" ")
print(now.minute, "분", end=" ")
print(now.second, "초")
#2025 년 10 월 3 일 10 시 57 분 59 초
#시간 포맷팅
print(now.strftime("%Y. %m. %d %H:%M:%S")) #2025. 10. 03 10:59:13


## urllib 모듈
# - 웹과 관련되 모듈로, 웹 주소의 정보를 불러옴
    # -> 대표적으로 urllib의 request 모듈을 사용하면 특정 URL의 정보를 불러올 수 있음

import urllib.request as req # as -> 별칭처리(이름이 긴 모듈을 간단한 별명으로 불러 쓰겠다)

#urlopen() 함수로 웹 페이지의 코드를 읽어옴
target = req.urlopen("https://dept.sjcu.ac.kr/computer/index.do")
output = target.read()

print(output)




## 사용자 정의 모듈
# - 파이썬에서는 .py 파일 자체가 모듈임
# - Jupyter Notebook환경의 경우 같은 경로에 .py 파일로 코드 작성


## __name__ 사용
# - 모듈의 이름이 저장되는 변수, 현재 모듈이 최상위 모듈로 수행되는지 여부 확인 가능

print(__name__) #__main__

# - print(__name__) : 현재 수행되는 파이썬 파일의 이름
    # -> 최상위 모듈은 __main__을 반환
