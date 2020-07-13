# 1. 단순한 딕셔너리
# ailen_0 = { 'color': 'green', 'points': 5 }
# print(ailen_0['color'])
# print(ailen_0['points'])

# 2. 딕셔너리 다루기

# 2.1 딕셔너리 값에 접근하기
# ailen_0 = { 'color': 'green', 'points': 5 }

# new_points = ailen_0['points']
# print('You just earned ' + str(new_points) + ' points!')

# 2.2 새 키-값 쌍 추가하기
# ailen_0 = { 'color': 'green', 'points': 5 }
# print(ailen_0)

# ailen_0['x_position'] = 0
# ailen_0['y_position'] = 25
# print(ailen_0)

# 2.3 빈 딕셔너리로 시작하기
# ailen_0 = {}

# ailen_0['color'] = 'green'
# ailen_0['points'] = 5

# print(ailen_0)

# 2.4 딕셔너리 값 수정하기
# ailen_0 = { 'color': 'green' }
# print('The ailen is ' + ailen_0['color'] + '.')

# ailen_0['color'] = 'yellow'
# print('The ailen is now ' + ailen_0['color'] + '.')

# ailen_0 = { 'x_position': 0, 'y_position': 25, 'speed': 'medium' }
# print('Origianl x-position: ' + str(ailen_0['x_position']))

# ailen_0['speed'] = 'fast'
# if ailen_0['speed'] == 'slow':
#     x_increment = 1
# elif ailen_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# ailen_0['x_position'] = ailen_0['x_position'] + x_increment

# print('New x-position: ' + str(ailen_0['x_position']))

# 2.5 키-값 쌍 제거하기
# ailen_0 = { 'color': 'green', 'points': 5 } 
# print(ailen_0)

# del ailen_0['points']
# print(ailen_0)

# 2.6 비슷한 객체의 딕셔너리
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
# print('Sarah\'s favorite language is ' + favorite_languages['sarah'].title() + '.')

# 3. 딕셔너리에 루프 실행하기

# 3.1 키-값 쌍 전체에 루프 실행하기
# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }

# for key, value in user_0.items():
#     print('\nKey: ' + key)
#     print('Value: ' + value)

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }

# for name, language in favorite_languages.items():
#     print(name.title() + '\'s favorite language is ' + 
#     language.title() + '.')

# 3.2 딕셔너리의 모든 키에 루프 실행하기
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         print(' Hi ' + name.title() + ' I see your favorite language is ' + 
#         favorite_languages[name].title() + '!')

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }

# if 'erin' not in favorite_languages.keys():
#     print('Erin please take our poll!')

# 3.3 딕셔너리 키에 순서대로 루프 실행하기
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }

# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ' thank you for taking the poll.')

# 3.4 딕셔너리의 모든 값에 루프 실행하기
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }

# print('The following languages have been mentioned:')
# for language in set(favorite_languages.values()):
#     print(language.title())

# 4. 중첩

# 4.1 리스트 안에 딕셔너리 담기
# ailen_0 = { 'color': 'green', 'points': 5 }
# ailen_1 = { 'color': 'yellow', 'points': 10 }
# ailen_2 = { 'color': 'red', 'points': 15 }

# ailens = [ ailen_0, ailen_1, ailen_2 ]

# for ailen in ailens:
#     print(ailen)

# ailens = []

# for ailen_number in range(30):
#     new_ailen = { 'color': 'green', 'points': 5, 'speed': 'slow' }
#     ailens.append(new_ailen)

# for ailen in ailens[0:3]:
#     if ailen['color'] == 'green':
#         ailen['color'] = 'yellow'
#         ailen['speed'] = 'medium'
#         ailen['points'] = 10

# for ailen in ailens[:5]:
#     print(ailen)
# print('...')

# print('Total number of ailens: ' + str(len(ailens)))

# 4.2 딕셔너리 안에 리스트 담기
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese']
# }

# print('You oredered a ' + pizza['crust'] + '-crust pizza with the following topping:')

# for topping in pizza['toppings']:
#     print('\t' + topping)

# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }

# for name, languages in favorite_languages.items():
#     print('\n' + name.title() + '\'s favorite languages are:')
#     for language in languages:
#         print('\t' + language.title())

# # 4.3 딕셔너리 안에 딕셔너리 담기
# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris'
#     }
# }

# for user_name, user_info in users.items():
#     print('\nUsername: ' + user_name)
#     full_name = user_info['first'] + ' ' + user_info['last']
#     location = user_info['location']

#     print('\tFull name: ' + full_name.title())
#     print('\tLocation: ' + location.title())