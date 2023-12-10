class Game_states():
    #追踪游戏并计算信息
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.game_active = 0
        self.reset_states()
        # 最高分设置
        self.highest_score = 0


    def reset_states(self):
        #初始化值
        self.ships_left = self.ai_settings.ship_number
        self.score = 0
        self.level = 1


