import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """총알 관련 클래스입니다."""

    def __init__(self, ai_settings, screen, ship):
        """총알 위치와 설정을 초기화합니다."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.rect = pygame.Rect(0, 0, self.ai_settings.bullet_width, self.ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.speed_factor = self.ai_settings.bullet_speed_factor
        self.color = self.ai_settings.bullet_color

        self.y = float(self.rect.y)

    def update(self):
        """총알 위치 데이터를 업데이트합니다."""
        self.y -= self.ai_settings.bullet_speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """총알의 현재 위치에 총알을 그립니다."""
        pygame.draw.rect(self.screen, self.color, self.rect)