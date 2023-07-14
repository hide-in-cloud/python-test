
def get_all_legal_coords(board):
    all_legal_coords = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] is None:
                all_legal_coords.append((x, y))
    return all_legal_coords


def get_opponent(current_player):
    if current_player == 'X':
        return 'O'
    elif current_player == 'O':
        return 'X'
    else:
        raise Exception("Unknown player:"+current_player)
