# 9-1 레스토랑
# class Restaurant():
#     """레스토랑 클래스"""
#     def __init__(self, name, cuisine):
#         """레스토랑 속성 초기화"""
#         self.name = name
#         self.cuisine = cuisine
    
#     def describe_restaurant(self):
#         """레스트랑 정보 출력"""
#         print('레스토랑 이름: ' + self.name)
#         print('레스토랑 요리: ' + self.cuisine)

#     def open_restaurant(self):
#         """식당이 오픈했다는 메시지 출력"""
#         print(self.name + '이/가 오픈했습니다!')

# kimbab = Restaurant('김밥천국', '떡볶이')
# kimbab.describe_restaurant()
# kimbab.open_restaurant()

# 9-2 세 레스토랑
# class Restaurant():
#     """레스토랑 클래스"""
#     def __init__(self, name, cuisine):
#         """레스토랑 속성 초기화"""
#         self.name = name
#         self.cuisine = cuisine
    
#     def describe_restaurant(self):
#         """레스트랑 정보 출력"""
#         print('레스토랑 이름: ' + self.name)
#         print('레스토랑 요리: ' + self.cuisine)

#     def open_restaurant(self):
#         """식당이 오픈했다는 메시지 출력"""
#         print(self.name + '이/가 오픈했습니다!')

# kimbab = Restaurant('김밥천국', '떡볶이')
# outback = Restaurant('아웃백 스테이크 하우스', '스테이크')
# bossam = Restaurant('원할머니 보쌈', '보쌈')

# kimbab.describe_restaurant()
# outback.describe_restaurant()
# bossam.describe_restaurant()

# 9-3 사용자
# class User():
#     """사용자 정보 클래스"""
#     def __init__(self, first_name, last_name, age):
#         """속성 초기화"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def describe_user(self):
#         full_name = self.first_name + ' ' + self.last_name
#         print('이름: ' + full_name.title())
#         print('나이: ' + str(self.age))

#     def greet_user(self):
#         print('안녕하세요, ' + self.last_name + '님.')

# user_0 = User('이', '승재', 28)
# user_0.describe_user()
# user_0.greet_user()

# 9-4 고객 숫자
# class Restaurant():
#     """레스토랑 클래스"""
#     def __init__(self, name, cuisine):
#         """레스토랑 속성 초기화"""
#         self.name = name
#         self.cuisine = cuisine
#         self.number_served = 0
    
#     def describe_restaurant(self):
#         """레스트랑 정보 출력"""
#         print('레스토랑 이름: ' + self.name)
#         print('레스토랑 요리: ' + self.cuisine)

#     def open_restaurant(self):
#         """식당이 오픈했다는 메시지 출력"""
#         print(self.name + '이/가 오픈했습니다!')

#     def set_number_server(self, number):
#         """서빙한 고객 숫자를 재설정"""
#         self.number_served = number

#     def increment_number_server(self, amount):
#         """서빙한 고객 숫자를 증가량만큼 더함"""
#         self.number_served += amount

# kimbab = Restaurant('김밥천국', '떡볶이')
# print(kimbab.number_served)

# kimbab.number_served = 3
# print(kimbab.number_served)

# kimbab.set_number_server(10)
# print(kimbab.number_served)

# kimbab.increment_number_server(2)
# print(kimbab.number_served)

# 9-5 로그인 시도
# class User():
#     """사용자 정보 클래스"""
#     def __init__(self, first_name, last_name, age):
#         """속성 초기화"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.login_attempts = 0

#     def describe_user(self):
#         full_name = self.first_name + ' ' + self.last_name
#         print('이름: ' + full_name.title())
#         print('나이: ' + str(self.age))

#     def greet_user(self):
#         print('안녕하세요, ' + self.last_name + '님.')

#     def increment_login_attempts(self):
#         """ 로그인 횟수 1 추가"""
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         """로그인 횟수 초기화"""
#         self.login_attempts = 0

# user_0 = User('이', '승재', 28)
# user_0.increment_login_attempts()
# user_0.increment_login_attempts()
# user_0.increment_login_attempts()
# print(user_0.login_attempts)
# user_0.reset_login_attempts()
# print(user_0.login_attempts)

# 9-6 아이스크림 가판대
# class Restaurant():
#     """레스토랑 클래스"""
#     def __init__(self, name, cuisine):
#         """레스토랑 속성 초기화"""
#         self.name = name
#         self.cuisine = cuisine
#         self.number_served = 0
    
#     def describe_restaurant(self):
#         """레스트랑 정보 출력"""
#         print('레스토랑 이름: ' + self.name)
#         print('레스토랑 요리: ' + self.cuisine)

