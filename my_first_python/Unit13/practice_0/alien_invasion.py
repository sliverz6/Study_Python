# 기본 모듈
import pygame
from pygame.sprite import Group

# 자체 제작 모듈
from settings import Settings
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

    # 우주선 객체 생성
    ship = Ship(ai_settings, screen)

    # 총알 그룹 만들기
    bullets = Group()

    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 게임 메인루프
    while True:
        # 이벤트 체크
        gf.check_events(ai_settings, screen, ship, bullets)

        # 우주선 위치 내용 업데이트
        ship.update()

        # 총알 위치 내용 업데이트
        gf.update_bullet(bullets)
        gf.update_aliens(ai_settings, aliens)

        # 화면 갱신
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()