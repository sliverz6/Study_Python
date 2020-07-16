# 1. 사용자 입력

# # 1.1 input()
# message = input('Enter the message')
# print(message)

# # 1.2 숫자 입력받기
# number = input('Enter number')
# number = int(number)
# print(number)

# 1.3 나머지 연산자 활용?

# 2. while 반복

# 2.1 while 사용
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# 2.2 사용자가 멈출 수 있게 만들기

# 2.2.1 플래그 사용

# 2.2.2 break 사용

# 2.3 continue
# current_number = 1
# while current_number < 10:
#     if current_number % 2 == 0:
#         continue
#     print(current_number)
#     current_number += 1

# 3. 리스트와 딕셔너리에 while 루프 사용

# 3.1 요소를 리스트에서 다른 리스트로 옮기기
# list_0 = ['a', 'b', 'c', 'd']
# list_1 = []

# while list_0:
#     popped_element = list_0.pop()
#     list_1.append(popped_element)

# print(list_1)

# 3.2 리스트에서 특정 값 모두 제거
# list_0 = ['a', 'a', 'b', 'c', 'c', 'c', 'd']

# while 'c' in list_0:
#     list_0.remove('c')

# print(list_0)

# 3.3 사용자가 입력한 값으로 딕셔너리 채우기
# people = {}

# active = True
# while active:
#     name = input('name: ')
#     age = int(input('age: '))

#     people[name] = age

#     active = False

# print(people)