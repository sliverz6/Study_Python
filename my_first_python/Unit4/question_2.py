# 4-1 피자
# pizzas = ['페페로니 피자', '치즈 피자', '불고기 피자']
# for pizza in pizzas:
#     print('저는 ' + pizza + '를 좋아합니다.')

# print('피자가 먹고싶네요!')

# 4-2 동물
# animals = ['강아지', '고양이', '햄스터']
# for animal in animals:
#     print(animal + '은/는 귀여운 애완동물입니다.')

# print('이들은 모두 애완동물입니다.')

# 4-3 20까지 세기
# for value in range(1, 21):
#     print(value)

# 4-4 백만 (안함)

# 4-5 백만까지 더하기
# numbers = list(range(1, 1000001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# 4-6 홀수
# odd_numbers = list(range(1, 21, 2))
# for odd_number in odd_numbers:
#     print(odd_number)

# 4-7 3배수
# numbers = list(range(3, 31, 3))
# for number in numbers:
#     print(number)

# 4-8 세제곱
# cubes = []
# for value in range(1, 11):
#     cube = value ** 3
#     cubes.append(cube)

# for cube in cubes:
#     print(cube)

# 4-9 세제곱 내포
# cubes = [value ** 3 for value in range(1, 11)]
# print(cubes)

# 4-10 슬라이스
# fruits = ['apple', 'banana', 'watermelon', 'strawberry', 'pineapple']
# print("리스트의 첫 세 항목은:")
# print(fruits[:3])

# print("\n리스트의 중간 세 항목은:")
# print(fruits[1:4])

# print("\n리스트의 마지막 세 항목은:")
# print(fruits[-3:])

# 4-11 내 피자, 너 피자
# pizzas = ['페페로니 피자', '치즈 피자', '불고기 피자']
# friend_pizzas = pizzas[:]

# pizzas.append('하와이안 피자')
# friend_pizzas.append('크러스트 피자')

# print("내가 좋아하는 피자는:")
# for pizza in pizzas:
#     print(pizza)

# print("\n내 친구가 좋아하는 피자는:")
# for friend_pizza in friend_pizzas:
#     print(friend_pizza)

# 4-13 뷔페
foods = ('라면', '삼겹살', '스프', '된장국', '용가리')
for food in foods:
    print(food)

# food[-1] = '치킨'

foods = ('치킨', '스테이크', '스프', '된장국', '용가리')
for food in foods:
    print(food)