import time
from  threading import Thread
from Board import Board
from Chess import Chess
import Piece
import pygame


# Constants

GRAY = (127, 127, 127)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)



# Display Size
window_size = (840, 680)
width, height = window_size

# Intitalize Pygame
pygame.init()


# Intialize Assets
black_pawn = pygame.image.load('images/black-queen.png')



# Create a Window
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption('Learning...')

background = BLACK

screen.fill(background)

# Redraw the screen
pygame.display.update()

# Used for timing within the program.
clock = pygame.time.Clock()

resources = {
    'black-pawn' : 'black-pawn.png',
    'white-pawn' : 'white-pawn.png',
    'black-king' : 'black-king.png',
    'white-king' : 'white-king.png',
    'black-queen' : 'black-queen.png',
    'white-queen' : 'white-queen.png',
    'black-bishop' : 'black-bishop.png',
    'white-bishop' : 'white-bishop.png',
    'black-knight' : 'black-knight.png',
    'white-knight' : 'white-knight.png',
    'black-rook' : 'black-rook.png',
    'white-rook' : 'white-rook.png'
}



    
def resource_name(identifier):
    return resources[identifier]

def make_resource_path(resource):
    return 'images/' + resource

def load_resource_image(path):
    return pygame.image.load(path)

#============================
# { 'black-pawn' : 'black-pawn.png'}
# { 'black-pawn' : <Surface(285x297x32 SW)>}
#
#
def load_resources():
    res = {}
    for key in resources.keys():
        path = make_resource_path(resources[key])
        res[key] = load_resource_image(path)

    return res
    
