## 학생 관리 프로그램

#1. 학생 클래스 정의
    # - 이름, 국어, 영어, 수학, 과학 점수를 저장 = 속성, 변수
    # - 총점과 평균 값을 구하는 기능 = 메서드

# 클래스 선언
class Student:
    # __init__ : 생성자, 속성을 초기화 해줌
    # self : 자기 자신을 가르키는 변수
    def __init__(self, name, korean, math, english, science):
        # 인스턴스 변수
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def get_sum(self):
        return self.korean + self.math + \
            self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())
    
    # __eq__ : 비교, 같을 때
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    # __ne__ : 비교, 같지 않다
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    # __gt__ : 비교, 왼쪽 기준으로 크다
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    # __ge__ : 비교, 왼쪽 기준으로 크거나 같다
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    # __lt__ : 비교, 왼쪽 기준으로 작다
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    # __le__ : 비교, 왼쪽 기준으로 작거나 같다
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()
    
# 학생 리스트를 선언
students = [
    Student("AAA",87,98,88,95),
    Student("BBB",92,98,96,98),
    Student("CCC",76,96,94,90),
    Student("DDD",98,92,96,92),
    Student("EEE",95,98,98,98),
    Student("FFF",64,88,92,92)
]

# 학생을 한명씩 반복
print("이름", "총점", "평균", sep="\t")
for student in students:
    #출력
    print(student.to_string())
#이름    총점    평균
#AAA     368     92.0
#BBB     384     96.0
#CCC     356     89.0
#DDD     378     94.5
#EEE     389     97.25
#FFF     336     84.0


# 학생 비교 예제 코드
# 학생을 선언
student_a = Student("SON",87,98,88,95) #368
student_b = Student("KING",92,98,96,98) #384

print("student_a == student_b", student_a == student_b) #student_a == student_b False
print("student_a != student_b", student_a != student_b) #student_a != student_b True
print("student_a > student_b", student_a > student_b) #student_a > student_b False
print("student_a >= student_b", student_a >= student_b) #student_a >= student_b False
print("student_a < student_b", student_a < student_b) #student_a < student_b True
print("student_a <= student_b", student_a <= student_b) #student_a <= student_b True