class Board:
    def __init__(self):
        self.board = {
            1: ["-", "-", "-"],
            2: ["-", "-", "-"],
            3: ["-", "-", "-"]
        }

    def print_board(self):
        for x in self.board:
            print(
                f"{self.board[x][0]}  {self.board[x][1]}  {self.board[x][2]}")
