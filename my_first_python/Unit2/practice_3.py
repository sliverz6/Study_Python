###### 변수
message = "Hello"
message = "world" #변수는 바꿀 수 있다
print(message)

# 변수 이름 짓기
# 숫자로 시작하면 안된다.
# 띄어쓰기는 _로 한다.
# 파이썬 키워드나 함수는 안된다.
# 이름의 뜻하는 바가 명확해야 한다.

##### 문자
# 선언법
# "string"
# 'string'
# "I'm string"

# 대소문자 변경
name = 'Lee seungjae'
print(name.title()) # 앞글자만 대문자
print(name.upper()) # 모든 글자 대문자
print(name.lower()) # 모든 글자 소문자

# 공백 문자
print("\tPython") # 들여쓰기
print("\nPython") # 줄바꿈

# 문자열 연결
first_name = 'Lee'
last_name = 'seungjae'
full_naem = first_name + " " + last_name

# 공백 잘라내기
language = ' Python '
language.lstrip() # 왼쪽 공백 제거
language.rstrip() # 오른쪽 공백 제거
language.strip() # 양쪽 모든 공백 제거


##### 숫자

# 정수형과 부동소수점 숫자가 있다

# 정수 연산
print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)
print(1 ** 2)

# 부동소수점 연산
print(0.2 + 0.2)

# 이상한 수
print(0.2 + 0.1)

# 문자열 결합시 에러 피하기 (숫자를 문자로 변환하기)
age = 28
message = "I'm " + str(age) +" years old."
print(message)


##### 주석
# 주석은 간결하고 명료해야 한다.

##### 파이썬 철학
# 추함보다 아름다움이 낫다
# 복잡함보다 단순함이 낫다
# 가독성이 중요하다
# 할 일은 지금 시작하라