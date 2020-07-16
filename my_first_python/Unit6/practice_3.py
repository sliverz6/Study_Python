# # 1. 딕셔너리 기본

# # 1.1 딕셔너리 값에 접근
# # ailen_0 = { 'color': 'yellow' }
# # print(ailen_0['color'])

# # # 1.2 새 키-값 쌍 추가
# # ailen_0['points'] = 5
# # print(ailen_0)

# # # 1.3 딕셔너리 값 수정
# # ailen_0['color'] = 'green'

# # # 1.4 딕셔너리 값 제거
# # del ailen_0['color']

# # 2. 딕셔너리 반복

# # 2.1 키-값 쌍 전체에 반복
# person = {
#     'name': 'lee',
#     'age': 28,
#     'location': 'korea'
# }

# for key, value in person.items():
#     print(key)
#     print(value)

# # 2.2 모든 키에 반복
# for key in person.keys():
#     print(key)

# for key in person:
#     print(key)

# # 2.3 모든 값에 반복
# for value in person.values():
#     print(value)

# # 3. 중첩

# # 3.1 리스트 안에 딕셔너리
# ailen_0 = { 'color': 'yellow' }
# ailen_1 = { 'color': 'green' }
# ailens = [ailen_0, ailen_1]

# # 3.2 딕셔너리 안에 리스트
# person = {
#     'hobbies': ['coding', 'sports']
# }

# # 3.3 딕셔너리 안에 딕셔너리
# person = {
#     'country': {
#         'name': 'korea',
#     }
# }