#     def open_restaurant(self):
#         """식당이 오픈했다는 메시지 출력"""
#         print(self.name + '이/가 오픈했습니다!')

#     def set_number_server(self, number):
#         """서빙한 고객 숫자를 재설정"""
#         self.number_served = number

#     def increment_number_server(self, amount):
#         """서빙한 고객 숫자를 증가량만큼 더함"""
#         self.number_served += amount

# class IceCreamStand(Restaurant):
#     """아이스크림 가판대 클래스"""
#     def __init__(self, name, cuisine):
#         """부모 속성 초기화"""
#         super().__init__(name, cuisine)
#         self.flavors = '바닐라'

#     def show_flavors(self):
#         print('아이스크림 맛: ' + self.flavors)

# ice_cream = IceCreamStand('베스킨라빈스', '아이스크림')
# ice_cream.show_flavors()

# 9-7 관리자
# class User():
#     """사용자 정보 클래스"""
#     def __init__(self, first_name, last_name, age):
#         """속성 초기화"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def describe_user(self):
#         full_name = self.first_name + ' ' + self.last_name
#         print('이름: ' + full_name.title())
#         print('나이: ' + str(self.age))

#     def greet_user(self):
#         print('안녕하세요, ' + self.last_name + '님.')

# class Admin(User):
#     """관리자 클래스"""
#     def __init__(self, first_name, last_name, age):
#         """부모 클래스 속성 초기화"""
#         super().__init__(first_name, last_name, age)
#         self.privileges = [
#             'can add post',
#             'can delete post',
#             'can ban user'
#         ]

#     def show_privileges(self):
#         print('관리자 권한들입니다:')
#         for privilege in self.privileges:
#             print(privilege)

# admin = Admin('Lee', 'Seungjae', 28)
# admin.show_privileges()

# 9-8 권한
# class User():
#     """사용자 정보 클래스"""
#     def __init__(self, first_name, last_name, age):
#         """속성 초기화"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def describe_user(self):
#         full_name = self.first_name + ' ' + self.last_name
#         print('이름: ' + full_name.title())
#         print('나이: ' + str(self.age))

#     def greet_user(self):
#         print('안녕하세요, ' + self.last_name + '님.')

# class Privileges():
#     """권한 속성 클래스"""
#     def __init__(self):
#         self.privileges = [
#             'can add post',
#             'can delete post',
#             'can ban user'
#         ]

#     def show_privileges(self):
#         """관리자 권한을 출력합니다"""
#         print('관리자 권한들입니다:')
#         for privilege in self.privileges:
#             print(privilege)

# class Admin(User):
#     """관리자 클래스"""
#     def __init__(self, first_name, last_name, age):
#         """부모 클래스 속성 초기화"""
#         super().__init__(first_name, last_name, age)
#         self.privilege = Privileges()

# admin = Admin('Lee', 'Seungjae', 28)
# admin.privilege.show_privileges()

# 9-9 배터리 업그레이드
class Car():
    """자동차를 나타내는 코드"""

    def __init__(self, make, model, year):
        """자동차를 나타내는 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """알아보기 쉬운 이름 반환"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """주행거리를 나타내는 문장을 출력합니다."""
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        """
        주행거리 표시기를 주어진 값으로 바꿉니다.
        주행거리 표시기를 더 적은 값으로 바꾸려고 하면 거부합니다.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')

    def increment_odometer(self, miles):
        """주행거리를 주어진 양만큼 늘립니다."""
        self.odometer_reading += miles

class Battery():
    """전기자동차의 배터리를 모델화하려는 단순한 시도"""
    def __init__(self, battery_size=70):
        """배터리의 속성 초기화"""
        self.battery_size = battery_size

    def describe_bettery(self):
        """배터리 크기를 설명하는 문장 출력"""
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        """이 베터리가 제공하는 주행 가능 거리를 출력합니다."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge.'
        print(message)
    
    def upgrade_battery(self):
        """배터리 용량을 체크 후 용량을 늘립니다."""
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    """전기자동차에만 해당하는 특징을 나타냅니다."""

    def __init__(self, make, model, year):
        """
        부모 클래스의 속성을 초기화한 다음
        전기자동차에만 해당하는 속성을 초기화합니다.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_bettery(self):
        """배터리 크기를 설명하는 문장을 출력합니다."""
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def fill_gas_tank():
        """전기자동차에는 연료 탱크가 없습니다."""
        print('This car doesn\'t need a gas tank!')

my_car = ElectricCar('폭스바겐', 'bmw', 2016)
my_car.battery.get_range()

my_car.battery.upgrade_battery()
my_car.battery.get_range()