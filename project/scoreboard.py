import pygame.font

from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    #显示分数
    def __init__(self, ai_settings, screen, states):
        #初始化分数
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.states = states
        
        # 设置字体
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # 准备初始分数图片
        self.prep_score()
        self.prep_highest_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        # 分数设置
        rounded_score = int(round(self.states.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        pygame.image.save(self.score_image,'score.bmp')
        
        # 把分数放在屏幕的右上方
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        #显示分数
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_highest_score(self):
        #最高分图像
        highest_score = int(round(self.states.highest_score, -1))
        highest_score_str = "{:,}".format(highest_score)
        self.highest_score_image = self.font.render(highest_score_str, True, self.text_color, self.ai_settings.bg_color)
        
        # 将位置设置在屏幕的底部中心
        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.centerx = self.screen_rect.centerx
        self.highest_score_rect.top = self.screen_rect.top

    def prep_level(self):
        #将关卡渲染为图像
        self.level_image = self.font.render(str(self.states.level), True, self.text_color, self.ai_settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ship(self):
        #准备飞船
        self.ships = Group()
        for ship_number in range(self.states.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
