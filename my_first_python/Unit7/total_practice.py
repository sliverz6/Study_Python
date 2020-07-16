##### SECTION 1 - 변수와 단순한 데이터 타입 #####

# 1. 변수

# 1.1 변수 선언
# 1.2 변수 값 재할당
# 1.3 변수 이름 규칙

# 2. 문자
# 2.1 문자 만들기
    # 작은 따옴표
    # 큰 따옴표
    # 혼합
# 2.2 문자 연결
    # +
# 2.3 대소문자 바꾸기
    # title()
    # upper()
    # lower()
# 2.4 공백 문자
    # \n
    # \t
# 2.5 공백 잘라내기
    # strip()
    # lstrip()
    # rstrip()

# 3. 숫자
# 3.1 숫자 종류
    # 정수
    # 실수
# 3.2 숫자 연산
    # +, -, *, /, **, %, //
# 3.3 연산 우선순위
# 3.4 이상한 수
# 3.5 문자로 바꾸기
    # str()

# 4. 주석
# 5. 파이썬 철학

##### SECTION 2 - 리스트 #####

# 1. 리스트 기본
# 1.1 리스트 만들기
list_0 = ['a', 'b', 'c']
# 1.2 리스트 요소 접근
list_0[0]
list_0[-1]

# 2. 요소 수정, 추가, 제거
# 2.1 수정
list_0[0] = 'a'
# 2.2 추가
list_0.append('d')
list_0.insert(1, 'e')
# 2.3 제거
del list_0[0]
popped_item = list_0.pop()
list_0.remove('b')

# 3. 정렬
# 3.1 임시정렬
sorted(list_0)
sorted(list_0, reverse=True)
# 3.2 영구정렬
list_0.sort()
list_0.sort(reversed=True)
# 3.3 역순정렬
list_0.reverse()
# 3.4 리스트 길이 알아내기
len(list_0)

##### SECTION 3 - 리스트 다루기 #####

# 1. 리스트 for 문
numbers = [1, 2, 3]
for number in numbers:
    print(number)

# 2. 숫자리스트
# 2.1 range()
for value in range(1, 6):
    print(value)
# 2.2 숫자리스트 만들기
numbers = list(range(1, 11))
even_numbers = list(range(2, 11, 2))
# 2.3 간단한 통계
min(numbers)
max(numbers)
sum(numbers)
# 2.4 리스트 내포
squares = [value ** 2 for value in range(1, 11)]

# 3. 리스트 자르기
# 3.1 슬라이스
numbers = list(range(0, 6))
numbers[1:3]
numbers[:3]
numbers[2:]
numbers[-2:]
# 3.2 슬라이스 반복
for number in numbers[:2]:
    print(number)
# 3.3 리스트 복사
new_numbers = numbers[:]

# 4. 튜플 
# 4.1 튜플 만들기
tuple_0 = (200, 50)
# 4.2 튜플 반복
for value in tuple_0:
    print(value)
# 4.3 튜플 덮어쓰기
tuple_0 = (400, 100)

##### SECTION 4 - if 문 #####

# 1. 조건테스트
# 1.1 일치 체크
car = 'bmw'
car == 'bmw'
# 1.2 불일치 체크
car != 'bmw'
# 1.3 숫자 비교
age = 28
age > 20
age < 20
age >= 20
age >= 20
# 1.4 여러 조건 비교
# and
# or
# 1.5 리스트 안에 값이 있는지 확인
numbers = [1, 2, 3, 4]
print(2 in numbers)
# 1.6 리스트 안에 값이 없는지 확인
print(5 not in numbers)
# 1.7 불리언 표현식
active = True

# 2. 조건문
# 2.1 if 문 기본
if condition:
    something
# 2.2 if-else 문
if condition:
    something
else:
    something_2
# 2.3 if-elif-else 문
if condition_0:
    something
elif condition_1:
    something_1
else:
    something_2

# 3. 리스트 안에서 조건문
# 3.1 리스트 안에 값이 있는지 판단
foods = ['라면', '김치찌개', '삼겹살']
for food in foods:
    if food == '라면':
        print('라면 먹자')
# 3.2 빈 리스트가 아닌지 판단
if foods:
    print('안비었다')
else:
    print('비었다')
# 3.3 여러 리스트 다루기
pocket = ['냉면']
for food in foods:
    if food in pocket:
        print('있다!')

##### SECTION 5 - 딕셔너리 #####

# 1. 딕셔너리 기본
# 1.1 딕셔너리 만들기
person = { 'name': 'lee' }
# 1.2 값 접근
person['name']
# 1.3 값 수정
person['name'] = 'seungjae'
# 1.4 새로운 키-값 쌍 추가
person['age'] = 28
# 1.5 키-값 쌍 제거
del person['age']

# 2. 딕셔너리 반복
# 2.1 키-값 쌍에 대한 반복
for key, value in person.items():
# 2.2 키에 대한 반복
for key in person.keys():
for key in person
# 2.3 값에 대한 반복
for value in person.values():

# 3. 중첩
# 3.1 리스트 안에 딕셔너리
person = {
    'name': 'lee'
}
people = [person_0]
# 3.2 딕셔너리 안에 리스트
person = {
    'hobbies': ['coding']
}
# 3.3 딕셔너리 안에 딕셔너리
person = {
    'friend': {
        'name': 'john'
    }
}

##### SECTION 6 - 사용자 입력과 while 루프 #####

# 1. 사용자 입력
# 1.1 input()
name = input('이름을 입력하세요: ')
# 1.2 숫자 입력
age = int(input('나이를 입력하세요: '))
# 1.3 나머지 연산자 활용 - 짝수 홀수 판단

# 2. while 루프
# 2.1 기본 사용법
number = 1
while number <= 5:
    print(number)
    number += 1
# 2.2 break 키워드
while number <= 5:
    print(number)
    break
    number += 1
# 2.3 continue 키워드
while number <= 5:
    if number % 2 == 0:
        continue
    print(number)
    number += 1
# 2.4 사용자가 실행 중지하기
# 플래그 만들기
# break로 빠져나가기

# 3. 리스트와 딕셔너리에 while 루프 사용
# 3.1 리스트에서 리스트로 요소 옮기기
list_0 = ['a', 'b', 'c']
list_1 = []
while list_0:
    popped_item = list_0.pop()
    list_1.append(popped_item)
# 3.2 리스트에서 특정 요소 전부 지우기
list_0 = ['a', 'a', 'b', 'c']
while 'a' in list_0:
    list_0.remove('a')
# 3.3 사용자 입력을 받아 딕셔너리 만들기
person = {}
active = True
while active:
    name = input()
    age = int(input())
    person[name] = age
    active = False