## 파일 저장 / 화면 출력
# - 텍스트 파일 인코딩 / 디코딩
    # -> 문자코드(아스키, 유니코드(UTF-8(한글))
# - 이진파일 인코딩 / 디코딩
    # -> 미디어별(이미지 파일, 동영상 파일) 저장형식


## open() 함수
# - 파일을 열 때, 파일유형과 사용 방법을 정의함
# - 텍스트 파일 모드 : "r", "w", "a"
# - 이진 파일 모드 : "rb", "wb"
# - 파일은 파일모드에서 정의한 방법으로만 사용 가능함
# - 읽기모드 "r" : 파일들에 대해 입력함수듦나 사용 가능함
# - 쓰기모드 "w" 또는 "a" : 파일에 대해 출력함수들만 사용 가능함

import os
#os.chdir()는 “지금부터 이 폴더를 기준으로 삼겠다”는 뜻
os.chdir(r"C:\Users\Dong\OneDrive\Desktop\GongHanna\세종사이버대학교\2025학년도 2학기\파이썬기초\실습코드\251025")

file5 = open("data.txt", "r", encoding="utf-8")
txt = file5.read()
print("read() 반환값", "="*30)
print(txt)
file5.close()


file5 = open("data.txt", "r", encoding="utf-8")
txt = file5.read(3)
print("read(3) 반환값", "="*30)
print(txt)
file5.close()


file5 = open("data.txt", "r", encoding="utf-8")
print("readline() 반환값", "="*30)
txt = file5.readline()
print(txt)
txt = file5.readline()
print(txt)
txt = file5.readline()
print(txt)
file5.close()


file5 = open("data.txt", "r", encoding="utf-8")
txt = file5.readlines() #list 반환, 라인 단위
print("readline() 반환값", "="*30)
print(txt)
file5.close()


print("data.txt 파일 내용 읽기/출력")
for element in txt :
    print(element, end="")



## for문 이용한 라인 단위 입력처리
# - readline()을 사용하지 않고 라인 단위로 입력파일을 처리할 수 있음
file6 = open("data.txt", "r", encoding="utf-8")
for line in file6:
    print(line, end="")
file6.close()



## 텍스트 파일 출력
# - "w" 또는 "a" 모드 설정
# - write() : 문자열 파일 출력(쓰기)
# - wirteline() : 라인단위 리스트 파일 출력(쓰기)

f1 = open("data.txt", "r", encoding="utf-8")
f2 = open("result.txt", "w", encoding="utf-8")

f2.write("[write()함수 출력]\n")
f2.write("제목: 파일 출력(쓰기) 테스트 ")
f2.write("한줄 입력....")
f2.write("\n\n[writelines() 함수 출력]\n")
list_line = f1.readlines()
f2.writelines(list_line)

f1.close()
f2.close()

print("쓰기 완료")



# 이진 파일 입출력
file_img = open("python_logo.png", "rb")
file_newImg = open("파이썬.png", "wb")

img = file_img.read()
# print(img)

# 파일쓰기 , 파일복사
file_newImg.write(img)

file_img.close()
file_newImg.close()

print("파일 복사 완료...")



## 텍스트 파일에서 리스트 표현
# - 한 학생의 성적 데이터 처리

## 라인 단위
# - 한 학생의 자료, 자료값들을 의미에 따라 동일한 순서로 나열함

## 한 라인에서 데이터 구분
# - 공백, 콤마, 기타 구분자

## 부분 문자열 분리 : rstrip()과 split 함수 사용

data_line = "손흥민, 81, 88, 73"
line = data_line.rstrip()
print("line.rstrip()의 결과: ", line)
# line.rstrip()의 결과:  손흥민, 81, 88, 73


data_line = "손흥민, 81, 88, 73"
line = data_line.split(',')
print("line.splie(',')의 결과: ", line)
#line.splie(',')의 결과:  ['손흥민', ' 81', ' 88', ' 73']



scoreList = []
for i in range(2, len(line)):
    score = int(line[i])
    scoreList.append(score)
print("line의 수치값 리스트: ", scoreList)
#line의 수치값 리스트:  [88, 73]



# 성적 처리 예제
original_file = open("score.csv", "r", encoding="utf-8")
result_file = open("result-score.txt", "w", encoding="utf-8")

result_file.writelines("[성적 처리 결과]\n")

for line in original_file:
    student = (line.rstrip()).split(",")
    total = 0
    for i in range(1, len(student)):
        total = total + int(student[i])
    avg = total / (len(student) - 1)
    studentResult = "이름:%s 총점: %3d 평균:%5.1f\n" % (student[0], total, avg)
    result_file.write(studentResult)

original_file.close()
result_file.close()

print("성적처리 완료...")