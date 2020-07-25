import sys
import pygame 

from bullet import Bullet

def fire_bullet(ai_settings, screen, ship, bullets):
    """총알을 발사합니다."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    """탄환 위치를 업데이트하고 제거합니다."""
    bullets.update() 
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ 키다운 이벤트에 응답합니다."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """ 키업 이벤트에 응답합니다."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT: 
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """이벤트에 응답합니다."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """가장 최근의 이미지와 화면을 업데이트합니다."""
    # 배경색을 업데이트 합니다.
    screen.fill(ai_settings.bg_color)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # 루프마다 최신 화면을 업데이트 합니다.
    pygame.display.flip()