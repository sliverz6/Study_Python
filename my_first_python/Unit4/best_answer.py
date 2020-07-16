#####################################
##### SECTION 3 - 리스트 다루기 #####
#####################################

##### 1. 리스트 반복 #####

# 1.1 for 문 
countries = ['korea', 'america', 'germany', 'swiss']

for country in countries:
    print(country) 

##### 2. 숫자 리스트 #####

# 2.1 range()
for value in range(1, 6): # 1부터 5까지
    print(value)

# 2.2 숫자 리스트 만들기
numbers = list(range(1, 11)) # 1부터 10까지 숫자 리스트
even_number = list(range(2, 11, 2)) # 2씩 증가 (짝수 리스트)

# 2.3 간단한 통계
print(min(numbers)) # 최솟값
print(max(numbers)) # 최댓값
print(sum(numbers)) # 합계

# 2.4 리스트 내포
squares = [value ** 2 for value in range(1, 11)]

##### 3. 리스트 자르기 #####

# 3.1 슬라이스 
alphabets = ['a', 'b', 'c', 'd', 'e']
print(alphabets[1:3]) # 1 ~ 2
print(alphabets[:3]) # 처음 ~ 2
print(alphabets[2:]) # 2 ~ 끝
print(alphabets[-2:]) # 뒤에서 2 ~ 끝

# 3.2 슬라이스 루프
for alphabet in alphabets[:3] # 처음 3개만
    print(alphabet)

# 3.3 리스트 복제
new_alphabets = alphabets[:] # 모든 인덱스 복사

##### 4. 튜플 #####

# 4.1 튜플 만들기
dimensions = (200, 50)

# 4.2 튜플 반복
for dimension in dimensions:
    print(dimension)

# 4.3 튜플 덮어쓰기
dimensions = (400, 100)