
from pprint import pprint

class SudokuValueError(BaseException):
    pass

class SudokuBlockError(BaseException):
    pass

class SudokuPuzzle(object):
    """The basic infrastructure for a puzzle. A puzzle is

    Notes:
        A puzzle is a 9x9 cube. rows(A-I) cols(1-9)

        A1 A2 A3| A4 A5 A6| A7 A8 A9
        B1 B2 B3| B4 B5 B6| B7 B8 B9
        C1 C2 C3| C4 C5 C6| C7 C8 C9
        --------+---------+---------
        D1 D2 D3| D4 D5 D6| D7 D8 D9
        E1 E2 E3| E4 E5 E6| E7 E8 E9
        F1 F2 F3| F4 F5 F6| F7 F8 F9
        --------+---------+---------
        G1 G2 G3| G4 G5 G6| G7 G8 G9
        H1 H2 H3| H4 H5 H6| H7 H8 H9
        I1 I2 I3| I4 I5 I6| I7 I8 I9

        All get methods return values starting the top left and either read
        from left to right or top to bottom or a combination of both.

    """
    def __init__(self):
        self.values = [[0 for _ in range(9)] for _ in range(9)]
        self.valid = set([_ for _ in range(1, 10)])

    def set_value(self, row, col, value):
        """Set the value for a position."""
        self.values[row][col] = value

    def get_value(self, row, col):
        """Get the value at the postion."""
        return self.values[row][col]

    def get_col(self, col):
        """Returns the values for the column."""
        return [self.values[row][col] for row in range(9)]

    def get_row(self, row):
        """Returns the values for the column."""
        return self.values[row]

    def get_block(self, block_num):
        """Returns the values in a given block.
        The top left is 0 and the bottom right is 8.
        """
        if block_num < 0 or block_num > 9:
            raise SudokuBlockError("Not a valid block must be between 0 & 8.")

        if 0 <= block_num <= 2:
            row_start = 0
        elif 3 <= block_num <= 5:
            row_start = 3
        else:
            row_start = 6
        if block_num in [0, 3, 6]:
            col_start = 0
        elif block_num in [1, 4, 7]:
            col_start = 3
        else:
            col_start = 6
        to_return = []
        for row in range(row_start, row_start + 3):
            for col in range(col_start , col_start +3):
                to_return.append(self.get_value(row, col))
        return to_return

    def check_row(self, row):
        """Checks to see if the row is valid."""
        return len(set(self.get_row(row)).intersection(self.valid)) == 9

    def check_col(self, col):
        """Check to see if the col is valid."""
        return len(set(self.get_col(col)).intersection(self.valid)) == 9

    def check_block(self, block_num):
        """Check to see if the block is valid."""
        return len(set(self.get_block(block_num)).intersection(self.valid)) == 9

    def check_puzzle(self):
        """Checks to see if the puzzle is valid."""
        rows = [self.check_row(row) for row in range(9)]
        cols = [self.check_col(col) for col in range(9)]
        blocks = [self.check_block(block) for block in range(9)]
        return all(rows) and all(cols) and all(blocks)

    def read_puzzle(self, path):
        """Read the file given and set it as the puzzle."""
        with open(path) as puzzle:
            try:
                for row, line in enumerate(puzzle):
                    for col, value in enumerate(line.strip()):
                        if value in ['.', '\n']:
                            continue
                        val = int(value)
                        if val not in self.valid:
                            raise SudokuValueError(
                                "Not a valid Sudoku value: {}".format(val))
                        self.set_value(row, col, val)
            except SudokuValueError as e:
                print(e, "invalid input")
