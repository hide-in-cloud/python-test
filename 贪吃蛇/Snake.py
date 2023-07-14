"""
    蛇类
"""
import pygame
from 贪吃蛇.settings import Settings


class Snake(object):
    def __init__(self):
        self.direction = pygame.K_RIGHT
        self.body = []
        self.draw()

    def draw(self):
        self.direction = pygame.K_RIGHT
        self.body = []
        for x in range(5):
            self.add_node()

    # 在前端增加蛇块
    def add_node(self):
        left, top = (0, 0)
        if self.body:
            left, top = (self.body[0].left, self.body[0].top)
        node = pygame.Rect(left, top, 25, 25)
        if self.direction == pygame.K_LEFT:
            node.left -= 25
        if self.direction == pygame.K_RIGHT:
            node.left += 25
        if self.direction == pygame.K_UP:
            node.top -= 25
        if self.direction == pygame.K_DOWN:
            node.top += 25
        self.body.insert(0, node)

    def move(self):
        self.del_node()
        self.add_node()

    def del_node(self):
        self.body.pop()

    # check snake is dead or not
    def is_dead(self):
        # 撞墙
        if self.body[0].x not in range(Settings.SCREEN_X):
            return True
        if self.body[0].y not in range(Settings.SCREEN_Y):
            return True
        # 撞自己
        if self.body[0] in self.body[1:]:
            return True
        return False

    # 改变蛇头方向
    def change_direction(self, current_key):
        L_R = (pygame.K_LEFT, pygame.K_RIGHT)
        U_D = (pygame.K_UP, pygame.K_DOWN)
        if current_key in L_R + U_D:
            if (current_key in L_R) and (self.direction in L_R):
                return
            if (current_key in U_D) and (self.direction in U_D):
                return
            self.direction = current_key


if __name__ == '__main__':
    pass
