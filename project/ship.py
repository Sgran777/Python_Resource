import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self,ai_settings,screen):
        #初始化飞船并设置位置
        super(Ship,self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        
        # 飞船图像
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # 在屏幕中间加载飞船图像
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        #测试并设置飞船位置
        if self.moving_right == True :
            self.center += self.ai_settings.ship_speed_factor
            if self.center >= self.screen_rect.right - 20.0:
                self.center = self.screen_rect.right - 20.0
        if self.moving_left ==True:
            self.center -= self.ai_settings.ship_speed_factor
            if self.center <= self.screen_rect.left + 20.0:
                self.center = self.screen_rect.left + 20.0
        
        # 更新位置
        self.rect.centerx = self.center
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
    def center_ship(self):
        #将飞船设置在屏幕的中下方
        self.center = self.screen_rect.centerx
