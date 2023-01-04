class Checker:
    def __init__(self, board):
        self.is_on = True
        self.line_list = []
        self.end(board)

    def end(self, board):
        self.check_diagonal_1(board)
        self.check_diagonal_2(board)
        self.check_row(board)
        self.check_column(board)

    def check_diagonal_1(self, board):

        for n in range(3):
            self.line_list.append(board[n + 1][n])
        if len(set(self.line_list)) == 1 and set(self.line_list) != {"-"}:
            print("diagonal 1")
            self.is_on = False
            self.who_won(self.line_list)
        else:
            self.line_list = []

    def check_diagonal_2(self, board):
        for line in board:
            for house in board[line]:
                if line + board[line].index(house) == 3:
                    self.line_list.append(house)
        if len(self.line_list) == 3 and len(set(self.line_list)) == 1 and set(self.line_list) != {"-"}:
            print("diagonal 2")
            self.is_on = False
            self.who_won(self.line_list)
        else:
            self.line_list = []

    def check_row(self, board):
        for line in board:
            if len(set(board[line])) == 1 and set(board[line]) != {"-"}:
                print("row")
                self.is_on = False
                self.who_won(board[line])

    def check_column(self, board):
        for n in range(3):
            for line in board:
                self.line_list.append(board[line][n])
            if len(set(self.line_list)) == 1 and set(self.line_list) != {"-"}:
                print("column")
                self.is_on = False
                self.who_won(self.line_list)
            else:
                self.line_list = []

    def who_won(self, list):
        if set(list) == {"X"}:
            print("Youn Won!!")
        elif set(list) == {"O"}:
            print("You lost")
