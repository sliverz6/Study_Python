#################################################
##### SECTION 1 - 변수와 단순한 데이터 타입 #####
#################################################

##### 1. 변수 #####

# 1.1 변수 선언
name = 'lee'

# 1.2 변수 재할당
name = 'seungjae'

# 1.3 변수 이름 규칙
# - 띄어쓰기는 _로 
# - 숫자로 시작 불가
# - 함수명, 예약어, 키워드 불가
# - 갖고 있는 값을 잘 표현하는 값으로

##### 2. 문자 #####

# 2.1 문자 만들기
string_0 = 'string' # 작은 따옴표
string_1 = "string" # 큰 따옴표
string_2 = "I'm string" # 혼합형

# 2.2 문자 연결
first_name = 'Lee'
last_name = 'Seungjae'
full_name = first_name + " " last_name
print(full_name)

# 2.3 대소문자 변경
name = 'Lee seungjae'
print(name.title()) # 단어별 앞글자만 대문자
print(name.upper()) # 모든 글자 대문자
print(name.lower()) # 모든 글자 소문자

# 2.4 공백 문자
print('\tpython') # 들여쓰기
print('\npython') # 줄바꿈

# 2.5 공백 잘라내기
language = ' python '
print(language.strip()) # 양쪽 공백 잘라내기
print(language.lstrip()) # 왼쪽 공백 잘라내기
print(language.rstrip()) # 오른쪽 공백 잘라내기

##### 3. 숫자 #####

# 3.1 숫자 종류
print(3) # 정수(integer)
print(0.3) # 부동소수점 숫자(float)

# 3.2 숫자 연산
print(2 + 1) # 더하기
print(2 - 1) # 빼기
print(2 * 3) # 곱하기
print(10 / 2) # 나누기
print(2 ** 3) # 제곱
print(10 % 3) # 나머지 연산자
print(10 // 3) # 몫 연산자

# 3.3 연산 우선순위
print(2 + 3 * 3) # 곱하기 먼저
print((2 + 3) * 3) # 괄호 먼저

# 3.4 이상한 수
print(0.1 + 0.2) # 이진법 연산 결과

# 3.5 숫자에서 문자로 바꾸기 (str())
age = 23 
message = "I'm " + str(age) + " years old."
print(message)

##### 4. 주석 #####

# 간단한 인삿말을 출력합니다.
print("Hello!")

##### 5. 파이썬 철학 #####

# - 복잡함보다 단순함이 낫습니다.
# - 추한것보다 아름다운게 낫습니다. 
# - 가독성에 신경쓰세요. 
# - 할 일은 지금 당장하세요. 