# 자료형이란?
#  - 프로그램에서 나타낼 수 있는 데이터의 종류
#  - 할당 받는 메모리 공간의 크기는 변수의 자료형(Data Type)에 의해 결정됨 -> 변수에 저장될 자료의 형에 따라 구분

# 동적 타이핑이란?
#  - 변수의 메모리 공간을 생성하는 시점이 프로그램이 실행되는 시점에 생성되는 것을 의미
# 예) 컴파일 언어의 경우 : int num = 10과 같이 실행 이전에 변수의 타입을 정의
# 예) 파이썬의 경우 : num = 8과 같이 선언함
#  - 프로그램이 실행되는 시점인 8의 값이 저장될 때 인터프리터가 정수(int)임을 판단해서 메모리의 타입을 결정함
#  - 파이썬은 프로그램의 실행 시점에 동적으로 판단해서 적용되는 것을 동적으로 자료형을 결정함

# 파이썬의 데이터 타입 (자료형)
#  - 숫자형 : 정수(int), 실수(float)
#  - 문자형 : 문자열(str)
#  - 논리형 : 불린(boolean) - True/false 두개의 값을 가짐
#  - 컬렉션형 : 리스트(list), 튜플(tuple), 집합(set), 딕셔너리(dictionary)
#  - None

# list : 순서가 있는 자료형으로, 다양한 객체들을 멤버로 가질 수 있는 자료형
# 예) member = ["LONDON", 'SON', 8.5, 30, True]

# tuple : list와 같으나 내용의 변경이 허용되지 않는 자료형, ()을 사용함
# 예) member = ("LONDON", 'SON', 8.5, 30, True)

# dict : 순서가 없는 자료형으로 키와 값으로 이루어진 자료를 저장하는 자료형, 값은 중복될 수 있으나, 키는 중보고딜 수 없음, {:}를 사용함
# 예) age = {'Kim':22, 'Park:21', 'Lee':22, 'Son':30}

# set : 순서가 없는 자료형으로 값의 중복을 허용하지 않음, {}를 사용함
# 예) grade={1,2,3,4}, item={40,3.14,"KIM", False}

# 자료형을 구분하는 이유?
#  - 자로형에 따라 컴퓨터 내부의 저장방식과 처리방법이 다름 -> 서로 다른 자료형들보는 같은 자료형들의 처리하는 것이 효율적
#  - 적절한 자료형의 선택이 중요! -> 가능하면 동일한 자료형들끼리 연산 수행하는 것이 좋음

# 자료형의 확인
#  - type() 함수를 사용
#  - 변수가 bool(불형), int(정수), float(실수), str(문자열), 어떤 자료형으로 생성된 것을 확인할 수 있음

bool_var1 = True
bool_var2 = False
int_var = 100
float_val = 3.14
str_val = '안녕하세요'
list_val = ['JIN', 20]
tuple_val = ('JIN', 20)
dict_val = {'name': 'JIN', 'age': 20}
set_val = {'JIN', 20}

print(type(bool_var1))  # <class 'bool'>
print(type(bool_var2))  # <class 'bool'>
print(type(int_var))  # <class 'int'>
print(type(float_val))  # <class 'float'>
print(type(str_val))  # <class 'str'>
print(type(list_val))  # <class 'list'>
print(type(tuple_val))  # <class 'tuple'>
print(type(dict_val))  # <class 'dict'>
print(type(set_val))  # <class 'set'>


## 정수형(Integer Type)
#  - 자연수를 포함해 0, 1, 2, -1, -2와 같이 값의 영역이 정수로 한정된 값
#  - 데이터를 선언할 때는 data = 1과 같은 방식으로 선언
#  - 파이썬의 인터프리터가 메모리 영역에 필요한 공간을 확보 후 데이터에 저장
# 정수형 상수 : 10진수, 2진수, 8진수, 16진수 사용 가능

# 숫자형 타입: int
number = 100
print(type(number)) #<class 'int'>


## 실수형(Floating-Point Type)
#  - 3.14, 180.5와 같이 소수점이 포함된 값
#  - 저장되는 값이 정수형 데이터라도 9.0으로 입력하면 인터프리터는 실수형 데이터로 해석 후 저장

