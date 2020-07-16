#############################
##### SECTION 5 - if 문 #####
#############################

##### 1. 조건 테스트 #####

# 1.1 일치 체크
car = 'bmw'
print(car == 'bmw')
print(car == 'Bmw') # 대소문자 구분한다

# 1.2 불일치 체크
print(car != 'audi')

# 1.3 숫자 비교
age = 28
print(age > 20)
print(age >= 20)
print(age < 20)
print(age >= 20)

# 1.4 여러 조건 비교
print(age > 20 and age < 30)
print(age > 20 or age < 30)

# 1.5 리스트에 값이 있는지 체크
fruits = ['apple', 'banana', 'watermelon']
print('apple' in fruits)

# 1.6 리스트에 값이 없는지 체크
print('orange' not in fruits)

# 1.7 불리언 표현식
active = True
active = False

##### 2. if 문 #####

# 2.1 기본 if 문
answer = 7
if answer != 8:
    print('Wrong')

# 2.2 if - else 문
time = 21
if time <= 12:
    print('오전입니다.')
else: 
    print('오후입니다.')

# 2.3 if - elif - else 문
age = 28
if age < 10:
    price = 5
elif age < 20:
    price = 10
else :
    price = 15

print(price)

##### 3. 리스트에서 if 문 #####

# 3.1 요소 존재 여부 체크
cars = ['bmw', 'audi', 'ferrari']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 3.2 빈 리스트인지 체크
cars = []

if cars:
    print(cars)
else:
    print('empty list.')