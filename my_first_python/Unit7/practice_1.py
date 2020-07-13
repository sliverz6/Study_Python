# 7-1 렌터카
# car = input('어떤 차를 찾고있습니까? ')
# print(car + '을/를 찾는 중입니다.')

# 7-2 레스토랑 예약
# person_number = input('예약 손님은 몇 명입니까? ')
# person_number = int(person_number)

# if person_number >= 9:
#     print('자리가 날 때까지 기다려야 합니다.')
# else: 
#     print('테이블이 준비 되었습니다.')

# 7-3 10의 배수
# number = input('숫자를 입력해주세요. ')
# number = int(number)

# if number % 10 == 0:
#     print(str(number) + ' 은\는 10의 배수입니다.')
# else:
#     print(str(number) + ' 은\는 10의 배수가 아닙니다.')

# 7-4 피자토핑
# while True:
#     topping = input('원하는 토핑을 입력하세요: ')

#     if topping == 'quit':
#         break
#     else: 
#         print('피자에 ' + topping + '을/를 추가합니다.')

# 7-5 영화 입장권
# age = input('나이가 어떻게 됩니까?: ')
# age = int(age)

# if age < 3:
#     price = 0
# elif age <= 12:
#     price = 10
# else: 
#     price = 15

# print('입장료는 ' + str(price) + '$ 입니다.')

# 7-6 세 가지 탈출구
# active = True
# while active:
#     topping = input('원하는 토핑을 입력하세요: ')

#     if topping == 'quit':
#         active = False
#     else: 
#         print('피자에 ' + topping + '을/를 추가합니다.')

# 7-8 제과점
# sandwich_orders = ['치킨샌드위치', '햄치즈샌드위치', 'BLT샌드위치']
# finished_sandwiches = []

# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
    
#     print(sandwich + '가 완성됐습니다!')

#     finished_sandwiches.append(sandwich)

# print('완성된 샌드위치 목록:')
# for sandwich in finished_sandwiches:
#     print('\t' + sandwich)

# 7-9 패스트라미 없음
# sandwich_orders = ['치킨샌드위치', '패스트라미', '햄치즈샌드위치', '패스트라미', 'BLT샌드위치', '패스트라미']
# finished_sandwiches = []

# print('패스트라미는 다 떨어졌습니다..')

# while '패스트라미' in sandwich_orders:
#     sandwich_orders.remove('패스트라미')

# print(sandwich_orders)

# 7-10 꿈같은 휴가
# places = {}

# message = '이번 휴가에 가고싶은 여행지는 어디입니까?: '
# active = True

# while active:
#     name = input('이름을 입력해 주세요: ')
#     place = input(message)

#     places[name] = place
    
#     keep_going = input('계속해서 설문 하시겠습니까? (예 / 아니오)')
#     if keep_going == '아니오':
#         active = False
    
# print('---설문 결과---')
# for name, place in places.items():
#     print('name: ' + name)
#     print('place: ' + place + '\n')

