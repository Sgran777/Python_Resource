# 《Python程序设计基础》程序设计作品说明书

题目： 外星人入侵游戏

学院： 21计科04

姓名： 高楷皓

学号： B20210502235

指导教师： 周景

起止日期：2023.11.10-2023.12.10

## 摘要

_介绍本次设计完成的项目的概述，本文的主要内容，总结你主要完成的工作以及关键词。_

这是一个射击小游戏，玩家控制着一艘飞船，使用箭头键左右移动飞船，还可使用空格键进行射击。游戏开始时，一群外星人在屏幕中移动。玩家的任务是射杀这些外星人。玩家将所有外星人都消灭干净后，将出现一群新的外星人，他们移动的速度更快。玩家可以不断过关升级游戏，累计积分。

关键词：pygame，类，函数，编组，图像

## 第1章 需求分析

_本章的内容主要包括系统的需求分析，系统主要需要实现的功能有哪些，可以帮助用户解决哪些问题等等。_

本系统需要大量的数据，以及添加图像的功能；

- 对象：包含飞船、外星人群、子弹、分数系统；
- 飞船：初始及变动位置，个数；
- 外星人：初始及变动位置，个数（一行有多少，几行）、移动速度（水平和垂直）；
- 子弹：初始及变动位置，移动速度；
- 记分：消灭外星人，等级增加即已消灭一群外星人，此时飞船、外星人、子弹移动速度。

## 第2章 分析与设计

_本章的内容主要包括系统的设计，例如：系统架构、系统流程、系统模块、数据库的设计，以及关键的实现，例如：使用的数据结果、算法。_

系统流程：
使用一个while循环不停调用创造好的函数和类等。主要是由飞船发射的子弹去击中外星人后计分，不停累加

系统模块： 
- 游戏初始化
- 新建模块settings，包含Settings类，用于存储与游戏相关的所有设置
- 新建模块game_function，包含很多方法，用于存储与游戏相关的所有操作
- 新建游戏窗口对象
- 创建一艘飞船
- 创建子弹组
- 创建外星人组
- 创建游戏开始按钮
- 创建计分板

## 第3章 软件测试

_本章的内容主要包括以类和函数作为单元进行单元测试，编写的对系统的主要功能的测试用例，以及测试用例执行的测试报告。_

### 单元测试用例
```python
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
```
![Alt text](https://github.com/Sgran777/AlienWar/blob/master/score.png)


## 结论

_本章的内容主要是对项目的总结，项目主要实现了哪些功能，达到了哪些目标，哪些不足之处，可以如何改进。_

## 参考文献
