# from typing import Tuple


class Board:
    def __init__(self):
        self.__board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.__player = {"X": 2, "O": 3}
        self.__count = 0

    def print_board(self):
        symbols = {0: " ", 2: "X", 3: "O"}

        def print_row(board_row):
            row = "|".join([symbols[i] for i in board_row])
            print(row)

        return [print_row(row) for row in self.__board]

    def get_board(self):
        return self.__board
    
    def get_count(self):
        return self.__count

    def _check_win(self, player: int, row: int, col: int) -> bool:
        rows, cols, diags, ndiags = 0, 0, 0, 0
        win = False

        for i in range(3):
            if self.__board[row][i] == player:
                rows += 1
            if self.__board[i][col] == player:
                cols += 1
            if self.__board[i][i] == player:
                diags += 1
            if self.__board[i][1 - i + 1] == player:
                ndiags += 1
        
        if rows == 3 or cols == 3 or diags == 3 or ndiags == 3:
            win = True

        print(f"rows: {rows}, cols: {cols}, diags: {diags}, ndiags: {ndiags}, winner: {win}")

        return win

    def update_board(self, player: str, move: int) -> bool:
        assert player in ("X", "O"), "only 1: X and 2: O"

        row, col = (move - 1) // 3, (move - 1) % 3

        if self.__board[row][col] == 0:
            self.__board[row][col] = self.__player[player]

            self.__count += 1
        else:
            print("Invalid move! Not the blank spot.")

        win = self._check_win(self.__player[player], row, col)

        # TODO: move to game class
        if self.__count == 9 and not win:
            print("Tie!")
        elif win:
            print(f"Player {player} win!")


if __name__ == "__main__":
    new_board = Board()

    print("New board!")
    new_board.print_board()

    print("Player X")
    new_board.update_board(player="X", move=1)
    new_board.print_board()

    new_board.update_board(player="X", move=2)
    new_board.print_board()

    new_board.update_board(player="X", move=3)
    new_board.print_board()

    print("Player O")
    new_board.update_board(player="O", move=1)
    new_board.print_board()

    new_board.update_board(player="O", move=4)
    new_board.print_board()
    
    new_board.update_board(player="O", move=7)
    new_board.print_board()