# 숫자형 타입: float
number = 9.0
print(type(number)) #<class 'float'>


## 문자형(String Type)
#  - 파이썬에서는 보통 따옴표(작은, 큰)에 들어간 문자데이터들을 문자형 데이터라고 함
#  - 하나 이상의 문자를 저장하면 문자열(텍스트)
#  - 큰따옴표를 사용하더라고 print()로 출력하면 작은따옴표로 표시함 -> 문자열은 리스트와 비슷한 부분이 많음

str_hello = "안녕하세요"
str_hello
print(str_hello) #안녕하세요
print(type(str_hello)) #<class 'str'>

str_a = "\"안녕하세요\""
str_b = '\'안녕하세요\''
print(str_a, str_b) #"안녕하세요" '안녕하세요'

str_c = """안녕하세요
반갑습니다."""  # """(큰따옴표 3개) :  입력한 형태 그대로 출력
str_c # '안녕하세요\n반값습니다.'
print(str_c) 
#안녕하세요
#반갑습니다.

# 문자열도 리스트와 마찬가지로 덧셈(+)를 사용해 연결
# 곱셈(*)를 사용해 문자열을 반복

str_d = "안녕하세요." + "반갑습니다."
print(str_d) #안녕하세요.반갑습니다.

str_3 = "안녕하세요." * 3
print(str_3) #안녕하세요.안녕하세요.안녕하세요.


## 불린형(Booolean Type)
#  - 논리형이라고도 함
#  - 참(True) 또는 거짓(False)을 표현할 때 사용, 파이썬에서는 대문자로 시작

check = True
print(check) #True
print(type(check)) #<class 'bool'>

result_1 = 10 == 10
print(result_1) #True

result_2 = 10 > 100
print(result_2) #False


## 형변환
#  - 변수의 자료형을 바꾸는 것
#  - int(), float(), str() 함수를 사용

# int() : 다른 데이터형을 정수로 변환 / int("100") -> 100
# float() : 다른 데이터형을 실수로 변환 / float(3) -> 3.0
# str() : 다른 데이터형을 문자열로 변환 / str(12345) -> "12345"

# 자료형 변환
str_to_num1 = int('100')
print(str_to_num1, type(str_to_num1)) #100 <class 'int'>

str_to_num2 = float('100')
print(str_to_num2, type(str_to_num2)) #100.0 <class 'float'>

num_temp = 1000 #정수, int 타입
num_to_str = str(num_temp)
print(num_to_str, type(num_to_str)) #1000 <class 'str'>




## 리스트(List)
#  - 하나의 변수에 여러 값을 저장하는 자료형
#  - 하나씩 사용하던 박스(변수)를 한 줄로 붙여 놓은 것
#  - 박스(변수)를 한 줄로 붙인 후 전체에 이름(list)을 지정
#  - 리스트의 요서 각각은 list[0], list[1], list[2], list[3]처럼 인덱스 번호를 붙여 사용 / 순서를 가지고 있음

## 리스트의 개념과 필요성
#  - 입력해서 사용해야 할 변수가 100개하면 변수를 선언하고 할당하는 것이 굉장히 힘듦
#  - 리스트를 사용하면 보다 효과적으로 처리가 가능한 경우 -> 학생 300명의 점수에 학점을 부여해야 하는 경우

## 리스트 선언 방법
#  - 대괄호 안에 값을 선언함
#  - 리스트명(변수명) = [값1, 값2, 값3, ...]

list = [10,20,30,40]
print(list) #[10, 20, 30, 40]
print(type(list)) #<class 'list'>


## 리스트 - 인덱싱(Indexing)
#  - 리스트에 저장되어 있는 값에 접근하기 위해 이 값의 상대적인 주소(offset)를 사용한는 것
#  - 상대적인 주소를 인덱스 값이라고 함
#  - 인덱스 값은 0 ~ 리스트의 길이-1 까지 범위를 가짐
# - len()함수는 리스트의 길이, 즉 리스트 안에 있는 요소의 개수를 반환함

