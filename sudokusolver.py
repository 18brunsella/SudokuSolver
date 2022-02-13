import sys
import Puzzle


def check_if_valid_placement(puzzle, num, pos):
    """
    Checks if the digit just added to the puzzle is a valid insertion
    Returns boolean, false if the placed digit was invalid, true if it was a valid placement
    Takes O(n^2) Time
    """

    # First, checks the row
    for i in range(puzzle.ROW):
        if puzzle[pos[0]][i] == num and pos[1] != i:
            return False

    # Secondly, checks the column
    for i in range(puzzle.COL):
        if puzzle[i][pos[1]] == num and pos[0] != i:
            return False

    # Lastly, checks the square
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if puzzle[i][j] == num and (i,j) != pos:
                return False

    # Otherwise, this is a valid insertion into the board
    return True


def find_empty_cell(puzzle):
    """
    Goes through the board and finds an empty cell
    Returns a tuple with the x,y of the Sudoku Board
    Takes O(n^2) time due to running through the board then the row of the board
    """
    # Goes through the rows / board to look for empty cells
    for i in range(puzzle.ROW):
        for j in range(puzzle.COL):
            if puzzle[i][j] == 0:
                return i, j

    # Returns none if there are no empty cells
    return None


def sudoku_solver(puzzle):
    """
    Recursive function that will go through the cells of the Sudoku Board
    """
    # First, find an empty cell
    empty_cell = find_empty_cell(puzzle)

    # Base case, if no empty cell is found, then it is solved
    if not empty_cell:
        return True
    else:
        row, col = empty_cell

    for i in range(1, 10):
        if check_if_valid_placement(puzzle, i, (row, col)):
            puzzle.place(row, col, i)

            if sudoku_solver(puzzle):
                return True

            puzzle.place(row, col, 0)

    return False


def main():
    """
    Takes the command line arguments and reads in txt file
    """
    if len(sys.argv) < 2:
        print("Please supply an sudoku puzzle test file to solve. sudokusolver.py *.txt ")
        sys.exit(1)

    if sys.argv[1].endswith('.txt'):
        # Read Sudoku Puzzle File
        sudokupuzzlefile = open(sys.argv[1], 'r')
        # Retrieve all the lines in the file
        lines = sudokupuzzlefile.readlines()
        puzzleLines = []
        for line in lines:
            line = line.strip()
            puzzleLines.append(list(int(i) for i in line))

        newPuzzle = Puzzle.SudokuPuzzle(puzzleLines)
        isValid = newPuzzle.check_if_valid_puzzle()

        if isValid:
            print("Puzzle is valid")
            print(newPuzzle)

            sudoku_solver(newPuzzle)

            print("Solved!")
            print(newPuzzle)
        else:
            sys.exit(1)
    else:
        print("Please supply an sudoku puzzle test file to solve.")
        sys.exit(1)


if __name__ == "__main__":
    main()
