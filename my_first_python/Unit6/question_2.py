# 6-1 사람
# myself = {'first_name': '이', 'last_name': '승재', 'age': 28, 'city': '부평'}
# print(myself['first_name'])
# print(myself['last_name'])
# print(myself['age'])
# print(myself['city'])

# 6-2 좋아하는 숫자
# favorite_numbers = {
#     'peter': 8,
#     'john': 2,
#     'alice': 7,
# }
# name = 'peter'
# print(name + '가 좋아하는 숫자: ' + str(favorite_numbers[name]))
# name = 'john'
# print(name + '가 좋아하는 숫자: ' + str(favorite_numbers[name]))
# name = 'alice'
# print(name + '가 좋아하는 숫자: ' + str(favorite_numbers[name]))

# 6-3 용어 사전
# dictionary = {
#     '딕셔너리': '값과 쌍의 리스트',
#     '딕셔너리 값 수정': '딕셔너리의 값을 수정한다',
#     '딕셔너리 키-값 추가': '키-값 쌍을 추가한다',
#     '딕셔너리 키-값 제거': '키-값 쌍을 제거한다',
#     '빈 딕셔너리': '값이 없는 딕셔너리'
# }

# print("딕셔너리:")
# print(dictionary['딕셔너리'] + '\n')

# 6-4 용어 사전 2
# dictionary = {
#     '딕셔너리': '값과 쌍의 리스트',
#     '딕셔너리 값 수정': '딕셔너리의 값을 수정한다',
#     '딕셔너리 키-값 추가': '키-값 쌍을 추가한다',
#     '딕셔너리 키-값 제거': '키-값 쌍을 제거한다',
#     '빈 딕셔너리': '값이 없는 딕셔너리'
# }

# for key, value in dictionary.items():
#     print(key + ":")
#     print(value + "\n")

# 6-5 강
# rivers = {
#     'nile': 'egypt',
#     'amazon': 'brasil',
#     'mississippi': 'america',
# }

# for river, country in rivers.items():
#     print(river.title() + " is in " + country.title() + ".")

# for river in rivers.keys():
#     print(river)

# for country in rivers.values():
#     print(country)

# 6-6 설문
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# people = ['jen', 'edward', 'alice', 'peter']

# for person in people:
#     if person in favorite_languages.keys():
#         print('설문에 참여해주셔서 감사합니다.')
#     else:
#         print('설문을 부탁드립니다.')

# 6-7 사람들
# person_0 = {'name': 'lee', 'age': 28}
# person_1 = {'name': 'mary', 'age': 27}
# person_2 = {'name': 'peter', 'age': 35}

# people = [person_0, person_1, person_2]

# for person in people:
#     print("\nName: " + person['name'].title())
#     print("Age: " + str(person['age']))

# 6-8 애완동물
# hotteok = {'animal_type': 'cat', 'master': 'lee seungjae'}
# ggomang = {'animal_type': 'dog', 'master': 'lee haeseok'}

# pets = [hotteok, ggomang]

# for pet in pets:
#     print("\nAnimal type: " + pet['animal_type'])
#     print("Master: " + pet['master'].title())

# 6-9 좋아하는 장소
favorite_places = {
    'lee': ['swiss', 'germany', 'iceland'],
    'park': ['paris', 'roma', 'japan'],
    'kim': ['venice', 'vietnam', 'roma'] 
}

for name, places in favorite_places.items():
    print('\n' + name.title() + "'s favorite place:")
    for place in places:
        print("\t" + place.title())