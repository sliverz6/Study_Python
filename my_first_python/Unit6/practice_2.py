# 1. 딕셔너리 만들기
person = {
    'name': 'lee',
    'age': 28
}

# 2. 키-값 쌍 접근
print(person['name'])

# 3. 값 수정
person['age'] = 28

# 4. 키-값 쌍 추가
person['gender'] = 'male'

# 5. 키-값 쌍 제거
del person['age']

# 6. 딕셔너리 반복

# 6.1 키-값 쌍 반복
favorite_fruits = {
    'lee': 'apple',
    'park': 'mango'
}

for name, favorite_fruit in favorite_fruits.items():
    print(name)

# 6.2 키에 대해 반복
for name in favorite_fruits.keys():
    print(name)

# 6.3 값에 대해 반복
for favorite_fruit in favorite_fruits.values():
    print(name)

# 7. 중첩

# 7.1 리스트 안에 딕셔너리
# 7.2 딕셔너리 안에 리스
# 7.3 딕셔너리 안에 딕셔너리