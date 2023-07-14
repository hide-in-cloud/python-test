from 贪吃蛇.Snake import Snake
from 贪吃蛇.food import Food
from 贪吃蛇.settings import Settings
from 贪吃蛇.utils import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((Settings.SCREEN_X, Settings.SCREEN_Y))
    pygame.display.set_caption('Snake')

    # 创建对象
    settings = Settings()
    snake = Snake()
    food = Food()

    while True:
        settings.clock.tick(7)  # 画面刷新频率，每秒8次
        check_event(screen, settings, snake, food)
        if settings.run and not settings.pause:
            settings.is_dead = snake.is_dead()  # check_is_dead
            if settings.is_dead:
                settings.run = False
                get_result(screen)  # 检测蛇是否死亡
            else:
                snake.move()    # 蛇移动
                update_food(settings, snake, food)  # 检查食物是否被吃
                update_screen(screen, settings, snake, food)


if __name__ == '__main__':
    main()
