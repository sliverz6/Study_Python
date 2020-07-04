##### 변수 #####

#  변수 선언
name = 'Lee'
name = 'seung jae' # 변수의 값은 변할 수 있다

# 변수 이름
# 1. 숫자로 시작하면 안된다.
# 2. 띄어쓰기는 _로 구분
# 3. 키워드, 함수명은 안된다.
# 4. 갖고 있는 값을 명확히 설명하는 이름으로


##### 문자열 #####

# 문자 만드는 법
'Hello' 
"Hello"
"I'm seung jae"

# 문자 연결
first_name = 'lee'
last_name = 'seung jae'
full_name = first_name + ' ' + last_name

# 대소문자 변경
name = 'Lee seungjae'
print(name.title()) # 단어별 앞글자만 대문자
print(name.upper()) # 모든 글자 대문자
print(name.lower()) # 모든 글자 소문자

# 공백 문자
print('\npython') # 줄바꿈
print('\tpython') # 들여쓰기

# 공백 잘라내기
language = ' python '
print(language.strip()) # 앞 뒤 공백 제거
print(language.lstrip()) # 왼쪽 공백 제거
print(language.rstript()) # 오른쪽 공백 제거


##### 숫자 #####

# 정수 연산
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)
print(2 ** 3)

# 연산 우선순위
print((2 + 3) * 4)

# 부동소수점 숫자 연산
print(0.3 + 0.1)

# 이상한 수
print(0.2 + 0.1)

# 문자와 연결시 오류 (숫자를 문자로 변환)
age = 28
message = "Hello, i' " + age + ' years old.'
print(message)


##### 주석 #####
# 주석은 간결하고 명료하게


##### 파이썬 철학 #####
# 1. 추함보다 아름다움이 낫습니다.
# 2. 복잡함보다 단순함이 낫습니다.
# 3. 가독성에 신경쓰세요.
# 4. 할 일은 지금 당장 하세요.