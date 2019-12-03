from random import randint

from board import new_board, update_board, check_win, check_tie
from ai_player import ai_move_random


class Game:
    def __init__(self, n=3):
        self.board = new_board(n=n)
        self.game_states = {-1: "Player X win!", 0: "Tie!", 1: "Player O win!"}

    def _game_turn(self, board, player: int, move: int):
        new_board = None

        while new_board is None:
            new_board = update_board(board, player, move)

        win = check_win(new_board, player, move)
        tie = check_tie(new_board)

        if win:
            return self.game_states[win]
        elif tie:
            return self.game_states[0]
        else:
            return new_board

    # TODO: who goes first, main game loop, ending, game state is weird now





# def game_turn(board: Board, player: str, move: int):
#     game_win = board.update_board(player=player, move=move)

#     if game_win:
#         print(f"Player {player} win!")
#         return 1
#     elif check_tie(board.get_board()):
#         print("Tie!")
#         return 0
#     else:
#         return game_win

# def start_game():
#     board = Board()

#     player = input("Choose side (O or X): ")
#     print("-"*18)
#     bot_player = "O" if player == "X" else "X"

#     while True:
#         # Player move
#         game_win = None

#         # if move is not valid
#         while game_win is None:
#             player_move = int(input("YOUR MOVE (1 to 9): "))
            
#             game_win = game_turn(board, player, player_move - 1)

#         board.print_board()
 
#         # BOT move
#         bot_move = ai_move_random(board.get_board())

#         print("-"*18)
#         print(f"BOT MOVE: {bot_move}")
#         game_win = game_turn(board, bot_player, bot_move)
#         board.print_board()



if __name__ == "__main__":
    pass 