print(len(list)) #4, 리스트의 길이: 리스트가 가지는 요소의 개수
print(list[0]) #10
print(list[1]) #20
print(list[2]) #30
print(list[3]) #40
# print(list[4]) IndexError: list index out of range, 변수 list가 가지고 있는 인데스의 번호는 3까지 밖에 없음

## 리스트 - 슬라이싱(Slicing)
#  - 리스트에서 파생된 기능 중 하나
#  - 리스트의 인덱스 기능을 사용하여 전체 리스트에서 일부를 잘라내어 사용
#  - 앞에서 선언한 리스트는 0~3까지의 인덱스를 가진 4개의 요소를 가지고 있음
#  - 슬라이싱의 기본 문법: 변수명[시작 인덱스 : 마지막 인덱스+1]
list = [10,20,30,40]
print(list[0 : 4]) #[10, 20, 30, 40]
print(list[:4]) #[10, 20, 30, 40], 시작 인덱스를 생략한 경우 0부터 시작함
print(list[0:]) #[10, 20, 30, 40], 마지막 인데스를 생략한 경우 마지막 요소까지 출력
print(list[2:4]) #[30, 40]
print(list[2:]) #[30, 40]


## 리스트 - 리버스 인덱스(Reverse Index)
#  - 마지막 값부터 -1을 할당하여 첫번재 값까지 역순으로 진행하는 방식
list = [10,20,30,40]
print(list[-4:]) #[10, 20, 30, 40]


## 리스트 - 증가값(Step)
#  - 슬라이싱에서는 시작 인덱스와 마지막 인덱스 외에도 마지막 자리에 증가값을 사용
#  - 변수명[시작 인덱스: 마지막 인덱스 : 증가값]
list = [10,20,30,40]
print(list[0:4:2]) #[10, 30]
print(list[::2]) #[10, 30], 시작과 마지막 인덱스 값이 생략된 경우 시작부터 마지막까지 포함
print(list[::-1]) #[40, 30, 20, 10], -1은 역순으로 데이터 출력


## 리스트 덧셈 연산
# - 덧셈 연산으로 두 리스트를 합치면, 각각의 리스트가 하나의 리스트로 합쳐져서 출력됨
list_a = [10,20,30,40]
list_b = [50,60,70,80]
list_total = list_a + list_b
print(list_total) #[10, 20, 30, 40, 50, 60, 70, 80]


## 리스트 곱셈 연산
#  - 리스트에 n을 곱했을 때 해당 리스트를 n배만큼 늘려줌
list_result = list_a * 3
print(list_result) #[10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40]


## 리스트 in 연산
#  - 포함 여부를 확인하는 연산으로 하나의 값이 해당 리스트에 들어있는지 확인할 수 있음
print(130 in list_a) #False
print(50 in list_b) #True


## 리스트 조작함수
#  append() : 리스트 맨 뒤에 항목 추가, 리스트명.append(값)
#  pop() : 리스트 맨 뒤의 항목 삭제, 리스트명.pop()
#  sort() : 리스트 항목을 정렬, 리스트명.sort()
#  reverse() : 리스트 항목의 순서를 역순으로 만듦, 리스트명.reverse()
#  index() : 지정한 값을 찾아 해당 위치 반환, 리스트명.index(찾을 값)
#  insert() : 지정된 위치에 값을 삽입, 리스트명.insert(위치, 값)
#  remove() : 리스트에서 지정한 값 삭제, 단 지정한 값이 여러개면 첫번째 값만 지움, 리스트명.remove(지울 값)
#  extend() : 리스트 뒤에 리스트 추가, 리스트의 더하기(+) 기능과 동일, 리스트명.extend(추가할 리스트)
#  count() : 리스트에서 해당 값의 개수를 셈, 리스트명.count(찾을 값)
#  clear() : 리스트의 내용을 모두 지움, 리스트명.clear()
#  del() : 리스트에서 해당 위치의 항목 삭제, del(리스트명[위치])
#  len() : 리스트에 포함된 전체 항목의 개수를 셈, len(리스트명) 
#  copy() : 리스트의 내용을 새로운 리스트엥 복사, 새리스트 = 리스트명.copy()
#  sorted() : 리스트의 항목을 정렬해서 새로운 리스트에 대입, 새리스트 = sorted(리스트)

