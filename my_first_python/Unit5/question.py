# 5-1 조건 테스트

# 5-2 더 많은 조건 테스트

# 5-3 외계인 색 #1
# ailen_color = 'green'

# if ailen_color == 'green':
#     print('5점을 얻었습니다.')

# 5-4 외계인 색 #2
# ailen_color = 'green'

# if ailen_color == 'green':
#     print("5점을 얻었습니다.")
# else:
#     print("10점을 얻었습니다.")

# 5-5 외계인 색 #3
# ailen_color = 'green'

# if ailen_color == 'green':
#     print("5점을 얻었습니다.")
# elif ailen_color == 'yellow':
#     print("10점을 얻었습니다.")
# elif ailen_color == 'red':
#     print('15점을 얻었습니다.')

# 5-6 성장단계
# age = 28

# if age < 2:
#     person_type = '영아'
# elif age < 4:
#     person_type = '유아'
# elif age < 13:
#     person_type = '아이'
# elif age < 20:
#     person_type = '청소년'
# elif age < 65:
#     person_type = '성인'
# else:
#     person_type = '노인'

# print("당신은 " + person_type + "입니다.")

# 5-7 좋아하는 과일
# favorite_fruits = ['수박', '사과', '메론', '파인애플']

# if '수박' in favorite_fruits:
#     print("수박을 좋아하는군요!")

# 5-8 관리자에게 인사
# users = ['peter', 'james', 'john', 'alice', 'admin']

# for user in users:
#     if user == 'admin':
#         print("관리자님 안녕하세요.")
#     else: 
#         print("Hello, " + user.title() + "!")

# 5-9 사용자 없음
# users = []

# if users:
#     for user in users:
#         if user == 'admin':
#             print("관리자님 안녕하세요.")
#         else: 
#             print("Hello, " + user.title() + "!")
# else:
#     print("사용자가 있어야 합니다!")

# 5-10 사용자 이름 체크
# current_users = ['peter', 'alice', 'julia', 'john', 'mike']
# new_users = ['james', 'peter', 'sam', 'alice', 'joly']

# for new_user in new_users:
#     if new_user in current_users:
#         print("다른 사용자 이름이 필요합니다.")
#     else: 
#         print("사용자 이름을 쓸 수 있습니다.")

# 5-11 순번
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")

