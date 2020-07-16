##### 사용자 입력과 while 루프

# 1. input() 함수가 동작하는 법
# message = input("Tell me something and I will repeat it back to you: ")
# print(message)

# 1.1 명확한 프롬프트 작성하기
# name = input("Please enter your name: ")
# print("Hello " + name + "!")

# prompt = "If you tell us who you are we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print("\nHello " + name + "!")

# 1.2 int()를 써서 숫자형 입력받기
# height = input("How tall are you in inches? ")
# height = int(height)
# if height >= 36:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# 1.3 나머지 연산자
# number = input("Enter a number and I'll tell you if it's even of odd: ")
# number = int(number)

# if number % 2 == 0:
#     print("\nThe number " + str(number) + " is even.")
# else:
#     print("\nThe number " + str(number) + " is odd.")


# 2. while 루프 소개

# 2.1 while 루프 사용하기
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# 2.2 사용자가 멈출 수 있도록 만들기
# prompt = "\nTell me something and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the progame. "
# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

# 2.3 플래그 사용하기
# prompt = "\nTell me something and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the progame. "

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# 2.4 break로 루프 빠져나가기
# prompt = "\nplease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")

# 2.5 루프에서 continue 문 사용하기
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue

#     print(current_number)


# 3. 리스트와 딕셔너리에 while 루프 사용하기

# 3.1 항목을 리스트에서 다른 리스트로 옮기기
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)

# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# 3.2 리스트에서 특정 값 모두 제거하기
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# 3.3 사용자가 입력한 값으로 딕셔너리 채우기
# responses = {}

# polling_active = True

# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")

#     responses[name] = response

#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False

# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(name + " would like to climb " + response + ".")