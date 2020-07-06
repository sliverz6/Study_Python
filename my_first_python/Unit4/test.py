# 1. 리스트 for문
alphabets = ['a', 'b', 'c', 'd', 'e']

for alphabet in alphabets:
    print(alphabet)

# 2. range() 함수

# 2.1 기본 사용
for value in range(1, 6): # 6은 포함 안된다.
    print(value) 

# 2.2 증가량 표현
for value in range(1, 11, 2): # 2씩 증가
    print(value)

# 2.3 숫자 리스트 만들기 (list() 함수)
numbers = list(range(1, 11))
print(numbers)

# 2.4 리스트 내포
numbers = [value ** 2 for value in range(1, 11)]
print(numbers)

# 2.5 간단한 통계
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(numbers)) # 최대값
print(min(numbers)) # 최솟값
print(sum(numbers)) # 합계

# 3. 리스트 자르기

# 3.1 원하는 범위 자르기
alphabets = ['a', 'b', 'c', 'd', 'e']
print(alphabets[0:3]) # 0부터 2까지
print(alphabets[:2]) # 처음부터 2까지
print(alphabets[2:]) # 2부터 끝까지
print(alphabets[-3:]) # 뒤에서 세번째까지

# 3.2 슬라이스 반복
for alphabet in alphabets[:2]:
    print(alphabet)

# 3.3 리스트 복제
cloned = alphabets[:]
print(cloned)

# 4. 튜플

# 4.1 튜플 정의
foods = ('삼겹살', '라면')

# 4.2 튜플 반복
for food in foods:
    print(food)

# 4.3 튜플 재할당
foods = ('삼겹살', '비빔면')
print(foods)