import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """우주선에서 발사한 탄환을 관리하는 클래스"""

    def __init__(self, ai_settigns, screen, ship):
        """우주선의 현재 위치에 탄환 객체를 만듭니다."""
        super().__init__()
        self.screen = screen

        # (0, 0) 좌표에 탄환을 만든 다음 정확한 위치에 지정합니다. 
        self.rect = pygame.Rect(0, 0, ai_settigns.bullet_width, ai_settigns.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top 
    
        # 탄환의 위치를 부동소수점 숫자로 저장합니다. 
        self.y = float(self.rect.y)
        self.color = ai_settigns.bullet_color 
        self.speed_factor = ai_settigns.bullet_speed_factor

    def update(self):
        """화면 위를 향해 탄환을 움직입니다."""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """화면에 탄환을 그립니다."""
        pygame.draw.rect(self.screen, self.color, self.rect)