print("모듈 생성 테스트를 위한 테스트 모듈 파일입니다.")

def test_print() :
    print("test print ........")

def add(n1, n2) :
    return n1+n2

pi = 3.14

print(__name__)
if __name__ == "__main__" :
    print("__main__일 때만 출력 ...")
    test_print()
# 해당 조건문 내 코드는 test.py가 최상위 모듈로 사용될 때만 실행
    # -> 모듈로 활용될 때는 무시