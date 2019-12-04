import pyfiglet

from random import randint
from itertools import count

from .board import new_board, update_board, check_win, check_tie, print_board, print_example
from .ai_player import ai_move_random


class Game:
    def __init__(self, n=3):
        self.board = new_board(n=n)
        self.it = None

        self.game_states = {-1: "Player X win!", 0: "Tie!", 1: "Player O win!"}
        self.side_value = {"O": 1, "X": -1}

        self.ascii_hello = pyfiglet.figlet_format("Tic Tac Toe Game", width=60)
        self.ascii_end = pyfiglet.figlet_format("The End", width=60)

    def _game_turn(self, board, player: int, move: int):
        new_board = update_board(board, player, move)

        # invalid move check
        if new_board is None:
            while new_board is None:
                print("Invalid move! Not the blank spot.")
                new_move = int(input("YOUR MOVE (0 to 8): "))
                new_board = update_board(board, player, new_move)

        win = check_win(new_board, player, move)
        tie = check_tie(new_board)

        print("-"*20)
        print_board(new_board)
        print("-"*20)

        if win:
            return self.game_states[win]
        elif tie:
            return self.game_states[0]
        else:
            return new_board

    def _human_turn(self, board, player):
        player_move = int(input(f"({self.it}) YOUR MOVE (0 to 8): "))
        
        new_board = self._game_turn(board, self.side_value[player], player_move)

        # check end state
        if type(new_board) != list:
            print(new_board)
            print(self.ascii_end)
            return None

        return new_board

    def _bot_turn(self, board, player):
        bot_move = ai_move_random(board)
        print(f"({self.it}) BOT MOVE: {bot_move}")

        new_board = self._game_turn(board, self.side_value[player], bot_move)

        # check end state
        if type(new_board) != list:
            print(new_board)
            print(self.ascii_end)
            return None

        return new_board

    def start_game(self):
        # TODO: запринтить поле последний раз перед концом/первый раз перед ходом/принтить каждый ход 
        print(self.ascii_hello)
        
        print("-"*20)
        print("Board positions:")
        print_example()
        print("-"*20)

        game_board = self.board.copy()
        goes_first = randint(0, 1)

        human_player = str(input("Choose side: "))
        bot_player = "O" if human_player == "X" else "X"

        if goes_first == 1:
            print("Human goes first!")
        else:
            print("Bot goes first!")
        print("-"*20)

        for it in count():
            self.it = it
            if goes_first == 1:
                new_board = self._human_turn(game_board, human_player)

                if new_board is None:
                    break

                new_board = self._bot_turn(new_board, bot_player)

                if new_board is None:
                    break
                
                game_board = new_board
            else:
                new_board = self._bot_turn(game_board, bot_player)

                if new_board is None:
                    break

                new_board = self._human_turn(new_board, human_player)

                if new_board is None:
                    break
                
                game_board = new_board


if __name__ == "__main__":
    game = Game()

    game.start_game()