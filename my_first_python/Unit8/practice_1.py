##### SECTION 7 - 함수 #####

# 1. 함수 기본
# 1.1 함수 정의
def greet():
    print('Hello')
# 1.2 함수 호출
greet()

# 2. 매개변수
# 2.1 매개변수 전달
def greet(name):
    print('Hello ' + name)
greet('Lee')
# 2.2 매개변수 기본값 설정
def greet(name='unnamed'):
    print('Hello ' + name)
greet()
# 2.3 키-값 쌍 매개변수
def greet(name, age):
    print(name)
    print(age)
greet(age=28, name='lee')
# 2.4 옵션 매개변수
def greet(name, age=''):
    print(name)
    if age:
        print(age)
greet('lee')
greet('lee', 28)

# 3. 리턴값
def add(a, b):
    return a + b

# 4. 심화
# 4.1 임의의 숫자만큼 매개변수 전달
def sum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output

print(sum(3, 5, 1, 3))

# 4.2 임의의 키워드 매개변수
def person(**info):
    print(info)
    for key, value in info.items():
        print(key)
        print(value)

person(name='lee', age=28)

# 5. 모듈
# 5.1 파일 임포트
import add
# 5.2 함수 임포트
from add import add
# 5.3 이름 붙이기
import add as a 
from add import add as a