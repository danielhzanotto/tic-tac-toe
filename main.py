import random
from checker import Checker

board = {
    1: ["-", "-", "-"],
    2: ["-", "-", "-"],
    3: ["-", "-", "-"]
}


checker = Checker(board)


def print_board():
    for x in board:
        print(board[x])


def change_house(line, column, player):
    if player == 0:
        board[line][column - 1] = "O"
    elif player == 1:
        board[line][column - 1] = "X"


def pc_play():
    pc_choice = [random.randint(1, 3), random.randint(1, 3)]
    if board[pc_choice[0]][pc_choice[1]-1] == "-":
        board[pc_choice[0]][pc_choice[1]-1] = "O"
    else:
        pc_play()


def player_play():
    choice = input("choose a line and column (ex: 11 for line 1 column 1)")
    choice_list = [int(x) for x in choice]
    if board[choice_list[0]][choice_list[1]-1] == "-":
        board[choice_list[0]][choice_list[1]-1] = "X"
    else:
        player_play()


while checker.is_on:
    player_play()
    checker.end(board)
    if not checker.is_on:
        print_board()
        break
    pc_play()
    checker.end(board)
    print_board()
