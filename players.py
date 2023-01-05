import random


class Player:
    def __init__(self) -> None:
        self.players = self.num_players()

    def pc_play(self, board):
        pc_choice = [random.randint(1, 3), random.randint(1, 3)]
        if board[pc_choice[0]][pc_choice[1]-1] == "-":
            board[pc_choice[0]][pc_choice[1]-1] = "O"
        else:
            self.pc_play(board)

    def player_play(self, board):
        choice = input(
            "Player X: choose a line and column (ex: 11 for line 1 column 1)")
        choice_list = [int(x) for x in choice]
        if choice_list[0] > 3 or choice_list[1] > 3:
            print("WRONG INPUT, PLEASE ENTER VALID NUMBERS")
            self.player_play(board)
        elif board[choice_list[0]][choice_list[1]-1] == "-":
            board[choice_list[0]][choice_list[1]-1] = "X"
        else:
            self.player_play(board)

    def player_2_play(self, board):
        choice = input(
            "Player O: choose a line and column (ex: 11 for line 1 column 1)")
        choice_list = [int(x) for x in choice]
        if choice_list[0] > 3 or choice_list[1] > 3:
            print("WRONG INPUT, PLEASE ENTER VALID NUMBERS")
            self.player_play()
        elif board[choice_list[0]][choice_list[1]-1] == "-":
            board[choice_list[0]][choice_list[1]-1] = "O"
        else:
            self.player_play(board)

    def num_players(self):
        return int(input("Would you like to play with 1 or 2 players? (1 / 2)"))
