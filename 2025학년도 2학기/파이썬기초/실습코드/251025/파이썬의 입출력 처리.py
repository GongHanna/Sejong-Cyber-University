## 파일 열기
# 변수 = open("파일명", "파일모드")
# - 변수 : 프로그램 내부에서 사용할 파일(파일명)의 식별자
# - 파일명 : 운영체제에서 사용하는 파일명, 파일의 경로 포함하는 이름
# - 파일모드 : 파일 사용 방법


## 파일모드
# - 읽기 모드 (r, r+, rb)
    # -> 입력파일들은 프로그램의 실행 전에 미리 준비해야 함
# - 쓰기 모드 ('w', 'a' 모드)
    # -> 출력파일들은 없으면 새로 생성해서 출력함
# - 'w' 모드
    # -> 기존 파일의 내용을 무시하고 새로 작성함, 즉 기존 파일내용 삭제
# - 'a' 모드
    # -> 기존 파일(있는 경우) 끝에 추가해서 출력함

import os
#os.chdir()는 “지금부터 이 폴더를 기준으로 삼겠다”는 뜻
os.chdir(r"C:\Users\Dong\OneDrive\Desktop\GongHanna\세종사이버대학교\2025학년도 2학기\파이썬기초\실습코드\251025")

# 파일 열기
file1 = open("data.txt", "r", encoding='utf-8')

print("data.txt 파일 읽고 화면에 출력하기")
print("="*40)

tempStr = file1.read()
# read()는 파일의 내용 전체를 문자열로 반환

print(tempStr)
print("="*40)

file1.close() # 파일을 다 사용한 후에는 닫아주어야 함


# 파일 쓰기
file2 = open("./write1.txt", "w", encoding="utf-8")

msg = input("메시지를 입력하세요.\n")

file2.write(msg)
file2.close()


# 파일에 추가 쓰기
file3 = open("./write1.txt", "a", encoding="utf-8")

msg = input("메시지를 입력하세요.\n")

file3.write("\n")
file3.write(msg)

file3.close()


# with 블록을 이용한 파일 처리
# - 파일을 사용하고 나면 반드시 close 해주어야 함
# - 출력파일의 close 생략
    # -> 출력 내용이 실제 파일에 반영되지 않음 -> 반드시 폐쇄해야 함

# with 블록 이용 : 블록이 끝날 때 자동으로 close() 실행


with open ("./data.txt", "r", encoding="utf-8") as file4:
    print("data.txt 파일을 읽고 화면에 출력하기")
    print("="*40)

    tempStr = file4.read()

    #read()는 파일의 내용 전체를 문자열로 반환
    print(tempStr)
    print("="*40)