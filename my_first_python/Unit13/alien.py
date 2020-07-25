import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """함대에 속한 외계인 하나를 나타내는 클래스"""

    def __init__(self, ai_settings, screen):
        """외계인을 초기화하고 시작 위치를 지정합니다."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    # def blitme(self):
    #     """외계인의 현재 위치에 외계인을 그립니다."""
    #     self.screen.blit(self.image, self.rect)