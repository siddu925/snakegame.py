def solve_sudoku(board):
    # Find the first empty cell (cell with 0)
    empty_cell = find_empty_cell(board)
    
    # If there are no empty cells, the puzzle is solved
    if not empty_cell:
        return True
    
    row, col = empty_cell

    # Try filling the empty cell with numbers from 1 to 9
    for num in range(1, 10):
        if is_valid_move(board, num, (row, col)):
            # If the number is valid, fill the cell
            board[row][col] = num

            # Recursively try to solve the rest of the puzzle
            if solve_sudoku(board):
                return True

            # If the current placement didn't lead to a solution, backtrack
            board[row][col] = 0

    # If no number is valid, the puzzle cannot be solved
    return False

def find_empty_cell(board):
    # Find the first empty cell in the board
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid_move(board, num, pos):
    row, col = pos

    # Check if the number is not already in the row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the number is not already in the 3x3 box
    box_row = row // 3
    box_col = col // 3
    for i in range(3):
        for j in range(3):
            if board[3 * box_row + i][3 * box_col + j] == num:
                return False

    return True

# Example Sudoku puzzle to solve
example_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(example_board):
    for row in example_board:
        print(row)
else:
    print("No solution exists.")
