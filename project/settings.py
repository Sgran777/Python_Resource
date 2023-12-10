class Settings():
    #存储游戏的所有类
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        
        # 外星人设置
        self.alien_speed_factor = 0.5       
        self.fleet_drop_speed = 3        
        self.fleet_direction = 1
        
        # 飞船设置
        self.ship_number = 3
        self.speedup_scale = 1.2
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #游戏速度
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1.2
        self.alien_speed_factor = 0.2
        self.fleet_direction = 1
        self.alien_points = 50

    def speedup_game(self):
        #加速
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale 
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

