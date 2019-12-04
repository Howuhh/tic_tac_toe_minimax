# from typing import Tuple
from typing import List


def new_board(n=3):
    return [[0 for j in range(n)] for i in range(n)]


def print_example() -> None:
    board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def print_row(board_row):
        row = "|".join([str(i) for i in board_row])
        print(row)

    return [print_row(row) for row in board]


def print_board(board) -> None:
    symbols = {0: " ", -1: "X", 1: "O"}

    def print_row(board_row):
        row = "|".join([symbols[i] for i in board_row])
        print(row)

    return [print_row(row) for row in board]


def update_board(board, player: int, move: int) -> List[List[int]]:
    new_board = board.copy()
    row, col = move // 3, move % 3

    if new_board[row][col] == 0:
        new_board[row][col] = player
        return new_board
    else:
        return None


# check win after move (problem for minimax -> no initial move for bot turn in recursion)
def check_win(board, player: int, move: int) -> bool:
    row, col = move // 3, move % 3
    rows, cols, diags, ndiags = 0, 0, 0, 0
    win = False

    for i in range(3):
        if board[row][i] == player:
            rows += 1
        if board[i][col] == player:
            cols += 1
        if board[i][i] == player:
            diags += 1
        if board[i][1 - i + 1] == player:
            ndiags += 1
    
    if rows == 3 or cols == 3 or diags == 3 or ndiags == 3:
        win = player

    return win
    

def check_tie(board):
    if len(possible_moves(board)) == 0:
        return True
    else:
        return False


def possible_moves(board):
    moves = []

    for i in range(9):
        if check_valid_move(board, i):
            moves.append(i)

    return moves


def check_valid_move(board, move: int) -> bool:
    row, col = move // 3, move % 3

    if board[row][col] == 0:
        return True
    else:
        return False
