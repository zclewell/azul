import board


def test_add_first_tile(empty_board):
    assert empty_board.place(0, 0) == 1


def test_add_non_adj_tile(empty_board):
    assert empty_board.place(0, 0) == 1
    assert empty_board.place(1, 1) == 1


def test_add_row_adj_tile(empty_board):
    assert empty_board.place(0, 0) == 1
    assert empty_board.place(1, 0) == 2


def test_add_col_adj_tile(empty_board):
    assert empty_board.place(0, 0) == 1
    assert empty_board.place(0, 1) == 2


def test_add_row_and_col_adj_tile(empty_board):
    assert empty_board.place(0, 0) == 1
    assert empty_board.place(1, 1) == 1
    assert empty_board.place(0, 1) == 4


def test_row_bonus_points(empty_board):
    for col_idx in range(board.COLS):
        empty_board.place(0, col_idx)

    assert empty_board.calculate_bonus_points() == board.FULL_ROW_BONUS_MULTIPLIER


def test_col_bonus_points(empty_board):
    for row_idx in range(board.ROWS):
        empty_board.place(row_idx, 0)

    assert empty_board.calculate_bonus_points() == board.FULL_COL_BONUS_MUTLIPLIER


def test_all_tiles_for_color_bonus_points(empty_board):
    for i in range(board.ROWS):
        empty_board.place(i, i)

    assert empty_board.calculate_bonus_points(
    ) == board.ALL_TILES_FOR_COLOR_BONUS_MULTIPLIER
