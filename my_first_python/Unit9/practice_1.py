# 1. 클래스 만들기
class Food():
    """음식 클래스"""
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def show_info(self):
        print('Name: ' + self.name + ' Price: ' + str(self.price))

    def eat(self):
        print('Eat ' + self.name)

    def update_price(self, new_price):
        self.price = new_price

# 1.1 인스턴스 만들기
steak = Food('steak', 19)
steak.show_info()
steak.eat()

# 1.2 속성 기본값 설정
# 1.3 속성 바꾸기
# 1.3.1 직접 바꾸기
steak.price = 20
steak.show_info()

# 1.3.2 메서드로 바꾸기
steak.update_price(30)
steak.show_info()

# 2. 상속
class FastFood(Food):
    """패스트푸드 클래스"""
    def __init__(self, name, price):
        """부모 클래스의 속성을 초기화"""
        super().__init__(name, price)

hamberger = FastFood('hamberger', 9)
hamberger.show_info()

# 2.1 부모 클래스 메서드 덮어쓰기

# 3. 모듈 임포트