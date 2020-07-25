import pygame

class Ship():
    """우주선에 관한 클래스입니다."""

    def __init__(self, ai_settings, screen):
        """우주선 이미지를 불러오고 위치를 초기화 합니다."""
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 정밀한 움직임을 위한 설정
        self.center = float(self.rect.centerx)

        # 움직임 플래그 설정
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """키입력 이벤트가 발생하면 우주선의 위치 데이터를 업데이트합니다."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 계산된 현재 위치 소수점 값을 위치 데이터로 설정합니다.
        self.rect.centerx = self.center

    def center_ship(self):
        """우주선을 화면 중앙에 놓습니다."""
        self.center = self.screen_rect.centerx
        
    def blitme(self):
        """우주선의 현재 위치에 우주선을 그립니다."""
        self.screen.blit(self.image, self.rect)