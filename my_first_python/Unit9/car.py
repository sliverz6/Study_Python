"""자동차를 나타낼 때 쓰는 클래스"""

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