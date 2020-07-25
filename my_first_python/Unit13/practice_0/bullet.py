import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """총알 클래스"""
    def __init__(self, ai_settings, screen, ship):
        """총알 설정 초기화"""
        super().__init__()
        self.screen = screen
        
        # 총알 rect 생성
        self.rect = pygame.Rect(
            0, 
            0, 
            ai_settings.bullet_width, 
            ai_settings.bullet_height
        )
        # 총알 rect 위치 정하기
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 총알 색, 속도 초기화
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        # 총알 y위치 부동소수점으로 바꾸기
        self.y = float(self.rect.y)

    def update(self):
        """총알을 위로 날려보내기"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """총알의 현재 위치에 맞게 화면에 그리기"""
        pygame.draw.rect(self.screen, self.color, self.rect)