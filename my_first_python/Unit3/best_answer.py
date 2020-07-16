##############################
##### SECTION 2 - 리스트 #####
##############################

##### 1. 리스트 기본 #####

# 1.1 리스트 생성
fruits = ['orange', 'watermelon', 'pineapple']

# 1.2 리스트 요소 접근
print(fruits[0]) # 0번 인덱스부터 시작
print(fruits[-1]) # 마지막 인덱스

##### 2. 리스트 요소 수정, 추가, 제거 #####

# 2.1 리스트 요소 수정
fruits[0] = 'apple'

# 2.2 리스트 요소 추가
fruits.append('banana') # 마지막에 추가
fruits.insert(1, 'strawberry') # 1번 인덱스에 추가

# 2.3 리스트 요소 제거
del fruits[0] # 0번 인덱스 제거
popped_fruits = fruits.pop() # 마지막 인덱스 제거 후 변수에 담기 (원하는 인덱스도 가능)
fruits.remove('strawberry') # 값으로 제거

print(fruits)

##### 3. 리스트 정렬 #####

cars = ['bmw', 'chevoret', 'audi', 'ferrari', 'jaguar']

# 3.1 임시정렬
print(sorted(cars)) # 알파벳순
print(sorted(cars, reverse=True)) # 알파벳 역순

# 3.2 영구정렬
cars.sort() # 알파벳순
cars.sort(reverse=True) # 알파벳 역순

# 3.3 역순정렬
cars.reverse()

# 3.4 리스트 길이 알아내기
print(len(cars))