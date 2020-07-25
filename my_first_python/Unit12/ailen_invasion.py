import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    # 파이게임 초기화
    pygame.init()

    # 스크린 객체 만들기
    ai_settings = Settings()
    screen = pygame.display.set_mode(( 
        ai_settings.screen_width, ai_settings.screen_height
    ))
    pygame.display.set_caption("Alien Invasion")

    # 우주선을 만듭니다.
    ship = Ship(ai_settings, screen)
    bullets = Group()

    # 게임 메인 루프
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # 화면에서 사라진 탄환을 제거합니다.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()