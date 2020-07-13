# 5-3 외계인 색#1
alien_color = 'yellow'

if alien_color == 'green':
    print('5점을 얻었습니다!')

# 5-4 외계인 색#2
alien_color = 'green'

if alien_color == 'green':
    print('5점을 얻었습니다!')
else:
    print('10점을 얻었습니다!')

# 5-8 관리자에게 인사
users = ['승재', '명준', '규성', '재윤', 'admin']

for user in users:
    if user == 'admin':
        print('관리자님 안녕하세요')
    else:
        print('안녕, ' + user + '.')

# 5-9 사용자 없음
users = []

if users:
    for user in users:
        if user0 == 'admin':
            print('관리자님 안녕하세요')
        else:
            print('안녕, ' + user + '.')
else:
    print('사용자가 있어야 합니다!')
