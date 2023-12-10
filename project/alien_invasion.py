import sys
import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_states import Game_states
from button import Button
from scoreboard import Scoreboard

import game_functions as gamef

def run_game():
    # 屏幕设置
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien War")

    # 创建按钮
    play_button = Button(ai_settings, screen, "Play")
    
    #创建game states
    games = Game_states(ai_settings)

    # 创建计分板
    score_board = Scoreboard(ai_settings, screen, games)

    # 创建背景
    screen.fill(ai_settings.bg_color)

    # 创建ship
    ship = Ship(ai_settings,screen)

    # 创建子弹
    bullets = Group()

    # 创建外星人
    aliens = Group()
    if games.game_active == 1:
        gamef.create_fleet(ai_settings,screen,ship,aliens)
    while True:
        gamef.check_events(ai_settings,screen,games,score_board,play_button,ship,aliens,bullets)
        if games.game_active == 1:
            ship.update()
            gamef.update_bullet(ai_settings,screen,games,score_board,ship,aliens,bullets)
            gamef.update_alien(ai_settings,games,screen,score_board,ship,aliens,bullets)
        #更新游戏屏幕
        gamef.update_screen(ai_settings,screen,games,score_board,ship,aliens,bullets,play_button) 

run_game()

