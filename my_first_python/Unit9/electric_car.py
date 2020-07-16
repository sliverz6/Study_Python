""" 전기자동차를 나타낼 때 쓸 수 있는 클래스 세트 """
from car import Car

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

class ElectricCar(Car):
    """전기자동차에만 해당하는 특징을 나타냅니다."""

    def __init__(self, make, model, year):
        """
        부모 클래스의 속성을 초기화한 다음
        전기자동차에만 해당하는 속성을 초기화합니다.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_bttery(self):
        """배터리 크기를 설명하는 문장을 출력합니다."""
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def fill_gas_tank():
        """전기자동차에는 연료 탱크가 없습니다."""
        print('This car doesn\'t need a gas tank!')