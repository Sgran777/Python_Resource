import pygame.font

class Button():
    def __init__(self,ai_settings,screen,msg):
        #设置开始按钮
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.start_image = pygame.image.load('images/start.bmp')
        
        # 设置大小
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        # 设置字体和大小
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.bottom += 185
        self.prep_msg(msg)
        
    def prep_msg(self,msg):
        #将文本渲染为图像并设置在中心位置
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        #在屏幕上设置按钮
        self.screen.blit(self.start_image,self.screen_rect)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
