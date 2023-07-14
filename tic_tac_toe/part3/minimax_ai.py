import copy
import numpy as np
import time
import tic_tac_toe.patr2.engine as engine
import tic_tac_toe.patr2.utils as utils

cache = {}


def get_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function = func(*args, **kwargs)
        execute_time = time.time() - start_time
        print("执行时间:", execute_time)
        return function
    return wrapper


@get_time
def minimax_ai(board, current_player):
    best_move = None
    best_score = None
    legal_moves = utils.get_all_legal_coords(board)
    for move in legal_moves:
        new_board = copy.deepcopy(board)
        engine.execute_move(new_board, move, current_player)
        opp = utils.get_opponent(current_player)
        score = minimax_score(new_board, opp, current_player)
        if best_score is None or score > best_score:
            best_score = score
            best_move = move
    return best_move


def minimax_score(board, current_player, player_to_optimize):
    # if board is a terminal state
    winner = engine.get_winner(board)
    if winner is not None:
        if winner == player_to_optimize:
            return 10
        else:
            return -10
    elif engine.is_board_full(board):
        return 0

    # if board is not a terminal state
    scores = []
    legal_moves = utils.get_all_legal_coords(board)
    for each_move in legal_moves:
        new_board = copy.deepcopy(board)
        engine.execute_move(new_board, each_move, current_player)
        opponent = utils.get_opponent(current_player)
        score = minimax_score(new_board, opponent, player_to_optimize)
        scores.append(score)

    if current_player == player_to_optimize:
        return max(scores)
    else:
        return min(scores)


def minimax_score_with_cache(board, current_player, player_to_optimize):
    np_board = np.array(board)
    np_board_90 = np.rot90(np_board, -1)
    np_board_180 = np.rot90(np_board, -2)
    np_board_270 = np.rot90(np_board, 1)
    board_cache_key = str(np_board)
    board_cache_key_90 = str(np_board_90)
    board_cache_key_180 = str(np_board_180)
    board_cache_key_270 = str(np_board_270)
    if board_cache_key not in cache or board_cache_key_90 not in cache \
            or board_cache_key_180 not in cache or board_cache_key_270 not in cache:
        score = minimax_score(np_board, current_player, player_to_optimize)
        cache[board_cache_key] = score
    return cache[board_cache_key]


def AlphaBeta(board, current_player, player_to_optimize, alpha, beta):
    # if board is a terminal state
    winner = engine.get_winner(board)
    if winner is not None:
        if winner == player_to_optimize:
            return 10
        else:
            return -10
    elif engine.is_board_full(board):
        return 0

    # if board is not a terminal state
    legal_moves = utils.get_all_legal_coords(board)
    for each_move in legal_moves:
        new_board = copy.deepcopy(board)
        engine.execute_move(new_board, each_move, current_player)
        opponent = utils.get_opponent(current_player)
        score = AlphaBeta(new_board, opponent, player_to_optimize, alpha, beta)
        if score > alpha:
            alpha = score
        if score < beta:
            beta = score
        if alpha > beta:
            break

    if current_player == player_to_optimize:
        return alpha
    else:
        return beta


if __name__ == '__main__':
    board = [
        ['X', 'X', 'O'],
        [None, 'O', 'X'],
        [None, None, None]
    ]
    np_board = np.array(board)
    np_board_90 = np.rot90(np_board, -1)
    print(minimax_ai(np_board, 'O'))
    print(minimax_ai(np_board_90, 'O'))
    print(cache)
