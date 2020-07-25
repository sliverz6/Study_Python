import pygame
from pygame.sprite import Group

# 자체 모듈
from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    """게임을 실행합니다."""

    # 설정을 초기화합니다.
    pygame.init()

    # 게임 설정 객체를 만듭니다.
    ai_settings = Settings()

    # 화면 객체를 만듭니다.
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # 우주선을 만듭니다.
    ship = Ship(ai_settings, screen)

    # 총알을 만듭니다.
    bullets = Group()

    # 게임 메인루프를 실행합니다.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()