import pygame

class Ship():
    """우주선 클래스"""

    def __init__(self, ai_settings, screen):
        """우주선 관련 설정을 초기화합니다."""
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """우주선의 현재 위치에 우주선을 그립니다."""
        self.screen.blit(self.image, self.rect)