"""
    食物类
"""
import pygame
import random
from 贪吃蛇.settings import Settings


class Food(object):
    def __init__(self):
        self.rect = pygame.Rect(-25, 0, 25, 25)

    def set(self):
        if self.rect.x == -25:
            all_position = []
            # 不靠墙太近 25 ~ screen_x -25 之间
            for position in range(25, Settings.SCREEN_X - 25, 25):
                all_position.append(position)
            self.rect.left = random.choice(all_position)
            self.rect.top = random.choice(all_position)

    def remove(self):
        self.rect.x = -25
