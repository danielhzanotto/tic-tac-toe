from checker import Checker
from players import Player
from board import Board


checker = Checker()
players = Player()
board = Board()


def keep_playing():
    keep_p = input("Would you like to keep playing? (Y/N)")
    if keep_p == "Y":
        checker.is_on = True
        board.board = {
            1: ["-", "-", "-"],
            2: ["-", "-", "-"],
            3: ["-", "-", "-"]
        }
        players.players = players.num_players()


while checker.is_on:

    players.player_play(board.board)
    board.print_board()

    checker.end(board.board)
    if not checker.is_on:
        board.print_board()
        keep_playing()
        if not checker.is_on:
            break

    if players.players == 1:
        players.pc_play(board.board)
    elif players.players == 2:
        players.player_2_play(board.board)

    print("\n\n")

    checker.end(board.board)
    if not checker.is_on:
        board.print_board()
        keep_playing()
        if not checker.is_on:
            break

    board.print_board()
