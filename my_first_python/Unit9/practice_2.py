##### SECTION 8: 클래스 #####

# 1. 클래스 만들고 사용하기

# 1.1 Dog 클래스 만들기
# class Dog():
#     """개를 모델화하는 시도"""

#     def __init__(self, name, age):
#         """name과 age 속성 초기화"""
#         self.name = name
#         self.age = age
    
#     def sit(self):
#         """명령에 따라 앉는 개"""
#         print(self.name.title() + ' is now sitting.')
#     def roll_over(self):
#         """명령에 따라 구르는 개"""
#         print(self.name.title() + ' rolled over!')

# # 1.2 클래스에서 인스턴스 만들기
# my_dog = Dog('willie', 6)
# print('My dog\'s name is ' + my_dog.name.title() + '.')
# print('My dog is ' + str(my_dog.age) + ' years old.')

# my_dog.sit()
# my_dog.roll_over()

# your_dog = Dog('lucy', 3)
# your_dog.sit()

# 2. 클래스와 인스턴스 다루기

# 2.1 Car 클래스
# class Car():
#     """자동차를 나타내는 코드"""

#     def __init__(self, make, model, year):
#         """자동차를 나타내는 속성 초기화"""
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_descriptive_name(self):
#         """알아보기 쉬운 이름 반환"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())

# 2.2 속성의 기본값 설정
# class Car():
#     """자동차를 나타내는 코드"""

#     def __init__(self, make, model, year):
#         """자동차를 나타내는 속성 초기화"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """알아보기 쉬운 이름 반환"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()

#     def read_odometer(self):
#         """주행거리를 나타내는 문장을 출력합니다."""
#         print('This car has ' + str(self.odometer_reading) + ' miles on it.')

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# 2.3 속성값 바꾸기

# 직접 바꾸기
# class Car():
#     """자동차를 나타내는 코드"""

#     def __init__(self, make, model, year):
#         """자동차를 나타내는 속성 초기화"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """알아보기 쉬운 이름 반환"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()

#     def read_odometer(self):
#         """주행거리를 나타내는 문장을 출력합니다."""
#         print('This car has ' + str(self.odometer_reading) + ' miles on it.')

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# 메서드를 통해 바꾸기
# class Car():
#     """자동차를 나타내는 코드"""

#     def __init__(self, make, model, year):
#         """자동차를 나타내는 속성 초기화"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """알아보기 쉬운 이름 반환"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()

#     def read_odometer(self):
#         """주행거리를 나타내는 문장을 출력합니다."""
#         print('This car has ' + str(self.odometer_reading) + ' miles on it.')

#     def update_odometer(self, mileage):
#         """
#         주행거리 표시기를 주어진 값으로 바꿉니다.
#         주행거리 표시기를 더 적은 값으로 바꾸려고 하면 거부합니다.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('You can\'t roll back an odometer!')

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())

# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

# 메서드를 통해 속성값을 정해진 만큼씩만 바꾸기
# class Car():
#     """자동차를 나타내는 코드"""

#     def __init__(self, make, model, year):
#         """자동차를 나타내는 속성 초기화"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """알아보기 쉬운 이름 반환"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()

#     def read_odometer(self):
#         """주행거리를 나타내는 문장을 출력합니다."""
#         print('This car has ' + str(self.odometer_reading) + ' miles on it.')

#     def update_odometer(self, mileage):
#         """
#         주행거리 표시기를 주어진 값으로 바꿉니다.
#         주행거리 표시기를 더 적은 값으로 바꾸려고 하면 거부합니다.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('You can\'t roll back an odometer!')

#     def increment_odometer(self, miles):
#         """주행거리를 주어진 양만큼 늘립니다."""
#         self.odometer_reading += miles

# my_new_car = Car('subaru', 'outback', 2013)
# print(my_new_car.get_descriptive_name())

# my_new_car.update_odometer(23500)
# my_new_car.read_odometer()

# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()

# 3. 상속

# 3.1 자식 클래스의 __init__() 메서드
# class Car():
#     """자동차를 나타내는 코드"""

#     def __init__(self, make, model, year):
#         """자동차를 나타내는 속성 초기화"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """알아보기 쉬운 이름 반환"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()

#     def read_odometer(self):
#         """주행거리를 나타내는 문장을 출력합니다."""
#         print('This car has ' + str(self.odometer_reading) + ' miles on it.')

#     def update_odometer(self, mileage):
#         """
#         주행거리 표시기를 주어진 값으로 바꿉니다.
#         주행거리 표시기를 더 적은 값으로 바꾸려고 하면 거부합니다.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('You can\'t roll back an odometer!')

#     def increment_odometer(self, miles):
#         """주행거리를 주어진 양만큼 늘립니다."""
#         self.odometer_reading += miles

# class ElectricCar(Car):
#     """전기자동차에만 해당하는 특징을 나타냅니다."""

#     def __init__(self, make, model, year):
#         """부모 클래스의 속성을 초기화합니다."""
#         super().__init__(make, model, year)

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())

# 3.3 자식 클래스의 속성과 메서드 정의
# class Car():
#     """자동차를 나타내는 코드"""

#     def __init__(self, make, model, year):
#         """자동차를 나타내는 속성 초기화"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """알아보기 쉬운 이름 반환"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()

#     def read_odometer(self):
#         """주행거리를 나타내는 문장을 출력합니다."""
#         print('This car has ' + str(self.odometer_reading) + ' miles on it.')

