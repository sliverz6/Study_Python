import pygame

class Ship():
    """우주선 클래스"""
    def __init__(self, ai_settings, screen):
        """우주선 위치, 이미지 초기화"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 우주선 이미지를 불러와서 rect로 바꾸기
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 우주선 rect의 위치 조정
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # rect 값을 부동소수점으로 바꾸기
        self.center = float(self.rect.centerx)
        self.vertical = float(self.rect.centery)

        # 우주선 플래그 설정
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def update(self):
        """우주선 위치 업데이트"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_top and self.rect.top > 0:
            self.vertical -= self.ai_settings.ship_speed_factor
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.vertical += self.ai_settings.ship_speed_factor


        # 소수점 위치를 원래 위치에 대입
        self.rect.centerx = self.center
        self.rect.centery = self.vertical

    def blitme(self):
        """우주선의 현재 위치에 우주선 그리기"""
        self.screen.blit(self.image, self.rect)