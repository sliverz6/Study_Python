# # 4-1 피자
# favorite_pizzas = ['peperoni pizza', 'bacon pizza', 'cheeze pizza']
# for favorite_pizza in favorite_pizzas:
#     message = 'I like ' + favorite_pizza + '.'
#     print(message)

# print('I\'m very hungry. I want pizza!\n')

# # 4-2 동물
# animals = ['rabbit', 'dog', 'cat']
# for animal in animals:
#     message = animal + ' is cute.'
#     print(message)

# print('They are cute animal.')

# # 4-3 20까지 세기
# for value in range(1, 21):
#     print(value)

# # 4-4 백만 (안함)

# # 4-5 백만까지 더하기
# numbers = list(range(1, 1000001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# # 4-6 홀수
# odd_numbers = list(range(1, 21, 2))
# for odd_number in odd_numbers:
#     print(odd_number)

# # 4-7 3배수
# three_times_numbers = list(range(3, 31, 3))
# for three_times_number in three_times_numbers:
#     print(three_times_number)

# # 4-8 세제곱
# cube_numbers = []
# for value in range(1, 11):
#     cube_number = value ** 3
#     cube_numbers.append(cube_number)

# for cube_number in cube_numbers:
#     print(cube_number)

# # 4-9 세제곱 내포
# cube_numbers = [value ** 3 for value in range(1, 11)]
# print(cube_numbers)

# 4-10 슬라이스
# animals = ['rabbit', 'dog', 'cat', 'bear', 'lion', 'tiger']
# print('리스트의 첫 세 항목은:')
# print(animals[:3])

# print('리스트의 중간 세 항목은:')
# print(animals[1:4])

# print('리스트의 마지막 세 항목은:')
# print(animals[-3:])

# # 4-11 내 피자, 네 피자
# favorite_pizzas = ['peperoni pizza', 'bacon pizza', 'cheeze pizza']
# friend_pizzas = favorite_pizzas[:]

# favorite_pizzas.append('hawaian pizza')
# friend_pizzas.append('golden pizza')

# print('내가 좋아하는 피자는:')
# for favorite_pizza in favorite_pizzas:
#     print(favorite_pizza)

# print('\n내 친구가 좋아하는 피자는:')
# for friend_pizza in friend_pizzas:
#     print(friend_pizza)
 
# 4-13 뷔페
foods = ('삼겹살', '김치찌개', '햄버거', '된장찌개', '부대찌개')

for food in foods:
    print(food)

