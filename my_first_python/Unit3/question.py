# 3-1 단순한 메시지
# names = ['john', 'peter', 'alice', 'kevin']
# print(names[0])
# print(names[1])
# print(names[-2])
# print(names[-1])

# 3-2 단순한 메시지들
# names = ['john', 'peter', 'alice', 'kevin']
# message = "은/는 파이썬을 배우고 있습니다."
# print(names[0].title() + message)
# print(names[1].title() + message)
# print(names[2].title() + message)
# print(names[3].title() + message)

# 3-3 단순한 메시지
# flowers = ['무궁화', '장미', '민들레']
# message = flowers[0] + '는 정말 아름다운 꽃입니다.'
# print(message)

# 3-4 손님 리스트
# invite_dinner = ['peter', 'alice', 'kevin']
# message = '님, 저녁 식사에 초대합니다!'

# print(invite_dinner[0] + message)
# print(invite_dinner[1] + message)
# print(invite_dinner[2] + message)

# 3-5 손님 리스트 바꾸기
# invite_dinner = ['peter', 'alice', 'kevin']
# message = '님, 저녁 식사에 초대합니다!'

# print(invite_dinner[0].title() + message)
# print(invite_dinner[1].title() + message)
# print(invite_dinner[2].title() + message)

# cannot_person = 'peter'
# print(cannot_person.title() + '님은 사정상 불참입니다.')

# invite_dinner[0] = 'mike'

# print(invite_dinner[0].title() + message)
# print(invite_dinner[1].title() + message)
# print(invite_dinner[2].title() + message)

# 3-6 더 많은 손님
# invite_dinner = ['peter', 'alice', 'kevin']
# message = '님, 저녁 식사에 초대합니다!'

# print(invite_dinner[0].title() + message)
# print(invite_dinner[1].title() + message)
# print(invite_dinner[2].title() + message)

# cannot_person = 'peter'
# print(cannot_person.title() + '님은 사정상 불참입니다.\n')

# invite_dinner[0] = 'mike'

# print(invite_dinner[0].title() + message)
# print(invite_dinner[1].title() + message)
# print(invite_dinner[2].title() + message)

# print('\n더 큰 식당으로 장소가 바뀌었습니다!')

# invite_dinner.insert(0, 'james')
# invite_dinner.insert(2, 'tommy')
# invite_dinner.append('julia')

# print(invite_dinner[0].title() + message)
# print(invite_dinner[1].title() + message)
# print(invite_dinner[2].title() + message)
# print(invite_dinner[3].title() + message)
# print(invite_dinner[4].title() + message)
# print(invite_dinner[5].title() + message)

# 3-7 손님 리스트 줄이기
# invite_dinner = ['peter', 'alice', 'kevin']
# message = '님, 저녁 식사에 초대합니다!'

# print(invite_dinner[0].title() + message)
# print(invite_dinner[1].title() + message)
# print(invite_dinner[2].title() + message)

# cannot_person = 'peter'
# print(cannot_person.title() + '님은 사정상 불참입니다.\n')

# invite_dinner[0] = 'mike'

# print(invite_dinner[0].title() + message)
# print(invite_dinner[1].title() + message)
# print(invite_dinner[2].title() + message)

# print('\n더 큰 식당으로 장소가 바뀌었습니다!')

# invite_dinner.insert(0, 'james')
# invite_dinner.insert(2, 'tommy')
# invite_dinner.append('julia')

# print(invite_dinner[0].title() + message)
# print(invite_dinner[1].title() + message)
# print(invite_dinner[2].title() + message)
# print(invite_dinner[3].title() + message)
# print(invite_dinner[4].title() + message)
# print(invite_dinner[5].title() + message)

# print('\n 죄송합니다. 사정상 저녁 식사 초대는 2명으로 바뀌었습니다.')

# popped_person = invite_dinner.pop()
# print('초대하지 못하게 되어서 죄송합니다, ' + popped_person.title() + '님.')
# popped_person = invite_dinner.pop()
# print('초대하지 못하게 되어서 죄송합니다, ' + popped_person.title() + '님.')
# popped_person = invite_dinner.pop()
# print('초대하지 못하게 되어서 죄송합니다, ' + popped_person.title() + '님.')
# popped_person = invite_dinner.pop()
# print('초대하지 못하게 되어서 죄송합니다, ' + popped_person.title() + '님.')

# print('\n' + invite_dinner[0] + '님, 저녁 식사가 준비되었습니다!')
# print(invite_dinner[1] + '님, 저녁 식사가 준비되었습니다!')

# del invite_dinner[1]
# del invite_dinner[0]

# print(invite_dinner)

# 3-8 세계 둘러보기
# most_places = ['norway', 'swiss', 'usa', 'tokyo', 'germany']
# print(most_places)
# print(sorted(most_places))
# print(most_places)
# print(sorted(most_places, reverse=True))
# print(most_places)
# most_places.reverse()
# print(most_places)
# most_places.reverse()
# print(most_places)
# most_places.sort()
# print(most_places)
# most_places.sort(reverse=True)
# print(most_places)

# 3-9 저녁 식사 손님
# invite_dinner = ['peter', 'alice', 'kevin']
# invited_number = len(invite_dinner)
# print('저녁 식사에 초대받은 손님은 총 ' + str(invited_number) + '명 입니다.')

# 3-10 모든 함수
# countries = ['usa', 'germany', 'japan']
# countries.append('france')
# countries.insert(1, 'iceland')
# countries.remove('japan')
# countries.pop()
# print(countries)
# print(sorted(countries))
# countries.sort()
# countries.reverse()
# print(countries)