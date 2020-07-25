# 기본 모듈
import pygame
from pygame.sprite import Group

# 자체 제작 모듈
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_function as gf

def run_game():
    # 파이게임 초기화
    pygame.init()

    # 게임 설정 객체 생성
    ai_settings = Settings()

    # 화면 객체 생성
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 게임 메인루프
    while True:
        # 이벤트 체크
        gf.check_events(ai_settings, screen, ship, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullet(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()