import pygame

from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    # 파이게임과 설정, 화면 객체 초기화
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # 우주선을 만듭니다.
    ship = Ship(ai_settings, screen)

    # 게임의 메인 루프를 시작합니다.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)       

run_game()