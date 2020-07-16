##### SECTION 7 - 함수 #####

# 1. 함수 기본

# 1.1 함수 정의
# def greet_user():
#     print('Hello')

# greet_user()

# 1.2 함수 매개변수
# def greet_user(username):
#     print('Hello, ' + username.title() + '!')

# greet_user('jesse')

# 2. 여러 매개변수 전달

# 2.1 순서대로 매개변수
# def describe_pet(animal_type, pet_name):
#     print('\nI have a ' + animal_type + '.')
#     print('My ' + animal_type + '\'s name is ' + pet_name.title() + '.')

# describe_pet('hamster', 'harry')

# 2.2 키워드 매개변수
# def describe_pet(animal_type, pet_name):
#     print('\nI have a ' + animal_type + '.')
#     print('My ' + animal_type + '\'s name is ' + pet_name.title() + '.')

# describe_pet(pet_name = 'harry', animal_type = 'hamster') # 키-값 쌍으로 전달

# 2.3 기본값 설정
# def describe_pet(pet_name, animal_type = 'dog'):
#     print(pet_name)
#     print(animal_type)
# describe_pet(pet_name = 'whille')

# 3. 리턴값

# 3.1 단순한 값 리턴
# def add(a, b):
#     return a + b
# print(add(1, 2))

# 3.2 매개변수를 옵션으로 만들기
# def greet(name = ''):
#     if name:
#         print('Hello, ' + name)
#     else:
#         print('Hello')

# greet()
# greet('Lee')

# 4. 매개변수를 임의의 숫자만큼 전달하기
# def make_number_list(*numbers):
#     return [numbers]

# list_0 = make_number_list(1, 2)
# list_1 = make_number_list(1, 2, 3, 4, 5)

# print(list_0)
# print(list_1)

# # 4.1 임의의 키워드 매개변수 사용하기
# def person(location, **info):
#     print(location)
#     for key, value in info.items():
#         print(key)
#         print(value)

# location = 'korea'
# person(location, name = 'lee', age = 28)

# 5. 함수를 모듈에 저장
# 함수를 분리해서 사용할 수 있다

# 5.1 모듈 전체를 임포트
import add

print(add.add(1, 2))

# 5.2 특정 함수만 임포트
from add import add
print(add(2, 3))

# 5.3 임포트한 함수에 이름 붙이기
from add import add as a
print(a(4, 3))

# 5.4 모듈에 이름붙이기
import add as ad 
print(ad.add(4, 3))6