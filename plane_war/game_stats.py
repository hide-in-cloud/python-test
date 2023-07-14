import os


class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings, filename):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚启动时处于活动状态
        self.game_active = False

        # 最高得分
        self.high_score = 0
        self.read_high_score(filename)

    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self, filename):
        """从文件中读取最高得分"""
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as rfile:
                    self.high_score = int(rfile.read())
            except (FileNotFoundError, ValueError):
                print('读取最高得分文件时发生异常')
