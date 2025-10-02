## 내장함수
# - 프로그래밍의 편의를 위해 프로그래밍에서 많이 사용되는 기능들을 내장함수로 제공하는 함수
# - https://docs.python.org/3/library/functions.html

# 자주 사용하는 주요 내장함수
# - abs(), sum(), max(), min(), pow(), round() : 수학 계산함수. 각각 절대값, 합, 최대값, 최솟값, 지수승, 반올림 계산함수
# - all(), any() : 객체 구성 요소가 모두 참이면, 어느 하나라도 참이면 True, 그렇지 않으면 False를 반환함
# - bin(), oct(), hex() : 각각 2진수, 8진수, 16진수 변환값 반환
# - int(), float(), bool(), str() : 자료값 형 변환함수. 각각 int, float, bool, str형으로 변환해서 반환함
# - list(), tuple(), set() : 각각 리스트, 튜플, 짖ㅂ합 객체로 변환해서 반환함
# - char(), ord() : 각각 문자, 문자 코드값(10진수) 반환함
# - type() : 자료형을 반환함
# - open(), close() : 파일 입출력 함수
# - input(), print(), format() : 각각 입력, 출력, 문자열 출력형싱 지정 함수
# - len() : 컬렉션 객체의 크기(요소 개수)를 반환함
# - sorted(), reversed() : 리스트를 정렬해서 반환함

print("abs(-3)=", abs(-3)) #abs(-3)= 3
print("sum([1,2,3,4,5])=", sum([1,2,3,4,5])) #sum([1,2,3,4,5])= 15
print("max([1,2,3,4,5])=", max([1,2,3,4,5])) #max([1,2,3,4,5])= 5
print("min([1,2,3,4,5])=", min([1,2,3,4,5])) #min([1,2,3,4,5])= 1
print("pow(5,2)=", pow(5,2)) #pow(5,2)= 25
print("round(3.14)=", round(3.14)) #round(3.14)= 3
# 숫자를 기준으로 0은 False, 1은 True, all()은 AND, any()는 OR와 같은 역할
print("all([1,2,3])=", all([1,2,3])) #all([1,2,3])= True
print("all([1,2,3,0])=", all([1,2,3,0])) #all([1,2,3,0])= False
print("any([1,2,3,0])=", any([1,2,3,0])) #any([1,2,3,0])= True
print("any([0,''])=", any([0,''])) #any([0,''])= False, ''->공백문자는 False로 처리
# 진수 변환 함수
print("bin(234)=", bin(234)) #bin(234)= 0b11101010
print("oct(234)=", oct(234)) #oct(234)= 0o352
print("hex(234)=", hex(234)) #hex(234)= 0xea
# 형변환 함수
print("int(3.14)=", int(3.14)) #int(3.14)= 3
print("float(3)=", float(3)) #float(3)= 3.0
print("bool('True')=", bool('True')) #bool('True')= True
print("str(10)=", str(10)) #str(10)= 10

print("len('python')=", len("python")) #len('python')= 6 , 요소의 개수 반환
print("len([1,2,3,4,5])=", len([1,2,3,4,5])) #len([1,2,3,4,5])= 5
print("sorted([11,52,23,4,35])=", sorted([11,52,23,4,35])) #sorted([11,52,23,4,35])= [4, 11, 23, 35, 52], 오름차순 형태로 정렬
print("reversed([1,2,3,4,5])=", list(reversed([1,2,3,4,5]))) #reversed([1,2,3,4,5])= [5, 4, 3, 2, 1]


## 외장함수
# - import 문을 사용하여 외부의 라이브러리에서 제공하는 함수

# 기본 라이브러리
# - sys : 파이썬에서 제공하는 변수들과 함수들을 직접 제어할 수 있게 해주는 모듈
# - pickle : 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
# - os : 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈
# - shutil : 파일을 복사해주는 파이썬 모듈
# - glob : 디렉터리 내의 파일들을 읽어서 리스트로 반환하는 모듈
# - tempfile : 파일을 임시로 만들어서 사용할 때 유용한 모듈
# - time : 시간과 관련된 모듈
# - calendar : 파이썬에서 달력에 관련된 모듈
# - random : 난수(규칙이 없는 임의의 수)를 발생시키는 모듈
# - webbrowser : 시스템 기본 웹 브라우저가 자동으로 실행되게 하는 모듈

import sys
print(sys.path) #['c:\\Users\\Dong\\OneDrive\\Desktop\\GongHanna\\세종사이버대학교\\파이썬기초\\250925', 'c:\\Users\\Dong\\AppData\\Local\\Programs\\Python\\Python313\\python313.zip', 'c:\\Users\\Dong\\AppData\\Local\\Programs\\Python\\Python313\\DLLs', 'c:\\Users\\Dong\\AppData\\Local\\Programs\\Python\\Python313\\Lib', 'c:\\Users\\Dong\\AppData\\Local\\Programs\\Python\\Python313', 'c:\\Users\\Dong\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages']

import glob #외부에 있는 폴더(및 파일) 리스트를 가져옴
print(glob.glob("./*")) #['.\\스크래치', '.\\알기쉬운코딩', '.\\자바스크립트', '.\\질문사항.txt', '.\\파이썬기초', '.\\합격통지서.pdf']

import time
print("time=", time.time()) #time= 1758793906.716302
print("ctime=", time.ctime()) #ctime= Thu Sep 25 18:51:46 2025

import calendar
#calendar.prmonth(년도,월)
calendar.prmonth(2025,9)

import random

print(random.random()) #0.30411481428646037
print(random.randrange(1,46)) #1 ~ (46 - 1), 10

list_temp = ['a', 'b', 'c', 'd', 'e']
random.shuffle(list_temp) #shuffle => 섞어줌
print(list_temp) #['a', 'c', 'e', 'd', 'b']
print(random.choice(list_temp)) #b, choice => 선택
