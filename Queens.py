# N-Queens Problem using Backtracking and Branch & Bound

N = 5

# Function to print solution
def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()

# Backtracking function
def solve_nqueens(board, row, cols, diag1, diag2):
    if row == N:
        print("Solution Found:")
        print_solution(board)
        return True

    for col in range(N):

        # Check if queen can be placed
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            continue

        # Place queen
        board[row][col] = 1
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

        # Recur for next row
        solve_nqueens(board, row + 1, cols, diag1, diag2)

        # Backtrack
        board[row][col] = 0
        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)

# Driver code
board = [[0 for _ in range(N)] for _ in range(N)]

solve_nqueens(board, 0, set(), set(), set())