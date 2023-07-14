"""

"""


class Player:
    def __init__(self, player_name, get_move_function):
        self.name = player_name
        self.get_move_function = get_move_function

    def get_move(self, side):
        return self.get_move_function(side)


