# 8-1 메시지
# def display_message():
#     print('함수는 코드 집합이다.')

# display_message()

# 8-2 좋아하는 책
# def favorite_book(title):
#     print('내가 좋아하는 책은 ' + title + '입니다.')

# favorite_book('나의 첫 파이썬')

# 8-3 티셔츠
# def make_shirt(size, message):
#     print('\nThis shirt\'s size is ' + str(size) + '.')
#     print('And this shirt\'s message is ' + message)

# make_shirt(10, 'I love you')
# make_shirt(message='I love you', size=10)

# 8-4 L 사이즈
# def make_shirt(size='L', message="I love Python"):
#     print('\nThis shirt\'s size is ' + str(size) + '.')
#     print('And this shirt\'s message is ' + message)

# make_shirt('S')
# make_shirt('M', 'I love Data Science')

# 8-5 도시
# def describe_city(name, country_name='korea'):
#     print('\n' + name + ' is in ' + country_name + '.')

# describe_city('seoul')
# describe_city(name='busan')
# describe_city('paris', 'france')

# 8-6 도시 이름
# def city_country(city, country):
#     message = city + ', ' + country
#     return message

# print(city_country('seoul', 'korea'))
# print(city_country('new york', 'america'))
# print(city_country('paris', 'france'))

# 8-7 앨범
# def make_album(musician, title, amount=''):
#     if amount:
#         album = {'musician': musician, 'title': title, 'amount': amount}
#     else:
#         album = {'musician': musician, 'title': title}
#     return album

# print(make_album('deadmau5', 'strobe', 2))
# print(make_album('avicii', 'levels'))
# print(make_album('hardwell', 'cannonball'))

# 8-8 사용자 앨범
# def make_album(musician, title, amount=''):
#     if amount:
#         album = {'musician': musician, 'title': title, 'amount': amount}
#     else:
#         album = {'musician': musician, 'title': title}
#     return album

# while True:
#     print('\n가수 이름과 음악 제목을 입력하세요.')
#     print('(종료를 원한다면 \'q\'를 입력하세요.) ')

#     musician_name = input('가수 이름: ')
#     if musician_name == 'q':
#         break

#     title_name = input('음악 이름: ')
#     if title_name == 'q':
#         break

#     album = make_album(musician_name, title_name)
#     print(album)

# 8-9 UFC 선수
# fighters = ['코너 맥그리거', '존존스', '우스만']

# def show_fighters(fighters):
#     for fighter in fighters:
#         print(fighter)

# show_fighters(fighters)

# 8-10 훌륭한 선수
# fighters = ['코너 맥그리거', '존존스', '우스만']

# def make_great(fighters):
#     great_fighters = []
#     for fighter in fighters:
#         great_fighter = '훌륭한 ' + fighter
#         great_fighters.append(great_fighter)

#     return great_fighters

# def show_fighters(fighters):
#     for fighter in fighters:
#         print(fighter)

# fighters = make_great(fighters)
# show_fighters(fighters)

# 8-11 변하지 않은 운동선수
# fighters = ['코너 맥그리거', '존존스', '우스만']

# def make_great(fighters):
#     great_fighters = []
#     for fighter in fighters:
#         great_fighter = '훌륭한 ' + fighter
#         great_fighters.append(great_fighter)

#     return great_fighters

# def show_fighters(fighters):
#     for fighter in fighters:
#         print(fighter)

# new_fighters = make_great(fighters[:])
# show_fighters(fighters)
# show_fighters(new_fighters)

# 8-12 샌드위치
# def make_sandwich(*toppings):
#     print('\n주문한 샌드위치 토핑입니다:')
#     for topping in toppings:
#         print('\t' + topping)

# make_sandwich('햄')
# make_sandwich('햄', '치즈', '베이컨')
# make_sandwich('토마토', '베이컨', '후라이')

# 8-13 사용자 프로필
# def user_profile(first_name, last_name, **user_info):
#     """사용자 정보를 입력받아 딕셔너리로 리턴합니다"""
#     profile = {}
#     profile['firstname'] = first_name
#     profile['lastname'] = last_name
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# my_profile = user_profile(
#     'Lee', 
#     'Seungjae', 
#     age=28,
#     location='부평'
# )

# print(my_profile)

# 8-14 자동차
# def make_car(maker, model, **car_info):
#     car_profile = {}
#     car_profile['maker'] = maker
#     car_profile['model'] = model
#     for key, value in car_info.items():
#         car_profile[key] = value
#     return car_profile

# car = make_car('폭스바겐', 'bmw', 색상='black')

# print(car)