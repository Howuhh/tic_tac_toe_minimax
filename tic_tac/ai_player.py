import copy

from random import randint
from board import possible_moves


def ai_move_random(board):
    moves = possible_moves(board)
    move = randint(0, len(moves) - 1)

    return moves[move]


def minimax_move(board, player, move):
    pass