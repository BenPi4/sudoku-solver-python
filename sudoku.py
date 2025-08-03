from random import randrange

FINISH_FAILURE = -1
FINISH_SUCCESS = 1
NOT_FINISH = 0

# Returns a list of valid digits for a given empty cell
# If cell is full, returns empty list; if no options possible, returns None
def options(board: list, loc: tuple) -> list:
    if board[loc[0]][loc[1]] != 0:
        return []
    possible_dig = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Row
    for dig in board[loc[0]]:
        if dig in possible_dig:
            possible_dig.remove(dig)
    # Column
    for i in range(9):
        dig = board[i][loc[1]]
        if dig in possible_dig:
            possible_dig.remove(dig)
    # Box
    box_row = (loc[0] // 3) * 3
    box_col = (loc[1] // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            dig = board[i][j]
            if dig in possible_dig:
                possible_dig.remove(dig)
    if len(possible_dig) == 0:
        return None
    return possible_dig

# Finds the cell with the fewest valid options (MRV)
def find_mrv_cell(board: list) -> tuple:
    min_options = 10
    best_cell = None
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                opts = options(board, (row, col))
                if opts is None:
                    return None
                if len(opts) < min_options:
                    min_options = len(opts)
                    best_cell = (row, col)
    return best_cell

# Solves the board using backtracking and MRV
def solve_sudoku(board: list):
    cell = find_mrv_cell(board)
    if cell is None:
        for row in board:
            for val in row:  # changed from 'cell' to 'val'
                if val == 0:
                    return False
        return True
    row, col = cell
    for num in options(board, (row, col)):
        board[row][col] = num
        if solve_sudoku(board):
            return True
        board[row][col] = 0
    return False

# Checks if board is valid (no duplicates)
def is_legit(board: list) -> bool:
    counters = [0 for _ in range(10)]
    for i in range(9):
        # Check rows
        for dig in board[i]:
            if dig != 0:
                counters[dig] += 1
        for count in counters:
            if count > 1:
                return False
        counters = [0 for _ in range(10)]
        # Check columns
        for j in range(9):
            if board[j][i] != 0:
                counters[board[j][i]] += 1
        for count in counters:
            if count > 1:
                return False
        counters = [0 for _ in range(10)]
    # Check 3x3 boxes
    square_row, square_col = 0, 0
    for t in range(9):
        for i in range(square_row, square_row + 3):
            for j in range(square_col, square_col + 3):
                if board[i][j] != 0:
                    counters[board[i][j]] += 1
        for count in counters:
            if count > 1:
                return False
        counters = [0 for _ in range(10)]
        if square_row < 6:
            square_row += 3
        else:
            square_row = 0
            square_col += 3
    return True

# Creates a board with random legal entries (not necessarily solvable)
def create_random_board(board: list) -> list:
    board.clear()
    loc_list = [(r, c) for r in range(9) for c in range(9)]
    for _ in range(9):
        board.append([0] * 9)
    n = randrange(10, 20)
    for _ in range(n):
        k = randrange(1, len(loc_list))
        r, c = loc_list[k - 1]
        loc_list.remove(loc_list[k - 1])
        finish = False
        tries = 0
        while not finish and tries < 20:  # prevent infinite loop
            dig = randrange(1, 10)
            if dig in options(board, (r, c)):
                board[r][c] = dig
                finish = True
            tries += 1
    return board

# Prints the board to the terminal
def print_board(board: list):
    print('-----------------')
    for row in board:
        print('|'.join(str(num) if num != 0 else ' ' for num in row))
        print('-----------------')

# Writes board and solution status to file
def print_board_to_file(board: list, file_name: str):
    f = open(file_name, "a")
    if not is_legit(board):
        f.write("Board is not legit\n")
    elif solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                board[i][j] = str(board[i][j])
        f.write("Here is the solved board!\n")
        f.write('-----------------\n')
        for i in range(9):
            row = '|'.join(board[i])
            f.write(row)
            f.write("\n-----------------\n")
    else:
        f.write("Board is unsolvable\n")
    f.close()

# ********************* main *************************
soduko1 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 9, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 3],
    [0, 0, 0, 8, 0, 3, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 9]
]
soduko2 = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
soduko3 = [
    [5, 1, 6, 8, 4, 9, 7, 3, 2],
    [3, 0, 7, 6, 0, 5, 0, 0, 0],
    [8, 0, 9, 7, 0, 0, 0, 6, 5],
    [1, 3, 5, 0, 6, 0, 9, 0, 7],
    [4, 7, 2, 5, 9, 1, 0, 0, 6],
    [9, 6, 8, 3, 7, 0, 0, 5, 0],
    [2, 5, 3, 1, 8, 6, 0, 7, 4],
    [6, 8, 4, 2, 0, 7, 5, 0, 0],
    [7, 9, 1, 0, 5, 0, 6, 0, 8]
]
soduko4 = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 9],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
soduko5 = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [0, 0, 0, 7, 6, 1, 4, 2, 3],
    [0, 0, 0, 8, 5, 3, 7, 9, 1],
    [0, 0, 0, 9, 2, 4, 8, 5, 6],
    [0, 0, 0, 0, 3, 7, 2, 8, 4],
    [0, 0, 0, 0, 1, 9, 6, 3, 5],
    [0, 0, 0, 0, 8, 6, 1, 7, 9]
]

f = open("solved_soduko", "w")
print_board_to_file(soduko1, "solved_soduko")
print_board_to_file(soduko2, "solved_soduko")
print_board_to_file(soduko3, "solved_soduko")
print_board_to_file(soduko4, "solved_soduko")
print_board_to_file(soduko5, "solved_soduko")
print_board_to_file(create_random_board([]), "solved_soduko")
f.close()
