################################
##### SECTION 5 - 딕셔너리 #####
################################

##### 1. 딕셔너리 기본 #####

# 1.1 딕셔너리 생성
person = {'name': 'lee'}

# 1.2 딕셔너리 값에 접근
print(person['name'])

# 1.3 키-값 쌍 추가
person['age'] = 28

# 1.4 값 수정
person['age'] = 27

# 1.5 키-값 쌍 제거
del person['age']

##### 2. 딕셔너리 반복 #####

# 2.1 키-값 쌍 전체에 반복
person = {'name': 'lee', 'age': 28}
for key, value in person.items():
    print("Key: " + key)
    print("Value: " + str(value))

# 2.2 키에 대해 반복
for key in person:
    print(key)

# 2.3 값에 대해 반복
for value in person.values():
    print(value)

##### 3. 중첩 #####

# 3.1 리스트에 딕셔너리
user_0 = {'name': 'john'}
user_1 = {'name': 'peter'}
users = [user_0, user_1]

# 3.2 딕셔너리에 리스트
person = {
    'name': 'lee',
    'hobbies': ['coding', 'sports']
}

# 3.3 딕셔너리에 딕셔너리
person = {
    'name': 'lee',
    'friends': {
        {'name': 'john'},
        {'name': 'peter'}
    }
}