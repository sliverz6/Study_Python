# 1. 변수 

# 1.1 변수 선언
name = 'lee'
name = 'seungjae' # 새로운 값을 할당할 수 있다

# 1.2 변수 이름 규칙
# - 숫자로 시작해서는 안된다
# - 띄어쓰기는 _로 구분한다
# - 키워드나 함수명은 불가
# - 갖고있는 값을 잘 표현하는 이름으로 지어야 한다

# 2. 문자

# 2.1 문자 만들기
string = 'string' # 작은 따옴표
string = "string" # 큰 따옴표
string = "I'm string" # 혼합형

# 2.2 대소문자 바꾸기
name = 'Lee seungjae'
print(name.title()) # 앞글자만 대문자
print(name.upper()) # 전부 대문자
print(name.lower()) # 전부 소문자

# 2.3 공백 문자
print('\tpython') # 들여쓰기
print('\npython') # 줄바꿈

# 2.4 공백 잘라내기
language = ' python '
print(language.strip()) # 양쪽 공백 잘라내기
print(language.lstrip()) # 왼쪽 공백 잘라내기
print(language.rstrip()) # 오른쪽 공백 잘라내기

# 2.5 문자 연결
first_name = 'Lee'
last_name = 'seungjae'
full_name = first_name + ' ' + last_name
print(full_name)

# 3. 숫자

# 3.1 숫자 종류
정수 = 2 
부동소수점숫자 = 0.1

# 3.2 숫자 연산
print(2 + 1) # 더하기
print(2 - 1) # 빼기
print(2 * 2) # 곱하기
print(3 / 1) # 나누기
print(2 ** 3) # 제곱

# 3.3 연산 우선순위
print(2 + 3 * 3) 
print((2 + 3) * 3) # 괄호먼저 연산

# 3.4 문자로 타입 변경
age = 28
message = 'I am ' + str(age) + 'years old.'
print(message)

# 3.5 이상한 수
print(0.2 + 0.1) # 컴퓨터의 이진법 연산때문에 발생

# 4. 주석

# 주석은 간결하고 명료하게 필요할 때만

# 5. 파이썬 철학 
# - 아름다움이 추한것보다 낫습니다
# - 단순함이 복잡함보다 낫습니다
# - 가독성이 중요합니다
# - 할 일은 지금 당장 하세요

#####################################################
#####################################################

# 1. 리스트 기본

# 1.1 리스트 선언 
strings = ['a', 'b', 'c', 'd']

# 1.2 리스트 요소 접근
print(strings[0]) # 'a'
print(strings[-1]) # 맨 마지막 요소

# 2. 요소 수정, 추가, 제거

# 2.1 수정
strings[0] = 'e'

# 2.2 추가

# 2.2.1 맨 끝에 추가
strings.append('f')

# 2.2.2 원하는 곳에 추가
strings.insert(2, 'g')

# 2.3 제거

# 2.3.1 del 문으로 제거
del strings[0]

# 2.3.2 pop()으로 제거
popped_string = strings.pop() # 변수에 담을 수 있음
strings.pop(2) # 원하는 인덱스를 제거할 수 있음

# 2.3.3 remove()로 제거
string = 'b'
strings.remove(string)

# 3. 정렬

strings = ['b', 'e', 'w', 'f', 'a', 'c']

# 3.1 알파벳 순으로 임시정렬
print(sorted(strings))

# 3.2 알파벳 역순으로 임시 정렬
print(sorted(strings, reverse=True))

# 3.3 알파벳 순으로 영구정렬
strings.sort()

# 3.4 알파벳 역순으로 영구정렬
strings.sort(reverse=True)

# 3.5 역순으로 정렬
strings.reverse()
print(strings)

# 3.6 배열 길이 알아내기
print(len(strings))