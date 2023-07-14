from tic_tac_toe.part1.game_functions import *
from tic_tac_toe.part1.ai_utils import *


def man_machine_mode():
    board = new_board()
    players = ['X', 'O']
    turn_number = 0
    while True:
        render(board)
        current_player = players[turn_number % len(players)]
        print('It is %s turn' % current_player)
        if current_player == 'O':
            move_coords = finds_winning_moves_ai(board, 'O')
            if move_coords is None:
                move_coords = finds_winning_moves_ai(board, 'X')
                if move_coords is None:
                    move_coords = moves_ai(board)
        else:
            while True:
                try:
                    move_coords = get_move()
                    if is_valid_move(board, move_coords):
                        break
                    else:
                        print("--Illegal move, try again!")
                except Exception as e:
                    print("--Exception throw:", e)
                    print("--Invalid input, try again!")
        execute_move(board, move_coords, current_player)
        if is_game_over(board, current_player):
            render(board)
            print("GAME OVER!")
            print("The winner is %s" % current_player)
            break
        if is_board_full(board):
            render(board)
            print("It is a DRAW!")
            break
        turn_number += 1


if __name__ == '__main__':
    man_machine_mode()
