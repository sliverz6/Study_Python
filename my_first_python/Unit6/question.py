# # 6-1 사람
# person = {
#     '이름': '이승재',
#     '나이': 28,
#     '사는 곳': '부평'
# }
# print(person['이름'])

# # 6-7 사람들
# people = []

# person_0 = {
#     'name': 'Mike',
#     'age': 23,
#     'location': 'paris'
# }

# person_1 = {
#     'name': 'Alice',
#     'age': 27,
#     'location': 'new york'
# }

# person_2 = {
#     'name': 'peter',
#     'age': 31,
#     'location': 'carifornia'
# }

# people.append(person_0)
# people.append(person_1)
# people.append(person_2)

# for person in people:
#     print('Name: ' + person['name'])
#     print('Age: ' + str(person['age']))
#     print('Location: ' + person['location'] + '\n')

# 6-8 애완동물
# pets = []
# dog = {
#     'name': 'beer',
#     'age': 3,
#     'family': 'lee'
# }

# cat = {
#     'name': 'hotteok',
#     'age': 5,
#     'family': 'lee'
# }
# pets.append(dog)
# pets.append(cat)

# for pet in pets:
#     print('Name: ' + pet['name'])
#     print('Family: ' + pet['family'])

# 6-11 도시
cities = {
    'seoul': {
        'country': 'korea',
        'population': 50000000,
        'fact': 'best',
    },
    'danang': {
        'country': 'veitnam',
        'population': 100000000,
        'fact': 'good',
    },
    'paris': {
        'country': 'france',
        'population': 70000000,
        'fact': 'very good',
    }
}

for city, city_infos in cities.items():
    print('\n' + city + ' about:')
    print('Country: ' + city_infos['country'])
