from copy import deepcopy

from random import choice, randint
from math import inf

try:
    from .board import possible_moves, print_board, game_over, game_score
except ModuleNotFoundError:
    from board import possible_moves, check_win, print_board, check_tie, game_over, game_score


class Bot():
    def __init__(self, player: int):
        self.player = player

    def move_random(self, board):
        moves = possible_moves(board)
        move = randint(0, len(moves) - 1)

        return moves[move]

    def move_minimax(self, board, player, depth=0):
        if game_over(board):
            return game_score(board, self.player)

        moves = possible_moves(board)

        # first move
        if len(moves) == 9:
            # angles 
            move = choice([0, 2, 6, 8])
            return [0, move]

        if player == self.player:
            maxEval = [-inf, None]

            for move in moves:
                new_board = deepcopy(board)
                row, col = move // 3,  move % 3

                new_board[row][col] = player
                score = self.move_minimax(new_board, player * -1, depth+1)

                if score[0] >= maxEval[0]:
                    maxEval = score
                    maxEval[1] = move
            return maxEval
        else:
            minEval = [inf, None]

            for move in moves:
                new_board = deepcopy(board)
                row, col = move // 3,  move % 3

                new_board[row][col] = player
                score = self.move_minimax(new_board, player * -1, depth+1)

                if score[0] <= minEval[0]:
                    minEval = score
                    minEval[1] = move

            return minEval


if __name__ == "__main__":
    test_board = [
        [1, 1, 0],
        [-1, 1, 1],
        [0, -1, -1]
    ]

    print_board(test_board)
    bot = Bot(player=1)

    best_move = bot.move_minimax(test_board, bot.player)

    print("Best move: ", best_move)