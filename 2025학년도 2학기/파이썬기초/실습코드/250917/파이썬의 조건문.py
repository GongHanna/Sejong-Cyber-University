## if문
# - 조건문에는 if 라는 키워드를 사용
# - if 다음에는 조건이 존재해야 함
# - if문의 끝에는 콜론(:)을 입력함
# - if문의 조건이 True일때 실행되는 문장은 4칸 들여쓰기 해야함
# - 실행하는 명령문은 들여쓰기 될 때 시작됨, 들여쓰기가 되지 않은 명령문을 만나면 반복 구문이 종료됨

# if expression(논리값) :
#    statement(s)

# expression
#  - 조건식 또는 논리연산식(boolean)의 경우 : 표현식(expression)이 사실이면 True를 반환해 if문 안쪽 문장이 실행, 거짓이면 False를 반환해 다음으로 진행
#  - 변수 또는 리터럴(value)의 경우 : 0이 아니거나 null이 아니면 -> True, 0이거나 null이면 -> False
num = 20
if num > 10 :
    print("num은 10보다 큰 숫자입니다") #num은 10보다 큰 숫자입니다, True
if num < 10 :
    print("num은 10보다 작은 숫자입니다") #False

age = 0
if age :
    print(age) # False

age = 20
if age :
    print(age) #20, True



## if~else 문
# - if 조건의 결과가 거짓일 때 처리할 수 있느 구문을 제공 -> True일 때뿐만 아니라 Fasle일 때도 필요한 문장을 처리할 수 있음

# if expression(논리값) :
#     statement(s)
# else :
#    statement(s)

age = 25
if age > 18 :
    print("성인입니다.") #성인입니다. True
else :
    print("미성년입니다.")



## if문의 중첩과 if~else
# - if 구문에서 참일 때 거짓일 때 처리되는 구문 안에 또 다른 if 구문을 사용하는 형태
# if expression 1 :
#   statement(s)
#   if expresstion 2 :
#     statement(s)
#   elif expresstion 3 :
#     statement(s)
#   else
#     statement(s)
#   elif expresstion 4 :
#     statement(s)
#   else :
#     statement(s)

# 학점을 판별하는 제어문
score = 55
if score >= 90 :
    print("A학점")
else :
  if score >= 80 :
      print("B학점")
  else :
    if score >= 70 :
        print("C학점")
    else :
      if score >= 60 :
          print("D학점")
      else :
          print("F학점") #F학점

score = 95
if score >= 90 :
  print("A학점") #A학점
elif score >= 80 :
    print("B학점")
elif score >= 70 :
    print("C학점")
elif score >= 60 :
    print("D학점")
else :
    print("F학점")



# 숫자를 입력 받아 짝수, 홀수를 판별하는 프로그램
#str = input("숫자를 입력하세요>>>")
#num = int(str)
#
#if num % 2 ==0 :
#    print("입력한 숫자는 짝수입니다.") #True
#else :
#    print("입력한 숫자는 홀수입니다.") #False


# 숫자를 입력받아 양수, 음수, 0을 판별하느 프로그램
#num = int(input("숫자를 입력하세요>>>"))
#if num > 0 :
#    print("입력한 숫자는 양수입니다")
#elif num < 0 :
#    print("입력한 숫자는 음수입니다")
#else :
#    print("입력한 숫자는 0 입니다")


# 15세 미만 혹은 65세 이상의 경우 무료예방접종 가능 메시지 출력
#age = int(input("나이를 입력하세요>>>"))
#if age > 15 or age >= 65 :
#    print("무료예방접종이 가능합니다")
#else :
#    print("무료예방접종 대상이 아닙니다")



# 특정 연도 건강검진 대상 여부 판별 및 검진 종류 확인
# - 매개변수로 올해 연도와 태어난 해 연도를 전달받음
# - 대한민국 성인(20세)의 경우 무료로 2년마다 건강검진을 받을 수 있음
# - 짝수 해에 태어난 사람은 올해가 짝수년이라면 검사 대상이 됨
# - 40 이상의 경우는 암 검사도 무료로 검사를 할 수 있음

year = int(input("올해 년도를 입력하세요>>>"))
birth_year = int(input("태어난 연도를 입력하세요>>>"))
age = year - birth_year

# 올해가 짝수 연도라면 태어난 연도도 짝수 판별
check1 = year % 2 == birth_year % 2
# 올해가 짝수 연도라면 태어난 연도도 짝수 판별
check2 = (year + birth_year) % 2 == 0

if check1 and age >= 20:
    print("건강검진 대상자입니다.")
    if age >= 40 :
        print("무료 암검사 대상자입니다.")
else :
    print("건강검진 대상자가 아닙니다.")