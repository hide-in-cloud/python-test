"""
    游戏设置类
"""
import pygame


class Settings(object):

    SCREEN_X = 600
    SCREEN_Y = 600

    def __init__(self):
        self.clock = pygame.time.Clock()  # 时钟对象(控制游戏帧数)
        self.is_dead = False
        self.run = True
        self.pause = False
        self.initialize()

    def reset(self):
        self.run = True
        self.pause = False

    def initialize(self):
        self.scores = 0  # 分数

