import sys
import pygame

from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    #游戏功能
    if event.key == pygame.K_RIGHT:
        # 朝右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 朝左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一个项目
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()
    
def check_keyup_events(event,ship):
    #按键停止移动
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,states,score_board,play_button,ship,aliens,bullets):
    #对鼠标和键盘做出反应
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, states, score_board, play_button, ship, aliens,bullets,  mouse_x, mouse_y)

def update_screen(ai_settings,screen,states,score_board,ship,aliens,bullets,play_button):    
    #屏幕设置
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    
    # 如果游戏没有开始，绘制play_button
    if states.game_active == 0:
        play_button.draw_button()
    elif states.game_active == 1:
        screen.fill(ai_settings.bg_color)
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        aliens.draw(screen)
        # 显示分数
        score_board.show_score()
    elif states.game_active == -1:
        sys.exit()
        
    pygame.display.flip()

def update_bullet(ai_settings,screen,states,score_board,ship,aliens,bullets):
    #更新子弹
    bullets.update()
    # 删除屏幕外的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet) 
    # 检查子弹是否击中了外星人。如果是的话，删除子弹和外星人。
    check_collide_bullet_alien(ai_settings,screen,states,score_board,ship,aliens,bullets)

def update_alien(ai_settings,states,screen,score_board,ship,aliens,bullets):
    #检查外星人的地点，并更新每一个外星人的地点
    
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,states,screen,score_board,ship,aliens,bullets)

    # 检查是否外星人到达屏幕底部
    check_aliens_bottom(ai_settings,states,screen,score_board,ship,aliens,bullets)

def get_number_aliens_x(ai_settings,alien_width):
    #计算外星人
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
    
def get_number_rows(ai_settings,ship_height,alien_height):
    #计算屏幕可以放下多少外星人
    available_space_y = (ai_settings.screen_height - (3 * alien_height) -ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,alien_rows):
    #创造外星人
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * alien_rows
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    #创造外星人组
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges(ai_settings,aliens):
    #外星人碰到边缘反弹
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens) 
            break

def change_fleet_direction(ai_settings,aliens):
    #反弹
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_collide_bullet_alien(ai_settings,screen,states,score_board,ship,aliens,bullets):
    #外星人被子弹击中
    # 打中则删除子弹和外星人
    collide_alien_bullet = pygame.sprite.groupcollide(bullets,aliens,True,True)

    # 打中加分
    if collide_alien_bullet :
        for aliens in collide_alien_bullet.values():
            states.score += ai_settings.alien_points * len(aliens)
            score_board.prep_score()
        check_highest_score(states, score_board)
    # 检查外星人的名单，并创建一个新的外星人组
    if len(aliens) == 0 :
        bullets.empty()
        ai_settings.speedup_game()

        # 提升游戏等级
        states.level += 1
        score_board.prep_level()

        # 创建外星人组
        create_fleet(ai_settings,screen,ship,aliens)

def ship_hit(ai_settings,states,screen,score_board,ship,aliens,bullets):
    #对飞船和外星人之间的碰撞做出反应
    if states.ships_left > 0:
        states.ships_left -= 1
        states.score = 0
        states.level = 1
        ai_settings.initialize_dynamic_settings()
        
        #更新计分面板
        score_board.prep_ship()
        score_board.prep_score()
        score_board.prep_level()
        
        # 清空子弹和外星人列表
        aliens.empty()
        bullets.empty()
        
        # 创建一组新的外星人，并将飞船设置在屏幕的中下方
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        
        sleep(0.5)
    else:
        states.game_active = -1
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,states,screen,score_board,ship,aliens,bullets):
    #检查是否外星人到达屏幕底部
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,states,screen,score_board,ship,aliens,bullets)
            break

def check_play_button(ai_settings,screen,states,score_board,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    #启动
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and states.game_active == 0:
        # 初始化设置
        ai_settings.initialize_dynamic_settings()
        # 使鼠标不可见
        pygame.mouse.set_visible(False)
        # 重置信息
        states.reset_states()
        states.game_active = 1
        
        # 重置计分板和等级
        score_board.prep_score()
        score_board.prep_highest_score()
        score_board.prep_level()
        
        # 清空子弹和外星人列表
        aliens.empty()
        bullets.empty()
        
        # 创造新的外星人组
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

def check_highest_score(states, score_board):
    #检查是否有新的分数，并更新分数
    if states.score > states.highest_score:
        states.highest_score = states.score
        score_board.prep_highest_score()


