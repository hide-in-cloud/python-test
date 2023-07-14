import sys
import pygame


def show_text(screen, pos, text, color, font_bold=False, font_size=60, font_italic=False):
    # 获取系统字体，设置字体的大小
    current_font = pygame.font.SysFont('宋体', font_size)
    # 设置是否加粗
    current_font.set_bold(font_bold)
    # 设置是否斜体
    current_font.set_italic(font_italic)
    # 文字内容(反锯齿)
    text_fmt = current_font.render(text, True, color)
    # 绘制字体
    screen.blit(text_fmt, pos)


def check_event(screen, settings, snake, food):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            snake.change_direction(event.key)
            if event.key == pygame.K_p and settings.run:  # 按p暂停
                if not settings.pause:  # 游戏暂停
                    settings.pause = not settings.pause
                    show_text(screen, (165, 200), 'GAME PAUSE!', (227, 29, 18))
                    show_text(screen, (135, 260), "press 'P' to start...", (0, 0, 22))
                    pygame.display.flip()  # 让绘制的东西显示在屏幕上
                else:                   # 游戏继续
                    settings.reset()
            elif event.key == pygame.K_SPACE and not settings.run:  # 死后按space重新开始
                replay(screen, settings, snake, food)


def get_result(screen):
    show_text(screen, (165, 200), 'GAME OVER!', (227, 29, 18))
    show_text(screen, (75, 260), "press 'SPACE' to restart...", (0, 0, 22))
    pygame.display.flip()  # 让绘制的东西显示在屏幕上


def update_food(settings, snake, food):
    if food.rect in snake.body:  # 食物被吃
        settings.scores += 100
        food.remove()
        snake.add_node()
    food.set()


def update_drawing(screen, snake, food):
    # 画蛇
    for rect in snake.body:
        pygame.draw.rect(screen, (20, 220, 39), rect, 0)
    # 画食物
    pygame.draw.rect(screen, (136, 0, 21), food.rect, 0)


def update_screen(screen, settings, snake, food):
    screen.fill((255, 255, 255))  # 填充颜色
    update_drawing(screen, snake, food)  # 绘制蛇和食物
    # 显示分数
    show_text(screen, (25, 550), 'Scores:' + str(settings.scores), (223, 223, 223))
    # 暂停提示
    show_text(screen, (510, 10), '暂停:P', (223, 223, 223))
    pygame.display.flip()  # 让绘制的东西显示在屏幕上


def replay(screen, settings, snake, food):
    # 重置游戏设置
    settings.run = True
    settings.is_dead = False
    # 重新绘制画面
    snake.draw()
    # 重置游戏统计信息
    settings.initialize()
    # 更新画面
    update_screen(screen, settings, snake, food)
