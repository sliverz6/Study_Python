# 7-1 렌터카
# rent_car = input("어떤 렌트카를 찾고 있나요? ")
# print(rent_car + "을/를 지금 찾는 중입니다.")

# 7-2 레스토랑 예약
# people_number = input("저녁 식사에 몇 명이 옵니까? ")
# people_number = int(people_number)

# if people_number >= 9:
#     print('자리가 날 때까지 기다리셔야 합니다.')
# else:
#     print('테이블이 준비되었습니다.')

# 7-3 10의 배수
# prompt = "10의 배수인지 알려드리겠습니다."
# prompt += "\n숫자를 입력하세요: "
# number = input(prompt)
# number = int(number)

# if number % 10 == 0:
#     print(str(number) + "은 10의 배수입니다.")
# else:
#     print(str(number) + "은/는 10의 배수가 아닙니다.")

# 7-4 피자 토핑
# active = True
# while active:
#     topping = input("원하는 토핑을 입력하세요.(종료는 'quit'을 입력하세요) ")
    
#     if topping == 'quit':
#         active = False
#     else:
#         print(topping + "을/를 추가합니다!")

# 7-5 영화 입장권
# while True:
#     age = input("나이를 입력하세요: ")
#     age = int(age)

#     if age < 3:
#         print("무료입니다.")
#     elif age <= 12:
#         print("10달러입니다.")
#     else: 
#         print("15달러입니다.")

# 7-6 세 가지 탈출구
# while age:
#     age = input("나이를 입력하세요: ")
#     age = int(age)

#     if age < 3:
#         print("무료입니다.")
#     elif age <= 12:
#         print("10달러입니다.")
#     else: 
#         print("15달러입니다.")

# 7-8 제과점
# sandwich_orders = ['BLT 샌드위치', '햄치즈 샌드위치', '치킨 샌드위치']
# finished_sandwichs = []

# while sandwich_orders:
#     sandwich = sandwich_orders.pop()

#     print(sandwich + "가 완성되었습니다!")
#     finished_sandwichs.append(sandwich)

# print("\n완성된 샌드위치:")
# for finished_sandwich in finished_sandwichs:
#     print(finished_sandwich)

# 7-9 패스트라미 없음
# sandwich_orders = [
#     'BLT 샌드위치', '패스트라미 샌드위치', '햄치즈 샌드위치', 
#     '치킨 샌드위치', '패스트라미 샌드위치', '패스트라미 샌드위치'
#     ]
# finished_sandwichs = []

# print("패스트라미 샌드위치는 다 떨어졌습니다.")

# while '패스트라미 샌드위치' in sandwich_orders:
#     sandwich_orders.remove('패스트라미 샌드위치')

# while sandwich_orders:
#     sandwich = sandwich_orders.pop()

#     print(sandwich + "가 완성되었습니다!")
#     finished_sandwichs.append(sandwich)

# print("\n완성된 샌드위치:")
# for finished_sandwich in finished_sandwichs:
#     print(finished_sandwich)

# 7-10 꿈같은 휴가
# responses = {}

# prompt = "이번 휴가때 가고싶은 곳은 어디입니까?"
# prompt += "가고싶은 곳: "

# polling_active = True
# while polling_active:
#     name = input("이름을 입력해주세요. ")
#     location = input(prompt)

#     responses[name] = location

#     repeat = input("설문조사를 계속하시겠습니까? (네 / 아니오) ")
#     if repeat == '아니오':
#         polling_active = False

# print("\n--- 설문 결과 ---")
# for name, response in responses.items():
#     print("이름: " + name + ", 휴가지: " + response)