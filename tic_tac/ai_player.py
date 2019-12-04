from copy import deepcopy

from random import randint
from math import inf

try:
    from .board import possible_moves, check_win, check_tie, print_board
except ModuleNotFoundError:
    from board import possible_moves, check_win, check_tie, print_board


class Bot():
    def __init__(self, player: int):
        self.player = player
        # self.op_player = 1 if player == -1 else 1

    def move_random(self, board):
        moves = possible_moves(board)
        move = randint(0, len(moves) - 1)

        return moves[move]

    def move_minimax(self, board, player: int, move: int=None, depth=0):
        # print(depth)
        # check base
        if depth > 0:
            if check_win(board, player, move):
                if player == self.player:
                    # print("Bot win!")
                    return 10
                else:
                    # print("Human win!")
                    return -10
            elif check_tie(board):
                return 0

        moves = possible_moves(board)

        if len(moves) == 9:
            return 0

        if player == self.player:
            best_move = None
            maxScore = -inf
            
            for new_move in moves:
                new_board = deepcopy(board)

                row, col = new_move // 3, new_move % 3
                new_board[row][col] = player

                score = self.move_minimax(new_board, player * -1, new_move, depth + 1)

                if score > maxScore:
                    maxScore = score
                    best_move = new_move
            return best_move
        else:
            best_move = None
            minScore = inf
            
            for new_move in moves:
                new_board = deepcopy(board)

                row, col = new_move // 3, new_move % 3
                new_board[row][col] = player

                score = self.move_minimax(new_board, player * -1, new_move, depth + 1)
                
                if score < minScore:
                    minScore = score
                    best_move = new_move
            return best_move


if __name__ == "__main__":
    test_board = [
        [1, 1, 0],
        [-1, 0, 1],
        [0, -1, -1]
    ]

    print_board(test_board)
    bot = Bot(player=1)

    best_move = bot.move_minimax(test_board, bot.player)

    print("Best move: ", best_move)