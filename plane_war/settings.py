class Settings:
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1100
        self.screen_height = 780
        self.bg_color = (220, 220, 220)  # 设置背景颜色

        # 飞船设置
        self.ship_limit = 2

        # 子弹设置
        self.bullet_width = 2
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 外星人设置
        self.fleet_direction = 1  # 1表示右移，-1表示左移

        # 以什么方式加快游戏节奏
        self.speedup_scale = 1.3
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 8
        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """提高游戏节奏"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
        # 提高得分
        self.alien_points = int(self.alien_points * self.speedup_scale)