#     def update_odometer(self, mileage):
#         """
#         주행거리 표시기를 주어진 값으로 바꿉니다.
#         주행거리 표시기를 더 적은 값으로 바꾸려고 하면 거부합니다.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('You can\'t roll back an odometer!')

#     def increment_odometer(self, miles):
#         """주행거리를 주어진 양만큼 늘립니다."""
#         self.odometer_reading += miles

# class ElectricCar(Car):
#     """전기자동차에만 해당하는 특징을 나타냅니다."""

#     def __init__(self, make, model, year):
#         """
#         부모 클래스의 속성을 초기화한 다음
#         전기자동차에만 해당하는 속성을 초기화합니다.
#         """
#         super().__init__(make, model, year)
#         self.battery_size = 70

#     def describe_bttery(self):
#         """배터리 크기를 설명하는 문장을 출력합니다."""
#         print('This car has a ' + str(self.battery_size) + '-kWh battery.')

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_bttery()

# 3.4 부모 클래스의 메서드 오버라이드
# class Car():
#     """자동차를 나타내는 코드"""

#     def __init__(self, make, model, year):
#         """자동차를 나타내는 속성 초기화"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """알아보기 쉬운 이름 반환"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()

#     def read_odometer(self):
#         """주행거리를 나타내는 문장을 출력합니다."""
#         print('This car has ' + str(self.odometer_reading) + ' miles on it.')

#     def update_odometer(self, mileage):
#         """
#         주행거리 표시기를 주어진 값으로 바꿉니다.
#         주행거리 표시기를 더 적은 값으로 바꾸려고 하면 거부합니다.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('You can\'t roll back an odometer!')

#     def increment_odometer(self, miles):
#         """주행거리를 주어진 양만큼 늘립니다."""
#         self.odometer_reading += miles

# class ElectricCar(Car):
#     """전기자동차에만 해당하는 특징을 나타냅니다."""

#     def __init__(self, make, model, year):
#         """
#         부모 클래스의 속성을 초기화한 다음
#         전기자동차에만 해당하는 속성을 초기화합니다.
#         """
#         super().__init__(make, model, year)
#         self.battery_size = 70

#     def describe_bttery(self):
#         """배터리 크기를 설명하는 문장을 출력합니다."""
#         print('This car has a ' + str(self.battery_size) + '-kWh battery.')

#     def fill_gas_tank():
#         """전기자동차에는 연료 탱크가 없습니다."""
#         print('This car doesn\'t need a gas tank!')

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_bttery()

# 3.5 속성인 인스턴스
# class Car():
#     """자동차를 나타내는 코드"""

#     def __init__(self, make, model, year):
#         """자동차를 나타내는 속성 초기화"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """알아보기 쉬운 이름 반환"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()

#     def read_odometer(self):
#         """주행거리를 나타내는 문장을 출력합니다."""
#         print('This car has ' + str(self.odometer_reading) + ' miles on it.')

#     def update_odometer(self, mileage):
#         """
#         주행거리 표시기를 주어진 값으로 바꿉니다.
#         주행거리 표시기를 더 적은 값으로 바꾸려고 하면 거부합니다.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('You can\'t roll back an odometer!')

#     def increment_odometer(self, miles):
#         """주행거리를 주어진 양만큼 늘립니다."""
#         self.odometer_reading += miles

# class Battery():
#     """전기자동차의 배터리를 모델화하려는 단순한 시도"""
#     def __init__(self, battery_size=70):
#         """배터리의 속성 초기화"""
#         self.battery_size = battery_size

#     def describe_bettery(self):
#         """배터리 크기를 설명하는 문장 출력"""
#         print('This car has a ' + str(self.battery_size) + '-kWh battery.')

#     def get_range(self):
#         """이 베터리가 제공하는 주행 가능 거리를 출력합니다."""
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270

#         message = 'This car can go approximately ' + str(range)
#         message += ' miles on a full charge.'
#         print(message)

# class ElectricCar(Car):
#     """전기자동차에만 해당하는 특징을 나타냅니다."""

#     def __init__(self, make, model, year):
#         """
#         부모 클래스의 속성을 초기화한 다음
#         전기자동차에만 해당하는 속성을 초기화합니다.
#         """
#         super().__init__(make, model, year)
#         self.battery = Battery()

#     def describe_bttery(self):
#         """배터리 크기를 설명하는 문장을 출력합니다."""
#         print('This car has a ' + str(self.battery_size) + '-kWh battery.')

#     def fill_gas_tank():
#         """전기자동차에는 연료 탱크가 없습니다."""
#         print('This car doesn\'t need a gas tank!')

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_bettery()
# my_tesla.battery.get_range()

# 4. 클래스 임포트

# 4.1 클래스 하나 임포트하기
# from car import Car

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# 4.2 여러 클래스를 모듈에 저장하기
# from car import ElectricCar

# my_tesla = ElectricCar('tesla', 'model s', 2016)

# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_bettery()
# my_tesla.battery.get_range()

# 4.3 모듈에서 여러 클래스 임포트하기
# from car import Car, ElectricCar

# my_bettle = Car('volkswagen', 'beetle', 2016)
# print(my_bettle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())

# 4.4 모듈에서 모듈 임포트
class Food():
	"""음식에 대한 클래스"""
		
	def __init__(self, name, calorie):
			"""속성 초기화"""
			self.name = name
			self.calorie = calorie
	
	def eat(self, amount):
			"""원하는 양을 먹는 메시지를 출력한다"""
			print(amount + '만큼 ' + self.name + '을 먹었다.')

food_0 = Food('김밥', '100')
food_0.eat('한 입')