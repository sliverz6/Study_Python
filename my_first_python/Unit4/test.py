##### Ch.1 변수와 단순한 데이터 타입 #####

# 1. 변수

# 1.1 변수 선언
name = 'Lee'

# 1.2 새로운 값 할당
name = 'Seung jae'

# 1.3 변수 이름 규칙
# - 숫자로 시작해서는 안된다
# - 띄어쓰기는 _로 구분한다
# - 함수명, 키워드는 사용 불가
# - 갖고있는 값을 잘 표현하는 이름 사용

# 2. 문자

# 2.1 문자 만드는 법
string = 'string' # 작은 따옴표
string = "string" # 큰 따옴표
string = "I'm string" # 혼합

# 2.2 문자 연결
first_name = 'lee'
last_name = 'seung jae'
full_name = first_name + ' ' + last_name

# 2.3 대소문자 변경
name = 'Lee seungjae'
print(name.title()) # 단어별 앞글자 대문자로
print(name.upper()) # 모든 글자 대문자
print(name.lower()) # 모든 글자 소문자

# 2.4 공백 문자
print('\tpython') # 들여쓰기
print('\npython') # 줄바꿈

# 2.5 공백 잘라내기
language = ' python '
print(language.strip()) # 양쪽 공백 제거
print(language.lstrip()) # 왼쪽 공백 제거
print(language.rstrip()) # 오른쪽 공백 제거

# 3. 숫자

# 3.1 숫자 종류
type1 = 2 # 정수(int)
type2 = 0.1 # 부동소수점숫자(float)

# 3.2 연산
print(2 + 1) # 더하기
print(2 - 1) # 빼기
print(3 * 2) # 곱하기
print(4 / 2) # 나누기
print(2 ** 2) # 제곱

# 3.3 연산 우선순위
print(2 + 3 * 4) # 곱하기 먼저
print((2 + 3) * 4) # 관호 먼저

# 3.4 이상한 수
print(0.1 + 0.2) # 이진법 때문에

# 3.5 문자로 타입 변경
age = 28
message = "I'm " + str(age) + "years old."
print(message)

# 4. 주석

# 주석은 간결하고 명료하게

# 5. 파이썬 철학

# - 추한 것 보다 아름다움이 낫습니다
# - 복잡함보다 단숨함이 낫습니다
# - 가독성이 중요합니다
# - 할 일은 지금 당장 하세요

##### Ch.2 리스트 #####

# 1. 리스트 기본

# 1.1 리스트 선언
numbers = [1, 2, 3, 4, 5]

# 1.2 리스트 요소 접근
print(numbers[0])
print(numbers[-1]) # 맨 마지막 요소

# 2. 요소 수정, 추가, 제거

# 2.1 요소 수정
numbers[0] = 0 # 새로운 값 할당

# 2.2 요소 추가

# 2.2.1 마지막에 추가
numbers.append(3)

# 2.2.2 중간에 추가
numbers.insert(2, 4) # 2번 인덱스에 4 추가

# 2.3 요소 제거

# 2.3.1 del 키워드로 제거
del numbers[2]

# 2.3.2 pop()으로 제거
numbers.pop() # 마지막 요소 제거
popped_number = numbers.pop(1) # 1번 요소 제거, 변수에 담을 수 있다

# 2.3.3 remove()로 제거
number = 1
numbers.remove(number) # 값을 넣어서 제거

# 3. 리스트 정렬
alphabets = ['b', 'c', 'f', 'w', 'g']

# 3.1 임시 정렬

# 3.1.1 알파벳 순
print(sorted(alphabets))

# 3.1.2 알파벳 역순
print(sorted(alphabets, reverse=True))

# 3.2 영구 정렬

# 3.2.1 알파벳 순
alphabets.sort()

# 3.2.2 알파벳 역순
alphabets.sort(reverse=Ture)

# 3.3 역순 정렬
alphabets.reverse()

# 3.4 리스트 길이 알아내기
print(len(alphabets))

##### Ch.3 리스트 다루기 #####

# 1. 리스트 반복
foods = ['hamberger', 'chicken', 'steak']

for food in foods:
    print(food)

# 2. range()

# 2.1 원하는 범위의 숫자리스트 만들기
numbers = list(range(0, 11))
numbers = list(range(1, 11, 2)) # 홀수만

# 2.2 간단한 통계
print(max(numbers)) # 최댓값
print(min(numbers)) # 최솟값
print(sum(numbers)) # 합계

# 2.3 리스트 내포
numbers = [value ** 2 for value in range(1, 11)]

# 3. 리스트 자르기
alphabets = ['a', 'b', 'c', 'd', 'e']
alphabets[0:3] # 0 ~ 2번 까지
alphabets[:2] # 처음 ~ 1번
alphabets[3:] # 3번 ~ 끝
alphabets[:] # 전부 (복사 용도로 사용됨)

# 4. 튜플
dimesions = (50, 200)
