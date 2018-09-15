#!/usr/bin/python

class ChessBoard:
    """docstring for ChessBoard"""
    def __init__(self):
        self.board = self.create_board()

    def create_board():
        # Create game board array
        game_board = [[for i in range(8)] for j in range(8)]

        # Fill in white pieces
        game_board[0][0] = Rook("w")
        game_board[0][1] = Knight("w")
        game_board[0][2] = Bishop("w")
        game_board[0][3] = Queen("w")
        game_board[0][4] = King("w")
        game_board[0][5] = Bishop("w")
        game_board[0][6] = Knight("w")
        game_board[0][7] = Rook("w")

        # Fill in black pieces
        game_board[7][0] = Rook("b")
        game_board[7][1] = Knight("b")
        game_board[7][2] = Bishop("b")
        game_board[7][3] = Queen("b")
        game_board[7][4] = King("b")
        game_board[7][5] = Bishop("b")
        game_board[7][6] = Knight("b")
        game_board[7][7] = Rook("b")


class Pawn():
    def __init__(self, arg):
        self.color = arg[1]
        self.piece = self.create_pawn()

    def create_pawn():

class Knight():
    def __init__(self):
        self.color = arg[1]
        self.piece = self.create_knight()
    def create_knight():

class Rook():
    def __init__(self):
        self.color = arg[1]
        self.piece = self.create_rook()
    def create_rook():

class Bishop():
    def __init__(self):
        self.color = arg[1]
        self.piece = self.create_bishop()
    def create_bishop():

class Queen():
    def __init__(self):
        self.color = arg[1]
        self.piece = self.create_queen()
    def create_queen():

class King():
    def __init__(self):
        self.color = arg[1]
        self.piece = self.create_king()
    def create_king():


class Game(object):
    """docstring for Game"""
    def __init__(self, arg):
        King.__init__(self)
        Queen.__init__(self)
        Bishop.__init__(self)
        Rook.__init__(self)
        Knight.__init__(self)
        Pawn.__init__(self)