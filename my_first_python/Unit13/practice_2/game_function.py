import sys 
import pygame

from bullet import Bullet

def fire_bullet(ai_settings, screen, ship, bullets):
    """조건에 맞으면 총알 객체 생성"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullet(bullets):
    """총알 위치를 업데이트하고 화면 밖 총알을 지움"""
    # 총알 위치 내용 업데이트
    bullets.update() # 그룹 안의 모든 총알에게 update 메서드 적용

    # 화면 밖으로 총알 나가면 지우기
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """키 다운 이벤트 체크"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """키 업 이벤트 체크"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """이벤트를 체크하고 응답"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """업데이트된 화면 내용을 갱신"""
    # 배경화면 그리기
    screen.fill(ai_settings.bg_color)

    # 총알 그리기
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 우주선의 현재 위치에 우주선 그리기
    ship.blitme()

    # 루프마다 화면 갱신
    pygame.display.flip()