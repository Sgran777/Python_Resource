import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):#初始化外星人
        super(Alien,self).__init__()
        self.screen = screen
        self.settings = ai_settings
        
        # 设置方向 
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 储存外星人的位置
        self.x = float(self.rect.x)
    
    def blitme(self):
        #装载外星人
        self.screen.blit(self.image,self.rect)

    def update(self):
        #移动外星人
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        #检查是否能碰到screen边缘
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

