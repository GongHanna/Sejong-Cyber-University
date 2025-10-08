## 객체(object)
# - 실생활에 존재하는 실제적인 물건 또는 개념임
    # -> 객체는 속성과 기능을 가짐

# 객체 : 실생활에 존재하는 사물 또는 개념 (예 : 축구선수)
# 속성 : 객체가 가지고 있느 변수(예: 선수이름, 팀 이름, 등번호)
# 기능 : 객체가 실행하는 함수=메소드 (예: 공을 찬다, 달린다, 패스한다)


## 객체 지향 프로그래밍(Object Oriented Programming, OOP)
# - 객체를 생성할 수 있도록 클래스를 정의하는 것
    # -> 클래스를 이용하여 객체를 생성하고 객체가 가지는 속성과 메소드를 이용하여 프로그래밍함
# - 객체의 개념을 활용하여 프로그램으로 표현하는 기법
# - 재활용의 관점으로 코드를 만들어 놓고 쓰는 방법임
    # - 변수와 함수를 묶어서 하나의 객체로 만들어 사용함
# => 함수처럼 어떤 기능을 함수 코드로 묶어 두는 것이 아니라, 특정 기능을 수행하는 하나의 단일 프로그램을 객체라고 하는 코드로 만들어 다른 프로그래머가 재사용할 수 있도록 함


## 클래스(class)
# - 객체는 하나의 프로그램에서 여려 개가 사용될 수 있으므로 객체들을 위한 설계도를 만들어야 함
# - 객체가 가져야 할 기본 정보를 담은 코드, 일종의 설계도 코드

##인스턴스(객체)
# - 클래스를 기반으로 생성한 객체
    # DOG 클래스
    # - 속성(변수) : 품종, 크기, 나이, 색상
    # - 행동(기능, 메서드) : 먹는다, 잠을 잔다, 뛴다


## 클래스를 정의하는 구조
# class -> 클래스 예약어
# footballPlayer -> 클래스 이름
# () -> 상속받는 객체
    # - 예약어인 class를 코드의 맨 앞에 입력함
    # - 만들고자 하는 클래스 이름을 작성함
        # -> 이름을 작성할 때는 대문자로 시작함
    # - 상속받아야 하는 다른 클래스의 이름을 괄호 안에 넣음


## 축구선수 클래스 정의
# 속성정의, 속성(변수) 선언 방법
    # __init__(매개변수) 
    # 예약함수 사용 : 클래스에서 사용할 변수를 정의하는 함수
# class FootballPlayer():
#     def __init__(self, name, team, back_number): # self는 객체 자신을 가리킴(필수로 작성해야 함)
#         self.name = name
#         self.team = team
#         self.back_number = back_number


## self
# - 객체의 그 자체를 의미함 -> 객체 자기 자신을 참조하는 매개변수임
# - 다른 객체지향 언어는 self 안보이게 전달하지만, 파이썬은 클래스의 메소드를 정의할 때 self를 명시해서 정의함
# - 메소드를 호출할 때 self는 자동으로 전달함
    # -> self를 사용하믕로 클래스 내에 정의한 멤버에 접근할 수 있음

#class FootballPlayer():
#    #속성정의
#    def __init__(self, name, team, back_number): 
#         # 생성자 : 속성을 초기화, 변수에 처음 값을 넣어줌
#         self.name = name
#         self.team = team
#         self.back_number = back_number
## 객체 생성
#p = FootballPlayer("Hanna", "Dream", 77) 
#print(p.name) #Hanna
#print(p.team) #Dream
#print(p.back_number) #77



## 메소드
# - 클래스에서 정의하는 함수
    # -> 클래스 내부에서 다양한 기능을 함수로 정의할 수 있음

# 클래스 내부에서 함수를 정의한느 방법은 동일함
# - 차이점은 매개변수 앞에 self를 반드시 넣어야 함

# class FootballPlayer():
#     def __init__(self, name, team, back_number): 
#          self.name = name
#          self.team = team
#          self.back_number = back_number

#     #기능정의
#     def show_info(self):
#          print("==========선수정보==========")
#          print("이름",self.name)
#          print("팀",self.team)
#          print("등번호",self.back_number)

# p = FootballPlayer("Donna", "Queen", 777)
# p.show_info() 
#==========선수정보==========
#이름 Donna
#팀 Queen
#등번호 777



## __str__(self) 메소드
# - print(객체이름)을 사용해서 클래스 내부에서 정의한 정보를 출력할 때 정의해서 사용
class FootballPlayer():
    #속성정의
    def __init__(self, name, team, back_number): 
         self.name = name
         self.team = team
         self.back_number = back_number

    #기능정의
    def show_info(self):
         print("==========선수정보==========")
         print("이름",self.name)
         print("팀",self.team)
         print("등번호",self.back_number)

    def __str__(self):
         return "{0} (팀: {1}, 등번호: {2})".format(self.name, self.team, self.back_number)

p = FootballPlayer("Dana", "토트넘", 9)
print(p) #Dana (팀: 토트넘, 등번호: 9)