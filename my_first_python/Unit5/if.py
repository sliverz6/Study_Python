# # 1. 간단한 예제
# # cars = ['audi', 'bmw', 'subaru', 'toyota']

# # for car in cars:
# # 	if car == 'bmw':
# # 		print(car.upper())
# # 	else:
# # 		print(car.title())

# # 2. 조건 테스트

# # 2.1 동일성 체크
# car = 'bmw'
# print(car == 'bmw')

# car = 'audi'
# print(car == 'bmw')

# # 2.2 대소문자 구분
# car = 'Audi'
# print(car == 'audi')

# # 2.3 불일치 체크
# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':
# 	print("Hold the anchovies!")

# # 2.4 숫자 비교하기
# age = 18
# print(age == 18)

# answer = 17

# if answer != 42:
# 	print("That is not the correct answer. Please try again!")

# age = 19
# print(age < 21)
# print(age <= 21)
# print(age > 21)
# print(age >= 21)

# # 2.5 여러 조건 판단하기
# age_0 = 22
# age_1 = 18
# print(age_0 >= 21 and age_1 >= 21)

# age_0 = 22
# age_1 = 18
# print(age_0 >= 21 or age_1 >= 21)

# # 2.6 값이 리스트에 있는지 체크
# requested_topping = ['mushrooms', 'onions', 'pineapple']
# print('mushrooms' in requested_topping)
# print('peperoni' in requested_topping)

# # 2.7 값이 리스트에 없는지 체크
# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'

# if user not in banned_users:
# 	print(user.title() + ", you can post a response if you wish.")

# 3. if 문

# 3.1 간단한 if 문

age = 19
if age >= 18:
	print("You are old enough to vote!")

# 3.2 if - else 문
age = 17
if age >= 18:
	print("You are old enough to vote!")
else:
	print("Sorry, you are too young to vote.")

# 3.3 if - elif - else 문
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10

print("Your admission cost is $" + str(price) + ".")


# 4. 리스트에서 if문 사용하기

# 4.1 특별한 항목이 있는지 체크하기
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry we are out of green peppers right now.")
	else:
		print('Adding ' + requested_topping + '.')

print('\nFinished making your pizza!')

# 4.2 리스트가 비어 있지 않은지 확인하기
requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print('Adding ' + requested_topping + '.')
	print('\nFinished making your pizza!')
else:
	print('Are you sure you want a plain pizza?')

# 4.3 여러 리스트 다루기
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print('Adding ' + requested_topping + '.')
	else:
		print('Sorry we don\'n have ' + requested_topping + '.')
	
print('\nFinished making your pizza!')