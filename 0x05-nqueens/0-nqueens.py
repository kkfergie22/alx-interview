#!/usr/bin/python3
""""N Queens solution"""
import sys

"""Solves the N queens problem"""
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)

# Helper function to check if a given position is safe for a queen


def is_safe(board, row, col):
    # Check the row
    for i in range(N):
        if board[row][i] == '1':
            return False
    # Check the column
    for i in range(N):
        if board[i][col] == '1':
            return False
    # Check the diagonals
    for i in range(N):
        if row+i < N and col+i < N and board[row+i][col+i] == '1':
            return False
        if row-i >= 0 and col-i >= 0 and board[row-i][col-i] == '1':
            return False
        if row+i < N and col-i >= 0 and board[row+i][col-i] == '1':
            return False
        if row-i >= 0 and col+i < N and board[row-i][col+i] == '1':
            return False
    # If we've made it here, the position is safe
    return True

# Recursive function to place queens on the board


def place_queens(board, row):
    # Base case: we've placed all the queens
    if row == N:
        # Create a list of the (row, col) positions of the queens
        positions = [[r, c]
                     for r in range(N) for c in range(N) if board[r][c] == '1']
        # Print the solution
        print(positions)
        return
    # Recursive case: try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = '1'
            place_queens(board, row+1)
            board[row][col] = '0'


# Initialize the board
board = [['0' for _ in range(N)] for _ in range(N)]

# Place the queens and print the solutions
place_queens(board, 0)
