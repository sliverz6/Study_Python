class Settings():
    """게임 설정에 관한 클래스입니다."""

    def __init__(self):
        """설정을 초기화합니다."""
        
        # 화면 설정
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 우주선 설정
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 총알 설정
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed_factor = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 외계인 설정
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1