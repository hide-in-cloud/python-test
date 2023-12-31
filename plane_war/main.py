import pygame
from pygame.sprite import Group
import plane_war.game_functions as gf
from plane_war.button import Button
from plane_war.game_stats import GameStats
from plane_war.scoreboard import Scoreboard
from plane_war.settings import Settings
from plane_war.ship import Ship


def run_game():
    # 初始化pygame、设置和并屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建play按钮
    play_button = Button(screen, "Play")

    # 创建存储游戏统计信息的实例，并创建记分牌，最高分保存在文件中
    filename = "highest_score.txt"
    stats = GameStats(ai_settings, filename)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船、创建一个用于存储子弹的编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, filename)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        # 更新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


if __name__ == '__main__':
    run_game()
