# 1. 함수 정의
# def greet_user():
#     """간단한 환영 인사를 표시합니다."""
#     print("Hello!")

# greet_user()

# 1.1 함수에 정보 전달
# def greet_user(username):
#     """간단한 환영 인사를 표시합니다."""
#     print('Hello, ' + username.title() + '!')

# greet_user('jesse')

# 1.2 매개변수

# 2. 매개변수 전달

# 2.1 위치형 매개변수
# def describe_pet(animal_type, pet_name):
#     """애완 동물에 관한 정보를 출력합니다."""
#     print('\nI have a ' + animal_type + '.')
#     print('My ' + animal_type + '\'s name is ' + pet_name.title() + '.')

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# 2.2 키워드 매개변수
# def describe_pet(animal_type, pet_name):
#     """애완 동물에 관한 정보를 출력합니다."""
#     print('\nI have a ' + animal_type + '.')
#     print('My ' + animal_type + '\'s name is ' + pet_name.title() + '.')

# describe_pet(animal_type='hamster', pet_name='harry')

# 2.3 기본값
# def describe_pet(pet_name, animal_type='dog'):
#     """애완 동물에 관한 정보를 출력합니다."""
#     print('\nI have a ' + animal_type + '.')
#     print('My ' + animal_type + '\'s name is ' + pet_name.title() + '.')


# describe_pet(pet_name='willie')

# 2.4 동등한 함수 호출

# 2.5 매개변수 에러 피하기

# 3. 반환값

# 3.1 단순한 값 반환하기
# def get_formatted_name(first_name, last_name):
#     """읽기 쉬운 전체 이름을 반환합니다."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# 3.2 매개변수를 옵션으로 만들기
# def get_formatted_name(first_name, last_name, middle_name=''):
#     """읽기 쉬운 전체 이름을 반환합니다."""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

# 3.3 딕셔너리 반환하기
# def build_person(first_name, last_name, age=''):
#     """사람에 관한 정보 딕셔너리를 반환합니다."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

# 3.4 함수에서 while 루프 사용하기
# def get_formatted_name(first_name, last_name):
#     """읽기 쉬운 전체 이름을 반환합니다."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# while True:
#     print('\nPlease tell me your name:')
#     print('(enter \'q\' at any time to quit)')

#     f_name = input('First name: ')
#     if f_name == 'q':
#         break

#     l_name = input('Last name: ')
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print('\nHello, ' + formatted_name + '!')

# 4. 리스트 전달
# def greet_user(names):
#     """리스트의 각 사용자에게 단순한 환영 인사를 출력합니다."""
#     for name in names:
#         msg = 'Hello, ' + name.title() + '!'
#         print(msg)

# username = ['hannah', 'ty', 'margot']
# greet_user(username)

# 4.1 함수에서 리스트 수정하기
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()

#     print('Printing model: ' + current_design)
#     completed_models.append(current_design)

# print('\nThe following models have been printed:')
# for completed_model in completed_models:
#     print(completed_model)

# def print_models(unprinted_designs, completed_models):
#     """
#     남은 것이 없을 때까지 각 디자인의 출력을 시뮬레이트 합니다.
#     출력한 각 디자인을 completed_models로 옮깁니다.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()

#         print('Printing model: ' + current_design)
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """출력이 끝난 모델을 모두 표시"""
#     print('\nThe following models have been printed.')
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# 5. 매개변수를 임의의 숫자만큼 전달하기
# def make_pizza(*toppings):
#     """만들려고 하는 피자를 요약합니다."""
#     print('\nMaking a pizza with the following toppings:')
#     for topping in toppings:
#         print('-' + topping)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 5.1 위치형 매개변와 임의의 매개변수 함께 쓰기
# def make_pizza(size, *toppings):
#     """만들려고 하는 피자를 요약합니다."""
#     print('\nMaking a ' + str(size) + '-inch pizza with the following toppings:')
#     for topping in toppings:
#         print('-' + topping)

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 5.2 임의의 키워드 매개변수 사용하기
# def build_profile(first, last, **user_info):
#     """사용자에 관해 아는 것을 모두 딕셔너리로 만듭니다."""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# user_profile = build_profile(
#     'albert', 
#     'einstein',
#     location='princeton',
#     field='physics'
# )

# print(user_profile)

# 6. 함수를 모듈에 저장

# 6.1 전체 모듈 임포트하기