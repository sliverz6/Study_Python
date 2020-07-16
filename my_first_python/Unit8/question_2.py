# 8-1 메시지
# def display_message():
#     print('함수를 배우자!')

# display_message()

# 8-2 좋아하는 책
# def favorite_book(title):
#     print("내가 좋아하는 책은 " + title + "입니다.")

# favorite_book('나의 첫 파이썬')

# 8-3 티셔츠
# def make_shirt(size='l', message='I love Python'):
#     print("\n티셔츠 사이즈: " + size.title())
#     print("티셔츠 문구: " + message)

# make_shirt('m', '안녕하세요')
# make_shirt(message='반갑습니다', size='l')
# make_shirt()

# 8-4 도시
# def describe_city(name, country):

# 8-6 도시 이름
# def city_country(city, country):
#     """도시와 나라이름을 출력합니다."""
#     message = city.title() + ", " + country.title()
#     return message

# city_0 = city_country('seoul', 'korea')
# city_1 = city_country('new york', 'america')
# city_2 = city_country('danang', 'vietnam')

# print(city_0)
# print(city_1)
# print(city_2)

# 8-7 앨범
# def make_album(artist, title, song_number=''):
#     album = {'artist': artist, 'title': title}
#     if song_number:
#         album['number'] = song_number
#     return album

# levels = make_album('avicii', 'levels', 3)
# break_my_heart = make_album('dua lipa', 'break_my_heart')
# circles = make_album('post malone', 'circles', 4)

# print(levels)
# print(break_my_heart)
# print(circles)

# while True:
#     print("아티스트 앨범을 등록하세요.")
#     print("(종료하려면 '종료'를 입력하세요)")

#     name = input('아티스트: ')
#     if name == '종료':
#         break

#     title = input('타이틀: ')
#     if title == '종료':
#         break

#     album = make_album(name, title)
#     print(album)

# 8-9 챔피언
# champions = ['이즈리얼', '케이틀린', '베인', '바루스', '자야']

# def show_champions(champions):
#     """챔피언들을 출력합니다."""
#     for champion in champions:
#         print(champion)

# show_champions(champions)
    
# 8-10 전설의 챔피언
# champions = ['이즈리얼', '케이틀린', '베인', '바루스', '자야']
# legend_champions = []

# def show_champions(champions):
#     """챔피언들을 출력합니다."""
#     for champion in champions:
#         print(champion)

# def make_legend(champions, legend_champions):
#     """챔피얼들을 전설로 만듭니다."""

#     while champions:
#         legend_champion = champions.pop()
#         legend_champion = "전설의 " + legend_champion

#         legend_champions.append(legend_champion)
#         legend_champions.reverse()

# make_legend(champions, legend_champions)        
# show_champions(legend_champions)

# 8-11 변하지 않은 챔피언
# champions = ['이즈리얼', '케이틀린', '베인', '바루스', '자야']
# cloned_champions = champions[:]
# legend_champions = []

# def show_champions(champions):
#     """챔피언들을 출력합니다."""
#     for champion in champions:
#         print(champion)

# def make_legend(champions, legend_champions):
#     """챔피얼들을 전설로 만듭니다."""

#     while champions:
#         legend_champion = champions.pop()
#         legend_champion = "전설의 " + legend_champion

#         legend_champions.append(legend_champion)
#         legend_champions.reverse()

# make_legend(cloned_champions, legend_champions)        
# show_champions(champions)
# show_champions(legend_champions)

# 8-12 샌드위치
# def make_sandwich(*ingredients):
#     print("\nMaking sandwich with the following ingredients:")
#     for ingredient in ingredients:
#         print("- " + ingredient)

# make_sandwich('ham')
# make_sandwich('tomato', 'letuce')
# make_sandwich('egg', 'cheese', 'potato')

# 8-13 사용자 프로필
# def build_profile(first, last, **user_info):
#     """사용자에 관해 아는 것을 모두 딕셔너리로 만듭니다."""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# user_profile = build_profile(
#     'lee', 'seungjae',
#     location='korea',
#     age=28
# )

# print(user_profile)

# 8-14 롤 챔피언
# def build_champ(name, position, **more_infos):
#     """롤 챔피언 딕셔너리를 리턴합니다."""
#     champ_profile = {}
#     champ_profile['이름'] = name
#     champ_profile['주 포지션'] = position
#     for key, value in more_infos.items():
#         champ_profile[key] = value

#     return champ_profile

# isreal = build_champ(
#     '이즈리얼', '원딜',
#     티어='1티어',
#     난이도='상'
# )

# print(isreal)