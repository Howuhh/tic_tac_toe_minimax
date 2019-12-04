import copy

from random import randint

from .board import possible_moves, check_win, check_tie


def ai_move_random(board):
    moves = possible_moves(board)
    move = randint(0, len(moves) - 1)

    return moves[move]


def minimax_move(board, player: int, move: int):
    pass
    # new_board = board.copy()
    # op_player = -1 if player == 1 else 1

    # # update board
    # row, col = move // 3, move % 3
    # new_board[row][col] = player

    # # check base 
    # if check_win(new_board, player, move):
    #     return 10
    # # not right!
    # elif check_win(new_board, op_player, move):
    #     return -10
    # elif check_tie(new_board):
    #     return 0

    # moves = possible_moves(new_board)

    # for move in moves:
    #     pass


    # best_move = 0

    # return moves[best_move]