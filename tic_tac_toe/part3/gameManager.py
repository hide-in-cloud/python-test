"""

"""
from tic_tac_toe.part3.board import Board
from tic_tac_toe.part3.minimax_ai import minimax_ai
from tic_tac_toe.part3.player import Player


def get_move_human(side):
    print("You are %s." % side)
    x = int(input("Input your X co-ordinate:"))
    y = int(input("Input your Y co-ordinate:"))
    return x - 1, y - 1


def is_valid_move(board, co_ords):
    if board[co_ords[0]][co_ords[1]] is None:
        return True
    else:
        return False


def get_all_line_coords(board):
    height = len(board)
    width = len(board[0])
    rows = []
    for x in range(height):
        row = []
        for y in range(width):
            row.append((x, y))
        rows.append(row)

    cols = []
    for y in range(width):
        col = []
        for x in range(height):
            col.append((x, y))
        cols.append(col)

    diagonals = [
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    return rows + cols + diagonals


def is_board_full(board):
    for row in board:
        for col in row:
            if col is None:
                return False
    return True


def get_winner(board):
    all_line_coords = get_all_line_coords(board)
    for line in all_line_coords:
        line_values = [board[x][y] for (x, y) in line]
        if line_values[0] is not None and line_values.count(line_values[0]) == 3:
            return line_values[0]
    return None


class GameManager:
    def __init__(self, player_o, player_x):
        self.players = [
            ('X', player_x),
            ('O', player_o),
        ]
        self.turn_number = 0

    def get_cur_player(self):
        player_name = self.players[self.turn_number % len(self.players)][1]
        current_player = Player(player_name, get_move_human)
        return current_player

    def get_cur_side(self):
        current_side = self.players[self.turn_number % len(self.players)][0]
        return current_side

    def play(self):
        board = Board(3, 3)
        while True:
            board.render()
            current_player = self.get_cur_player()
            current_side = self.get_cur_side()
            print("It is %s's turn" % current_player.name)

            if current_player.name == 'robot':
                move_coords = minimax_ai(board.board, current_side)
            else:
                while True:
                    move_coords = current_player.get_move(current_side)
                    if is_valid_move(board.board, move_coords):
                        break
                    else:
                        print("Illegal move, try again!")

            board.update(move_coords, current_side)

            winner = get_winner(board.board)
            if winner is not None:
                board.render()
                print("GAME OVER!")
                print("The winner is %s" % current_side)
                break
            if is_board_full(board.board):
                board.render()
                print("It is a DRAW!")
                break

            self.turn_number += 1