list_num = [10,20,30,40]
list_num.append(100)
print(list_num) #[10, 20, 30, 40, 100]

list_num.extend([1000,2000])
print(list_num) #[10, 20, 30, 40, 100, 1000, 2000]

list_num.insert(0,99) #인데스 위치 0에 99 추가
print(list_num) #[99, 10, 20, 30, 40, 100, 1000, 2000]

list_num.remove(99)
print(list_num) #[10, 20, 30, 40, 100, 1000, 2000]

del list_num[4] #특정 인덱스 위치의 값 삭제
print(list_num) #[10, 20, 30, 40, 1000, 2000]


## 튜플
#  - 리스트와 같이 여러 타입의 데이터들으 ㄹ순서에 따라 나열한 것
#  - 리스트와는 달리 원소들의 추가, 삭제, 변경이 불가능함

list_score = (100,90,60,80,70)
print(list_score) #(100, 90, 60, 80, 70)
print(type(list_score)) #<class 'tuple'>

# 튜플 생성 시 소괄호 생략 가능
list_score_a = 10,90,60,80,70
print(list_score_a) #(100, 90, 60, 80, 70)
print(type(list_score_a)) #<class 'tuple'>

# 튜플의 삭제는 del()를 사용
# del list_score_a
print(list_score_a) #NameError: name 'list_score_a' is not defined.

# 튜플의 활용
#  - 리스트처럼 튜플명[인덱스] 사용 가능
#  - 덧셈, 곱셈 연산도 가능


## 집합(Set)
#  - 여러 유형의 데이터들을 순서에 관계없이 모아둔 것, 중복 불가능
#  - 수학의 집합연산(합집합, 교집합, 차집합 등) 지원함

x = {10,30,50}
y = {30,20,50,40}
print(x | y) #{50, 20, 40, 10, 30} , 합집합
print(x & y) #{50, 30}, 교집합
print(x - y) #{10}, 차집합


## 딕셔너리(Dictionary)
#  - "키:값" 형태의 데이터들의 집합
#  - 중괄호 내에 "키:값" 형태의 원소들을 콤마(,)로 구분해서 저장
#  예) {"name": "손흥민", "grade": 4, "major": "축구"}
#  - 여러 정보의 하나의 변수로 표현할 때 유용

# 딕셔너리 - 키(key)
#  - 데이터 값을 구별하는 식별자
#  - 원소 값(데이터)를 참조할 때 인덱스(식별 키)로 사용함

student = {"name": "손흥민", "grade": 4, "major": "축구"}
print(student) #{'name': '손흥민', 'grade': 4, 'major': '축구'}
print(student['name'],student['major'],student['grade']) #손흥민 축구 4

# 딕셔너리에 데이터 추가
#  - 딕셔너리명[키]=값 형식으로 추가
student['age'] = 30
print(student) #{'name': '손흥민', 'grade': 4, 'major': '축구', 'age': 30}

# 딕셔너리에 데이터 삭제
#  - del 딕셔너리명[키] 형식으로 삭제
del student['age']
print(student) #{'name': '손흥민', 'grade': 4, 'major': '축구'}

# 딕셔너리의 활용
#  - 딕셔너리명.get(키) 함수 : 키로 값에 접근 가능
#  - 딕셔너리명.items() 함수 : 키와 값의 쌍을 튜플 형태로도 구할 수 있음
#  - 딕셔너리명.values() 함수 : 딕셔너리의 모든 값을 리스트로 만들어 반환함 -> 해당 키가 있는 지 없는지는 in을 사용해 확인
print(student.get('name')) #손흥민
print(student.keys()) #dict_keys(['name', 'grade', 'major'])
print(student.items()) #dict_items([('name', '손흥민'), ('grade', 4), ('major', '축구')])
print(student.values()) #dict_values(['손흥민', 4, '축구'])
print('name' in student) #True


# None
#  - 자료값 없음을 나타냄
#  - 변수를 정의할 때, 또는 프로그램의 실행 도중 변수값을 None으로 지정함
var_temp = None
print(var_temp) #None
print(type(var_temp)) #<class 'NoneType'>