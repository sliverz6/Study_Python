# 1. for 루프의 이해

# 1.1 전체 리스트에 루프 실행하기
magicians = ['alice', 'david', 'carolina']
for magician in magicians: # 루프의 임시변수는 최대한 단수, 복수 짝을 맞춰서 사용하자.
    print(magician) 

# 1.2 루프 안에서 더 많은 일 하기
for magician in magicians:
    print(magician.title() + ', that was a great trick!') # 들여쓰기 한 곳은 루프 블록
    print("I can't wait to see your next trick, " + magician.title() + '.\n')

# 1.3 for 루프 다음에 어떤 일 하기
print("Thank you, everyone. That was a great magic show!") # 한 번만 실행된다


# 2. 들여쓰기 에러 피하기


# 3. 숫자 리스트 만들기

# 3.1 range() 함수 사용하기
for value in range(1, 5): # 5는 포함 안된다
    print(value)

for value in range(1, 6):
    print(value)

# 3.2 range()로 숫자 리스트 만들기
numbers = list(range(1, 6)) # list() 함수 사용
print(numbers)

# 짝수 리스트
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# 홀수 리스트
odd_numbers = list(range(1, 11, 2))
print(odd_numbers)

# 제곱수 리스트
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# 3.3 숫자 리스트를 이용한 단순한 통계
digits = list(range(0, 10))
print(min(digits)) # 최솟값
print(max(digits)) # 최대값
print(sum(digits)) # 합계

# 3.4 리스트 내포
squares = [value ** 2 for value in range(1, 11)]
print(squares)


# 4. 리스트 일부분 다루기 (슬라이스 slice)

# 4.1 리스트 자르기
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4]) # 처음 인덱스부터
print(players[2:]) # 마지막 인덱스까지
print(players[-3:]) # 마지막에서 3번째 인덱스부터

# 4.2 슬라이스에 루프 실행
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# 4.3 리스트 복사
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
# frined_foods = my_foods # 이것은 같은 리스트를 가르킨다

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


# 5. 튜플

# 5.1 튜플 정의하기
dimensions = (200, 50)
print(dimensions[0]) 
print(dimensions[1])

# 5.2 튜플에 for 루프 실행하기
for dimension in dimensions:
    print(dimension)

# 5.3 튜플에 새로운 값 덮어쓰기
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimension = (400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)