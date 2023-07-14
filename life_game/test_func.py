from life_game.main import next_board_state

if __name__ == '__main__':
    # TEST 1
    init_state = [
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0],
    ]
    expected_next_state = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    actual_next_state = next_board_state(init_state)
    if actual_next_state == expected_next_state:
        print("PASS TEST 1")
    else:
        print("FAIL TEST 1")
        print("Expected:")
        print(expected_next_state)
        print("Actual:")
        print(actual_next_state)

