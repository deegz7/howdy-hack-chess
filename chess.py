import pygame

pygame.init()
'''
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

        # Initialize pawns
        for i in range(8):
            game[1][i] = Pawn("w")
            game[6][i] = Pawn("b")


class Pawn():
    def __init__(self, arg):
        self.color = arg[1]
        self.piece = self.create_pawn()

    def create_pawn():

    def move():
        # First move can be 2 forward

        # Moves 1 step forward

        # Attack left

        # Attack right

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
'''

# Images
class Board(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
#Img = pygame.image.load('.png')
#Img = pygame.image.load('.png')
#Img = pygame.image.load('.png')
#Img = pygame.image.load('.png')
#Img = pygame.image.load('.png')

# value defs



# *********************************************************************
# Start the code

# Create display board
board = Board('chess_board.png', [0,0])
display_width = 1000
display_height = 1000
chessDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Get It Off Your Chess')
chessDisplay.fill([255,255,255])
chessDisplay.blit(board.image, board.rect)

# Clock
clock = pygame.time.Clock()

# Define color schemes
black = (0,0,0)
white = (255,255,255)
maroon = (80,0,0)



checkMate = False
while not checkMate:
    for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            # They closed it
        print(event)

    pygame.display.update()

    clock.tick(30)

pygame.quit()

quit()
