##### SECTION 3: 리스트 다루기 #####

# 1. for 루프의 이해
animals = ['dog', 'cat', 'whale']
for animal in animals:
    print('I like ' + animal)

print('They are cute.')

# 2. 숫자 리스트

# 2.1 range() 사용하기
for value in range(1, 6):
    print(value)

# 2.2 range()로 숫자리스트 만들기
numbers = list(range(1, 11))
print(numbers)

# 짝수 리스트
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# 제곱 리스트
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# 2.3 리스트 내포
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 2.4 간단한 통계
digits = list(range(0, 10))
print(max(digits)) # 최댓값
print(min(digits)) # 최솟값
print(sum(digits)) # 합계

# 3. 리스트 잘라내기 (슬라이스)
alphabets = ['a', 'b', 'c', 'd', 'e', 'f']

# 3.1 슬라이스
print(alphabets[1:3])
print(alphabets[:3])
print(alphabets[3:])
print(alphabets[-2:]) 

# 3.2 슬라이스 루프
for alphabet in alphabets[:3]:
    print(alphabet)

# 3.3 리스트 복제
new_alphabets = alphabets[:]
print(new_alphabets)

# 4. 튜플 (값이 변하지 않는 리스트)
dimensions = (200, 50)
print(dimensions)