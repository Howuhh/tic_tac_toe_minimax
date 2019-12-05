# from typing import Tuple
# import numpy as np
from typing import List


def new_board(n=3):
    return [[0 for j in range(n)] for i in range(n)]


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


def game_score(board, player):
    if check_win(board, player):
        return [10, None]
    elif check_win(board, player * -1):
        return [-10, None]
    else:
        return [0, None]


def game_over(board):
    return check_win(board, 1) or check_win(board, -1) or check_tie(board)


def get_diag(board, d: bool=True, n=3) -> List[int]:
    if d:
        return [row[i] for i, row in enumerate(board)]
    else:
        return [row[n - 1 - i] for i, row in enumerate(board)]


def check_win(board, player: int) -> bool:
    sums = []

    # row sums
    sums.extend(list(map(sum, board)))
    # col sums
    sums.extend(list(map(sum, zip(*board))))
    # diag sums
    sums.extend(list(map(sum, [get_diag(board, d=d) for d in (True, False)])))

    if player > 0 and max(sums) == 3:
        return True
    elif player < 0 and min(sums) == -3:
        return True
    else:
        return False


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


# TODO: delet this func and rewrite game class
# def check_win(board, player: int, move: int) -> bool:
#     row, col = move // 3, move % 3
#     rows, cols, diags, ndiags = 0, 0, 0, 0
#     win = False

#     for i in range(3):
#         if board[row][i] == player:
#             rows += 1
#         if board[i][col] == player:
#             cols += 1
#         if board[i][i] == player:
#             diags += 1
#         if board[i][1 - i + 1] == player:
#             ndiags += 1
    
#     if rows == 3 or cols == 3 or diags == 3 or ndiags == 3:
#         win = player

#     return win