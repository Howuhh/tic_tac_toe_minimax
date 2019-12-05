import pyfiglet
import sys

from random import randint
from time import time
from itertools import count

try:
    from .board import new_board, update_board, check_win, check_tie, print_board, print_example
    from .ai_player import Bot
except ModuleNotFoundError:
    from board import new_board, update_board, check_win, check_tie, print_board, print_example
    from ai_player import Bot


class Game:
    def __init__(self, n=3, bot_type="random"):
        self.bot_type = bot_type

        if bot_type not in ("random", "minimax"):
            raise NameError("Only random and minimax bot available")

        self.board = new_board(n=n)
        self.it = None

        self.game_states = {-1: "Player X win!", 0: "Tie!", 1: "Player O win!"}
        self.side_value = {"O": 1, "X": -1}

        self.ascii_hello = pyfiglet.figlet_format("Tic Tac Toe Game", width=60)
        self.ascii_end = pyfiglet.figlet_format("The End", width=60)

    def _human_turn(self, board, player: int):
        player_move = int(input(f"({self.it}) YOUR MOVE (0 to 8): "))
        
        new_board = update_board(board, player, player_move)

        # invalid move check
        if new_board is None:
            while new_board is None:
                print("Invalid move! Not the blank spot.")
                player_move = int(input("YOUR MOVE (0 to 8): "))
                new_board = update_board(board, player, player_move)

        return new_board

    def _bot_turn(self, board, player: int):
        bot = Bot(player)
        
        start_time = time()
        
        if self.bot_type == "random":
            bot_move = bot.move_random(board)
        else:
            bot_move = bot.move_minimax(board, player)[1]
            
        
        end_time = round(time() - start_time, 2)
        
        print(f"({self.it}) BOT MOVE ({end_time}s): {bot_move}")
        new_board = update_board(board, bot.player, bot_move)

        return new_board

    def _game_turn(self, board, human_player: str, goes_first: int):
        player = self.side_value[human_player]
        new_board = None

        if goes_first == player:
            new_board = self._human_turn(board, player)
            print_board(new_board)
            
            if check_win(new_board, player):
                return player

            new_board = self._bot_turn(new_board, player * -1)
            print_board(new_board)

            if check_win(new_board, player * -1):
                return player * -1
        else:
            new_board = self._bot_turn(board, player * -1)
            print_board(new_board)
            
            if check_win(new_board, player * -1):
                return player * -1

            new_board = self._human_turn(new_board, player)
            print_board(new_board)

            if check_win(new_board, player):
                return player

        if check_tie(new_board):
            return 0
        
        return new_board

    def start_game(self):
        print(self.ascii_hello)
        
        print("-"*48)

        game_board = self.board.copy()
        goes_first = randint(0, 1)

        human_player = str(input("Choose side: "))

        if human_player not in ("O", "X"):
            while human_player not in ("O", "X"):
                print("Not an option! Please, choose O or X.")
                human_player = str(input("Choose side: "))

        if goes_first == 1:
            print("Human goes first!")
        else:
            print("Bot goes first!")
        print("-"*25)

        for it in count():
            self.it = it
            new_board = self._game_turn(game_board, human_player, goes_first)

            if type(new_board) != list:
                print(self.game_states[new_board])
                break

            game_board = new_board
            print("-"*25)

        print(self.ascii_end)


if __name__ == "__main__":
    game = Game(bot_type="blabla")

    game.start_game()