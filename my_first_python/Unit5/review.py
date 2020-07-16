##### if 문

# 1. 간단한 예제
# cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())


# 2. 조건 테스트

# 2.1 동일성 테스트

# 2.2 일치하는지 체크할 때 대소문자 무시하기

# 2.3 불일치 체크하기
# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

# 2.4 숫자 비교하기
# answer = 17

# if answer != 42:
#     print("That is not the correct answer. Please try again!")

# 2.5 여러 조건 체크하기

# 2.6 값이 리스트에 있는지 체크하기

# 2.7 값이 리스트에 없는지 체크하기
# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'

# if user not in banned_users:
#     print(user.title() + ", you can post a response if you wish.")

# 2.8 불리언 표현식


# 3. if 문

# 3.1 단순한 if 문
# age = 19
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")

# 3.2 if-else 문
# age = 17
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# else: 
#     print("Sorry, you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")

# 3.3 if-elif-else 문
# age = 12

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# else:
#     price = 5

# print("Your admission cost is $" + str(price) + ".")

# 3.4 elif 블록 여러 개 쓰기

# 3.5 else 블록 생략하기

# 3.6 여러 조건 테스트하기
# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")

# print("\nFinished making your pizza!")


# 4. 리스트에서 if 문 사용하기

# 4.1 특별한 항목이 있는지 체크하기
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry we are out of green peppers right now.")
#     else:
#         print("Adding " + requested_topping + ".")

# print("\nFinished making your pizza!")

# 4.2 리스트가 비어 있지 않은지 확인하기
# requested_toppings = []

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print("Adding " + requested_topping + ".")
#     print("\nFinished makin your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

# 4.3 여러 리스트 다루기
# available_toppings = [
#     'mushrooms', 'olives', 'green peppers',
#     'pepperoni', 'pineapple', 'extra cheese'
# ]

# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print("Adding " + requested_topping + ".")
#     else:
#         print("Sorry we don't have " + requested_topping + ".")

# print("\nFinished making your pizza!")