class SudokuPuzzle:
    """
    Sudoku Puzzle class
    """

    # 81 cells on board
    BOARD = 81
    # 9 cells in row
    ROW = 9
    # 9 cells in column
    COL = 9
    # 3x3 box / square
    BOX = 3
    # The valid values in sudoku game
    VALID_VALUES = set([str(num) for num in range(1, 10)])

    def __init__(self, lines):
        """
        Constructor for the Sudoku Puzzle
        """
        self.puzzle = lines

    def __getitem__(self, item):
        """
        Subscripts enabled for the Puzzle object
        """
        return self.puzzle[item]

    def place(self, x, y, digit):
        self.puzzle[x][y] = digit

    def check_if_valid_puzzle(self):
        """
        Checks if the puzzle given to the program is valid
        Returns a message if invalid, returns true if it is valid
        """
        # Checks if the puzzle has 9 rows (9x9)
        if len(self.puzzle) != 9:
            print("Invalid Sudoku Puzzle: A puzzle must contain 9 rows.")
            return False

        # Checks row by row
        for line in self.puzzle:
            # If there are not 9 numbers in the puzzle, it is an invalid puzzle
            if len(line) != 9:
                print("Invalid Sudoku Puzzle: A puzzle must contain 9 columns.")
                return False

        # Checks if the square / box has no overlapping numbers (3x3)
        start_y = 0
        for m in range(self.BOX):
            to_row = 0
            for k in range(self.BOX):
                start_x = 0
                value_set = [False] * 10
                start_x += to_row
                for i in range(start_x, start_x + 3):
                    for j in range(start_y, start_y + 3):
                        value = int(self.puzzle[i][j])
                        if value != 0 and value_set[value]:
                            print("Invalid Sudoku Puzzle: Each value in a square of a sudoku puzzle must be all unique.")
                            return False

                        elif value != 0:
                            value_set[value] = True

                to_row += 3
            start_y += 3

        # Check for same numbers in each row (to see if invalid)
        for line in self.puzzle:
            value_set = [False] * 10
            for number in line:
                number = int(number)
                if value_set[number] and number != 0:
                    print("Invalid Sudoku Puzzle: Each value in a row of a sudoku puzzle must be all unique.")
                    return False
                elif number != 0:
                    value_set[number] = True

        # Checks if column has no overlapping numbers
        for i in range(0, 9):
            value_set = [False] * 10
            for j in range(0, 9):
                value = self.puzzle[j][i]
                if value_set[value] and value != 0:
                    print("Invalid Sudoku Puzzle: Each value in a column of a sudoku puzzle must be all unique.")
                    return False
                elif value != 0:
                    value_set[value] = True

        return True

    def check_valid_solution(self):
        """
        Checks if the solution is valid
        Every digit is unique in row, column, and square
        """
        # Check the rows of the puzzle
        for row in self.puzzle:
            if not set(row) == self.VALID_VALUES:
                return False

        return True

    def __repr__(self):
        """
        Prints out the board
        """
        board = "-------------------------\n"
        for i in range(9):
            board += "| {} {} {} | {} {} {} | {} {} {} |\n".format(*self.puzzle[i]).replace("0", " ")
            if (i + 1) % 3 == 0:
                board += "-------------------------\n"

        return board
