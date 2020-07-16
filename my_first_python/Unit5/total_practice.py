# # ##### SECTION 1 - 변수와 단순한 데이터 타입 #####

# # # 1. 변수

# # # 1.1 변수 선언
# # name = 'lee'

# # # 1.2 변수 값 재 할당
# # name = 'seung jae'

# # # 1.3 변수 이름 규칙
# # # - 숫자로 시작 불가
# # # - 띄어쓰기는 _로
# # # 함수명, 키워드, 예약어 불가
# # # 갖고 있는 값을 잘 표현하는 변수명으로

# # # 2. 문자

# # # 2.1 문자 만들기
# # string = 'string'
# # string = "string"
# # string = "I'm string"

# # # 2.2 문자 연결
# # first_name = 'lee'
# # last_name = 'seungjae'
# # full_name = first_name + ' ' + last_name

# # # 2.3 대소문자 변경
# # name = 'Lee seungjae'
# # print(name.title())
# # print(name.upper())
# # print(name.lower())

# # # 2.4 공백문자
# # print('\npython')
# # print('\tpythin')

# # # 2.5 공백 잘라내기
# # language = ' python '
# # print(language.strip())
# # print(language.lstrip())
# # print(language.rstrip())

# # # 3. 숫자

# # # 3.1 숫자 종류
# # # - 정수(int)
# # # - 실수(float)

# # # 3.2 연산
# # print(2 + 3)
# # print(2 - 3)
# # print(2 * 3)
# # print(2 / 3)
# # print(2 ** 3)
# # print(2 // 3)
# # print(2 % 3)

# # # 3.3 연산 우선순위
# # print(2 + 3 * 4)
# # print((2 + 3) * 4)

# # # 3.4 이상한 수
# # print(0.1 + 0.2)

# # # 3.5 문자로 변경
# # age = 28
# # message = 'I\'m ' + str(age) + ' years old.'

# # # 4. 주석
# # # 주석은 짧고 간결하게

# # # 5. 파이썬 철학

# # ##### SECTION 2 - 리스트 #####

# # # 1. 리스트 기본

# # # 1.1 리스트 만들기
# # foods = ['라면', '김밥', '삼겹살']

# # # 1.2 요소 접근
# # print(foods[1])
# # print(foods[-1])

# # # 2. 리스트 요소 수정, 추가, 제거

# # # 2.1 요소 수정
# # foods[0] = '비빔밥'

# # # 2.2 추가

# # # 2.2.1 끝에 추가
# # foods.append('김치찌개')

# # # 2.2.2 원하는 곳에 추가
# # foods.insert(2, '된장찌개')

# # # 2.3 제거

# # # 2.3.1 del 키워드로 제거
# # del foods[0]

# # # 2.3.2 pop()으로 제거
# # popped_food = foods.pop() # 인덱스도 넣을 수 있음

# # # 2.3.3 값으로 제거
# # foods.remove('김밥')

# # # 4. 정렬
# # alphabets = ['b', 'c', 'd', 'f', 'e']

# # # 4.1 임시 정렬
# # print(sorted(alphabets))
# # print(sorted(alphabets, reverse=True))

# # # 4.2 영구 정렬
# # alphabets.sort()
# # alphabets.sort(reverse=True)

# # # 4.3 역순 정렬
# # alphabets.reverse()

# # # 4.4 리스트 길이 구하기
# # print(len(alphabets))

# ##### SECTION 3 - 리스트 다루기 #####

# # 1. 리스트 반복 for
# foods = ['김밥', '라면', '삼겹살']
# for food in foods:
#     print(food)

# # 2. 숫자 리스트

# # 2.1 range()
# for value in range(1, 6):
#     print(value)

# # 2.2 숫자리스트 만들기
# numbers = list(range(1, 11))
# print(numbers)

# # 2.2.1 짝수 리스트
# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

# # 2.3 간단한 통계
# digits = list(range(0, 10))
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# # 2.4 리스트 내포
# squares = [value ** 2 for value in range(1, 11)]

# # 3. 리스트 자르기

# # 3.1 슬라이스
# alphabets = ['a', 'b', 'c', 'd', 'e']
# print(alphabets[1:3])
# print(alphabets[:3])
# print(alphabets[2:])
# print(alphabets[-2:])

# # 3.2 슬라이스 루프
# for alphabet in alphabets[:2]:
#     print(alphabet)

# # 3.3 리스트 복사
# new_alphabets = alphabets[:]

# # 4. 튜플

# # 4.1 튜플 만들기
# dimensions = (200, 50)

# # 4.2 튜플 반복
# for dimension in dimensions:
#     print(dimension)

# # 4.3 튜플 덮어쓰기
# dimensions = (400, 100)

##### SECTION 4 - if 문 ######

# 1. 조건 테스트

# 1.1 일치 체크
car = 'bmw'
print(car == 'bmw')

# 1.2 대소문자 구분
car = 'audi'
print(car == 'Audi')

# 1.3 불일치 체크
car = 'bmw'
print(car != 'bmw')

# 1.4 숫자 비교
age = 28
print(age > 20)
print(age < 20)
print(age <= 20)
print(age <= 20)

# 1.5 리스트 안에 값이 있는지 체크
numbers = list(range(1, 11))
print(3 in numbers)

# 1.6 리스트 안에 값이 없는지 체크
print(11 not in numbers)

# 1.7 불리언 표현식
active = True

# 2. if 문

# 2.1 기본 if문
age = 28
if age >= 20:
    print('20대입니다.')

# 2.2 if-else 문
age = 28
if age >= 20:
    print('20대입니다.')
else: 
    print('20대가 아닙니다.')

# 2.3 if-elif-else 문
age = 28
if age >= 10:
    price = 0
elif age >= 20:
    price = 5
else:
    price = 10

print(price)

# 3. 리스트에서 if 문 사용
foods = ['라면', '김밥', '족발', '삼겹살']

# 3.1 값이 있는지 체크
for food in foods:
    if food == '라면':
        print('맛있겠다')

# 3.2 리스트가 비어 있지 않은지 확인
if foods:
    print('음식 있음')
else:
    print('음식 없음')

# 3.3 여러 리스트 다루기
favorite_foods = ['라면', '삼겹살', '냉면']

for favorite_food in favorite_foods:
    if favorite_food in foods:
        print('먹을 수 있다')
    else:
        print('음식이 없다')