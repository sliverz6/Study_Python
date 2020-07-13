# 1. 반복 실행
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)

# 1.2 반복문 안에서 더 많은 일 하기
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician.title() + ', that was a great trick!')
#     print("I can't wait to see your next trick, " + magician.title() + '.\n')

# 1.3 for 루프 다음에 어떤 일 하기
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician.title() + ', that was a great trick!')
#     print("I can't wait to see your next trick, " + magician.title() + '.\n')

# print("Thank you, everyone. That was a great magic show!")


# 2. 숫자 리스트 

# 2.1 range()
# for value in range(1, 6):
#     print(value)

# 2.2 range()로 숫자 리스트 만들기
# numbers = list(range(1, 6))
# print(numbers)

# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)

# print(squares)

# 2.3 숫자 리스트를 이용한 단순한 통계
# digits = list(range(0, 10))
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# 2.4 리스트 내포
# squares = [value ** 2 for value in range(1, 11)]
# print(squares)


# 3. 리스트 일부분 다루기

# 3.1 리스트 자르기
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[2:])
# print(players[-3:])

# 3.2 슬라이스에 반복문 실행
# players = ['charles', 'martina', 'michael', 'florence', 'eli']

# print("Here are the first three player on my team:")
# for player in players[:3]:
#     print(player.title())

# 3.3 리스트 복제
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy frined's favorite foods are:")
# print(friend_foods)


# 4. 튜플

# 4.1 튜플 정의하기
# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# # 4.2 튜플 루프 실행
# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)

# 4.3 튜플 덮어쓰기
# dimensions = (200, 50)
# print('Original dimension:')
# for dimension in dimensions:
#     print(dimension)

# dimensions = (400, 100)
# print('\nModified dimensions:')
# for dimension in dimensions:
#     print(dimension)