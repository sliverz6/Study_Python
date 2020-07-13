# 1. 리스트 반복
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)

# 2. 숫자 리스트

# 2.1 range()
for value in range(1, 6):
    print(value)

# 2.2 숫자리스트 만들기
numbers = list(range(1, 11))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# 2.3 간단한 통계
digits = list(range(0, 10))
print(min(digits))
print(max(digits))
print(sum(digits))

# 2.4 리스트 내포
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 3. 리스트 잘라내기

# 3.1 슬라이스
numbers = list(range(0, 8))
print(numbers[0:3])
print(numbers[:2])
print(numbers[5:])
print(numbers[-3:])

# 3.2 슬라이스 반복
players = ['mike', 'alice', 'peter', 'james']
for player in players[:1]:
    print(player)

# 3.3 리스트 복사
new_players = players[:]
print(new_players)

# 4. 튜플

# 4.1 튜플 정의
dimensions = (200, 50)
print(dimensions)

# 4.2 튜플 반복
for dimension in dimensions:
    print(dimension)

# 4.3 튜플 덮어쓰기