class GEntity(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

assets = load_resources()

import random
class GPiece(GEntity):

    def __init__(self, piece):
        # self.x = random.randint(0, 300)
        # self.y = random.randint(0, 300)

        asset_name = Piece.make_asset_name(piece.representation)

        image = assets[asset_name]
        position = piece.position
        ox = 50
        oy = 50

        c_width = (width - 2 * ox) / 8
        c_height = (height - 2 * oy) / 8

        self.image = pygame.transform.scale(image, (int(c_width - 30), int(c_height - 10)))

        self.set_board_position(*position)


    def update(self):
        pass

    def set_position(self, x, y):
        self.x = x
        self.y = y
        r = self.image.get_rect()
        self.rect = pygame.Rect(self.x, self.y, r.width, r.height)

    def set_board_position(self, x, y):
        "Converts (x, y) to (ColX, ColY)"
        ox = 50
        oy = 50

        c_width = (width - 2 * ox) / 8
        c_height = (height - 2 * oy) / 8
        r = self.image.get_rect()
        
        self.x = x * c_width + ( c_width / 2 - r.width / 2) + ox
        self.y = y * c_height + ( c_height / 2 - r.height / 2) + oy
        self.rect = pygame.Rect(self.x, self.y, r.width, r.height)

    def set_board_position_1d(self, position):
        "Converts 1D to 2D"
        x = position % 8
        y = math.floor(position / 8)
        self.set_board_position(x, y)
        

    def invert_x(self):
        self.x_speed -= self.x_speed * 2
    

    def invert_y(self):
        self.y_speed -= self.y_speed * 2


class Group(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)


    
    
# Board()
# Generate Random Positions
# Translate Positions into Board
# Update Board Configuration

def gameLoop(): 

    running = True
    background = BLACK


    mx, my = pygame.mouse.get_pos()

    count = 0
    ox = 50
    oy = 50
    c_width = (width - 2 * ox) / 8
    c_height = (height - 2 * oy) / 8
    
    m_active = False
    selected_cell = None
    action_cell = None
    active_time = 0
    action_time = 0

    CHESS_DARK_MAROON = (59, 39, 71)
    CHESS_LIGHT_MAROON = (100, 106, 158)

    CHESS_BROWN = (209, 139, 71)
    CHESS_WHITE = (255, 206, 158)

    DARK_CELL_COLOR = CHESS_DARK_MAROON
    LIGHT_CELL_COLOR = CHESS_LIGHT_MAROON



    game = Chess()
    board = game.board



    # For each Piece on Board:
    #  Construct a Image representation

    for index in range(0, len(board.board)):
        # Create Image for each corresponding Piece => Image

        
        piece = board[index]
        #piece.id = 0
        asset_name = Piece.make_asset_name(piece.representation)


        if asset_name is not Piece.Piece.EMPTY:
            # piece.image = GPiece(assets[asset_name], piece.position)
            piece.sprite = GPiece(piece)

        else:
            piece.sprite = Piece.Piece.EMPTY


    while running:

        mx, my = pygame.mouse.get_pos()

        # Draw a Background
        screen.fill(background)



        # Draw a Board

        for r in range(0, 8):
            for c in range(0, 8):

                if count % 2 == 0:
                    pygame.draw.rect(screen, DARK_CELL_COLOR, [ox + c_width * r, oy + c_height * c, c_width, c_height])
                else:
                    pygame.draw.rect(screen, LIGHT_CELL_COLOR, [ox + c_width * r, oy + c_height * c, c_width, c_height])
                count += 1
            count += 1


        # Draw Entites
        queen = pygame.transform.scale(black_pawn, (int(c_width - 30), int(c_height - 10)))
        outline = pygame.transform.laplacian(black_pawn)
        
        rect = queen.get_rect().move(mx, my)
        pygame.draw.rect(screen, RED, rect, 3)

        screen.blit(outline, (mx, my, 50, 50))
        screen.blit(queen, (mx, my, 50, 50))

        # Draw each Piece (GPiece)
        for piece in board:
            # print(s.x)
            if piece.sprite is not Piece.Piece.EMPTY:
                screen.blit(piece.sprite.image, piece.sprite.rect)




        # Draw on Board per GPiece
        if mx >= ox and mx <= c_width * 8 + ox and my >= oy and my <= c_height * 8 + oy:

            cx = ox+ int((mx -ox) / c_width) * c_width
            cy = oy+int((my  - oy) / c_height) * c_height
            #print(cx)
            if selected_cell and action_cell is None:
                pygame.draw.rect(screen, RED, [cx, cy, c_width, c_height], 4)
            elif selected_cell is None:
                pygame.draw.rect(screen, BLUE, [cx, cy, c_width, c_height], 4)
            
        # Draw Active Cell
        if selected_cell:
            ax, ay = selected_cell
            cx = ax * c_width + ox
            cy = ay * c_height + oy
            piece = board.get_piece_2d((ax, ay))

            pygame.draw.rect(screen, GREEN, [cx, cy, c_width, c_height], 4)
            if pygame.time.get_ticks() - active_time > 2200:
                # print("~Activated X~")
                selected_cell = None

        if action_cell:
            ax, ay = action_cell
            cx = ax * c_width + ox
            cy = ay * c_height + oy

            pygame.draw.rect(screen, RED, [cx, cy, c_width, c_height], 4)
            if pygame.time.get_ticks() - action_time > 2200:
                # print("~Activated X~")
                action_cell = None


        # If active, and action cell
        # if selected_cell and action_cell:
            

        # Update Application Logic

        if selected_cell and action_cell:
            ax, ay = selected_cell
            cx = math.floor((mx - ox) / c_width)
            cy = math.floor((my - oy) / c_height)
            the_piece = board.get_piece_2d(selected_cell)
            other_piece =  board.get_piece_2d(action_cell)


            # Apply Game Logic

            # Check the move is valid in terms of the Chess Model
            result = game.validate_move(selected_cell, action_cell)

            # IF the RESULT is True, Apply a tranpose
            if result:

                # Update in Graphical Components
                the_sprite = the_piece.sprite
                other_sprite = other_piece.sprite
                print('transposing : ', the_sprite.x)
                
                the_sprite.set_board_position(*other_piece.position)
                if other_piece.id is not Piece.Piece.EMPTY:
                    other_sprite.set_board_position(*the_piece.position)

                # Update on Board Model
                board.transpose_piece(the_piece, other_piece)

                # Switch Game player
                #game.switch_player()

            # Otherwise, nullify active and action cell.
            selected_cell = None
            action_cell = None


        
        for piece in board:
            if piece.sprite is Piece.Piece.EMPTY:
                continue
            piece.sprite.update()



        # Update Display
        pygame.display.update()

        import math
        # Handle Events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    running = False
                elif event.key == pygame.K_x:
                    pygame.mouse.set_pos(0,0)
                elif event.key == pygame.K_w:
                    DARK_CELL_COLOR = CHESS_BROWN
                    LIGHT_CELL_COLOR = CHESS_WHITE
                    background = GRAY
                elif event.key == pygame.K_e:
                    DARK_CELL_COLOR = CHESS_DARK_MAROON
                    LIGHT_CELL_COLOR = CHESS_LIGHT_MAROON
                    background = BLACK
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Click...", end='', flush=True)

                # Current Row/Col Mouse Over
                ax = math.floor((mx - ox) / c_width)
                ay = math.floor((my - oy) / c_height)


                piece = board.get_piece_2d((ax, ay))
                print(piece, piece.id, piece.position)

                # If Click within Board
                if mx >= ox and mx <= c_width * 8 + ox and my >= oy and my <= c_height * 8 + oy:

                    # If cell active, inactive
                    if selected_cell is None:
                        if piece.id != Piece.Piece.EMPTY:
                            selected_cell = (ax, ay)
                            
                            # Get Current Time
                            active_time = pygame.time.get_ticks()
                            print("active cell")

                    # Else, check to set Active Cell
                    elif action_cell is None and selected_cell != (ax, ay):
                        # Set as Action Cell
                        action_cell = (ax, ay)
                        # Get Current Time
                        action_time = active_time

                    elif selected_cell == (ax, ay):
                        selected_cell = None
                        action_cell = None

            if event.type == pygame.MOUSEBUTTONUP:
                pass
            if event.type == pygame.QUIT:
                running = False


        # Set Frame Rate
        clock.tick(60)

task = Thread(target=gameLoop)
task.start()



