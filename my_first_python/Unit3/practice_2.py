##### 3-4 손님 리스트 #####
# invite_dinner = ['Lee', 'Park', 'Kim']
# greet_message = 'Hello '
# print(greet_message + invite_dinner[0])
# print(greet_message + invite_dinner[1])
# print(greet_message + invite_dinner[2])


##### 3-5 손님 리스트 바꾸기 #####
# invite_dinner = ['Lee', 'Park', 'Kim']
# greet_message = 'Hello '
# print(invite_dinner[2] + '은 불참입니다.')

# invite_dinner[2] = 'Jung'
# print(greet_message + invite_dinner[0])
# print(greet_message + invite_dinner[1])
# print(greet_message + invite_dinner[2])


##### 3-6 더 많은 손님 #####
# invite_dinner = ['Lee', 'Park', 'Kim']
# greet_message = 'Hello '
# print(invite_dinner[2] + '은 불참입니다.')

# invite_dinner[2] = 'Jung'
# print(greet_message + invite_dinner[0])
# print(greet_message + invite_dinner[1])
# print(greet_message + invite_dinner[2])

# print('더 큰 저녁 식탁을 발견했습니다.')

# invite_dinner.insert(0, 'James')
# invite_dinner.insert(2, 'Mike')
# invite_dinner.append('Peter')

# print(greet_message + invite_dinner[0])
# print(greet_message + invite_dinner[1])
# print(greet_message + invite_dinner[2])
# print(greet_message + invite_dinner[3])
# print(greet_message + invite_dinner[4])
# print(greet_message + invite_dinner[5])


##### 3-6 손님 리스트 줄이기 #####
invite_dinner = ['Lee', 'Park', 'Kim']
greet_message = 'Hello '
print(invite_dinner[2] + '은 불참입니다.')

invite_dinner[2] = 'Jung'
print(greet_message + invite_dinner[0])
print(greet_message + invite_dinner[1])
print(greet_message + invite_dinner[2])

print('더 큰 저녁 식탁을 발견했습니다.')

invite_dinner.insert(0, 'James')
invite_dinner.insert(2, 'Mike')
invite_dinner.append('Peter')

print(greet_message + invite_dinner[0])
print(greet_message + invite_dinner[1])
print(greet_message + invite_dinner[2])
print(greet_message + invite_dinner[3])
print(greet_message + invite_dinner[4])
print(greet_message + invite_dinner[5])

print('저녁 식사에 최대 인원은 2명입니다.')

popped_person = invite_dinner.pop()
print('죄송합니다, ' + popped_person)
popped_person = invite_dinner.pop()
print('죄송합니다, ' + popped_person)
popped_person = invite_dinner.pop()
print('죄송합니다, ' + popped_person)
popped_person = invite_dinner.pop()
print('죄송합니다, ' + popped_person)

print('얼른 오세요. ' + invite_dinner[0])
print('얼른 오세요. ' + invite_dinner[1])

del invite_dinner[1]
del invite_dinner[0]

print(invite_dinner)