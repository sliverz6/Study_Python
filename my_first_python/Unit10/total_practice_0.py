# ##### SECTION 7 - 함수 #####

# # 1. 함수 기초

# # 1.1 함수 정의
# def greet():
#     """간단한 인사를 합니다."""
#     print('Hello')

# greet()

# # 1.2 매개변수 전달
# def greet(name):
#     """간단한 인사를 합니다."""
#     print('Hello ' + name)

# greet('Lee')
 
# # 1.3 리턴
# def add(a, b):
#     return a + b

# print(add(1, 2))

# # 2. 매개변수

# # 2.1 기본값
# def add(a, b=2):
#     return a + b

# print(add(1))
# print(add(2, 3))

# # 2.2 키워드 매개변수
# def greet(name, age):
#     print('Name: ' + name)
#     print('Age: ' + str(age))

# greet(age=28, name='Lee')

# # 2.3 동적 매개변수
# def sum(*numbers):
#     output = 0
#     for number in numbers:
#         output += number
#     return output

# print(sum(1, 2))
# print(sum(1, 2, 3, 4, 5))

# # 2.4 동적 매개변수2 (키-값 쌍)
# def show_info(**info):
#     for key, value in info.items():
#         print('Key: ' + key)
#         if type(value) == 'int':
#             print('Value: ' + str(value))
#         else:
#             print('Value: ' + value)

# show_info(name='Lee')

##### SECTION 8 - 클래스 #####

# 1. 클래스 기초

# 1.1 클래스 만들기
class Person():
    """사람 클래스"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print('Hello, my name is ' + self.name.title())

# 1.2 인스턴스 만들기
person = Person('Lee Seungjae', 28)

# 1.3 속성 접근
print(person.name)

# 1.4 메서드 사용
person.greet()

# 2. 클래스 다루기

# 2.1 인스턴스 기본값 설정
class Person():
    """사람 클래스"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.country = 'Korea'
    
    def greet(self):
        print('Hello, my name is ' + self.name.title())

# 3. 상속
class Man(Person):
    """남자 클래스"""
    def __init__(self, name):
        super().__init__(name, 28)
        self.gender = 'Male'

man = Man('Lee Seungjae')
print(man.country)
print(man.age)
