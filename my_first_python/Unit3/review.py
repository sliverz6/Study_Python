# 1. 리스트란? 
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)

# 1.1 리스트 항목에 접근하기
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0].title())
# print(bicycles[1])
# print(bicycles[3])
# print(bicycles[-1])

# 1.2 리스트에서 개개의 값 사용
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# message = "My first bicycle was a " + bicycles[0].title() + "."

# print(message)

# 2. 항목 변경, 추가, 제거

# 2.1 리스트 항목 수정하기
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

# 2.2 리스트에 항목 추가하기
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles.insert(0, 'ducati')
# print(motorcycles)

# 2.3 리스트에서 항목 제거
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print('\nA ' + too_expensive.title() + " is too expensive for me.")

# 3. 리스트 정리하기

# 3.1 sort()로 리스트 영구 정렬하기
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(cars)

# 3.2 sorted()로 리스트 임시 정렬하기
# cars = ['bmw', 'audi', 'toyota', 'subaru']

# print("Here is the original list:")
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nHere is the original list again:")
# print(cars)

# 3.3 리스트를 반대 순서로 출력
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
