from magic import rotate
from copy import deepcopy

ROWS = 5
COLS = 5

FULL_ROW_BONUS_MULTIPLIER = 2
FULL_COL_BONUS_MUTLIPLIER = 7
ALL_TILES_FOR_COLOR_BONUS_MULTIPLIER = 10


class Board():
    def __init__(self):
        self._board = [[False for r in range(ROWS)] for c in range(COLS)]
        self._score = 0

    def __str__(self):
        str_rep = ''
        for row_idx in range(ROWS):
            str_rep = str_rep + \
                list(
                    map(lambda x: 1 * x, self._board[row_idx])).__str__() + '\n'
        return str_rep[:-1]

    def place(self, row, col):
        assert row < ROWS
        assert col < COLS

        self._board[row][col] = True

        new_points = 1  # Always at least one point for the tile itself
        were_adj_row = False
        were_adj_col = False

        # Count adjacent tiles moving to the right in the row
        row_idx = row + 1
        while row_idx < ROWS:
            if self._board[row_idx][col]:
                new_points = new_points + 1
                row_idx = row_idx + 1
                were_adj_row = True
            else:
                break

        # Count adjacent tiles moving to the left in the row
        row_idx = row - 1
        while row_idx > -1:
            if self._board[row_idx][col]:
                new_points = new_points + 1
                row_idx = row_idx - 1
                were_adj_row = True
            else:
                break

        # Count adjacent tiles moving down in the column
        col_idx = col + 1
        while col_idx < COLS:
            if self._board[row][col_idx]:
                new_points = new_points + 1
                col_idx = col_idx + 1
                were_adj_col = True
            else:
                break

        # Count adjacent tiles moving up in the column
        col_idx = col - 1
        while col_idx > -1:
            if self._board[row][col_idx]:
                new_points = new_points + 1
                col_idx = col_idx - 1
                were_adj_col = True
            else:
                break

        # If there are adjacent tiles in both the row and the col the new tile is counted twice
        if were_adj_row and were_adj_col:
            new_points = new_points + 1

        self._score = self._score + new_points
        return new_points

    def calculate_bonus_points(self):
        bonus_points = 0

        # If all elements are true, the row is full
        bonus_points = bonus_points + \
            (list(map(all, self._board)).count(True) * FULL_ROW_BONUS_MULTIPLIER)

        # Likewise for columns, but need to rotate the board
        bonus_points = bonus_points + \
            (list(map(all, rotate(deepcopy(self._board)))).count(True)
             * FULL_COL_BONUS_MUTLIPLIER)

        # Shift the rows so the same color tiles are all in the same column
        shifted_board = []
        for i in range(ROWS):
            shifted_board.append(self._board[i][i:] +
                                 self._board[i][:i])

        # Rotate the shifted board so we can check columnwise
        bonus_points = bonus_points + \
            (list(map(all, rotate(shifted_board))).count(True)) * \
            ALL_TILES_FOR_COLOR_BONUS_MULTIPLIER

        return bonus_points
