"""
    游戏核心逻辑
"""
import pygame


class Game:
    def __init__(self):
        pass

    def update_drawing(self, screen, snake, food):
        # 画蛇
        for rect in snake.body:
            pygame.draw.rect(screen, (20, 220, 39), rect, 0)
        # 画食物
        pygame.draw.rect(screen, (136, 0, 21), food.rect, 0)

