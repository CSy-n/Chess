from Piece import Piece
import math

class Cell:
    "A Cell is a space on the Board which may hold a Piece"
    def __init__(self, piece):
        self.piece = piece


class Board:
  HEIGHT = 8
  WIDTH  = 8
  
#   INITIAL_BOARD ="\
# r n b k q b n r \
# p p p p p p p p \
# _ _ _ _ _ _ _ _ \
# _ _ _ _ _ _ _ _ \
# _ _ _ _ _ _ _ _ \
# _ _ _ _ _ _ _ _ \
# P P P P P P P P \
# R N B Q K B N R"

  INITIAL_BOARD ="\
r n b _ q b n r \
p p p _ p p p p \
_ _ _ _ _ _ _ _ \
_ _ _ k _ _ _ _ \
_ _ _ p _ _ _ _ \
_ _ _ _ _ _ P _ \
P P P P P P B P \
R N B Q K _ N R"

  

  def __init__(self):
    self.board = Board.init_board()
    self.board_cell_height = Board.HEIGHT
    self.board_cell_width = Board.WIDTH
    
  def init_board():
    board = []
    position = 0
    
    # For each Letter in the Text:
    #  Create a corresponding Piece on the board.
    
    for letter in Board.INITIAL_BOARD:
      piece = Piece.create_piece_from_sym(letter)
      if piece is not None:
        board.append(piece)
        piece.position = (position % Board.WIDTH, math.floor(position / Board.WIDTH))
        position += 1
    return board    
    
  def __repr__(self):
    "Return a Representation of a Board"
    chess_board = self.board
    iteration = 0
    interim = []
    for piece in chess_board:
      if iteration != 0 and iteration % Board.WIDTH == 0:
        interim.append('\n')
      interim.append(piece)

      iteration += 1    
    
    return ''.join(str(e) for e in interim)

  def __getitem__(self, value):
    "Return value of *index* (slice) notation"
    return self.board[value]


  """Property Accesses"""
  def set_piece(self, piece, position):
    "Sets a piece on the board (0 Indexed)"
    piece.position = position
    self.board[position] = piece

  def set_piece_2d(self, piece, pos_coordinate):
      "Sets a piece via a 2d coordinate"
      x, y = pos_coordinate
      piece.position = pos_coordinate
      self.board[int(x + y * Board.WIDTH)] = piece

      

  def get_piece(self, x, y):
      return self.get_piece_2d( (x, y))

  def get_piece_2d(self, coordinate):
      x, y = coordinate
      return self.board[int(x + y * Board.WIDTH)]

  def get_piece_as_1d(self, position):
      "Returns the `pieces' position as 1d"
      return self.board[position]
      
  """----------------------------------------"""

  """ Common Logic """

  def transpose_piece(self, the_piece, other_piece):
      "Swap one piece from one spot to the other"
      # Store Temporary Copy of Position
      interim = the_piece.position
      # Swap Piece
      self.set_piece_2d(the_piece, other_piece.position)
      self.set_piece_2d(other_piece, interim)
      #print(self.board[the_piece_position_1d])

  def remove_piece(self, piece):
      "Removes a Piece appropiately; replacing it with an EmptyPiece"
      empty_piece = EmptyPiece(piece.side, piece.position)
      self.set_piece_2d(empty_piece, piece.position)

  def check_diagonal_collision(self, start_pos, end_pos):

      pieces = self.find_pieces_diagonal(start_pos, end_pos)
      pieces = trim_list(pieces)
      collisions = []
      if len(pieces) == 0:
          return []

      for piece in pieces:

          if piece != Piece.EMPTY:
              collisions.append(piece)
      return collisions

  def find_pieces_diagonal(self, start_pos, end_pos):
    "Assumes start_pos and end_pos are diagonally apart"
    sx, sy = start_pos
    ax, ay = end_pos
    
    dx = (sx - ax)
    dy = (sy - ay)
    
    pieces = []
    
    if dx == 0 and dy == 0 or abs(dx) != abs(dy):
        return []
    
    # Means that it is diagonal in a direction: NW, NE, SW, SE
    for index in range(abs(dx) + 1):
        print(dx, dy, index)
        if dx < 0:
            if dy < 0:
                piece = self.get_piece(sx + index, sy + index)
            else:
                piece = self.get_piece(sx + index, sy - index)
                
        if dx > 0:
            if dy < 0:
                piece = self.get_piece(sx - index, sy + index)
            else:
                piece = self.get_piece(sx - index, sy - index)
                        
        pieces.append(piece)
                        
    return pieces


        

  def find_pieces_orthogonal(self, start_pos, end_pos):
    "Assumes start_pos and end_pos are orthogonal"
    sx, sy = start_pos
    ax, ay = end_pos
    dx = (sx - ax)
    dy = (sy - ay)
      
    pieces = []

    # if dx == 0 or dy == 0:
        

    # if not (dx != 0 and dy != 0):
    # if True:
        # Implies an orthogonal position

    # If both dx and dy are not zero; return []

    if dx != 0 and dy != 0 or dx == 0 and dy == 0:
        return []

    for index in range(abs(dx) + abs(dy) + 1):
        # For each of the orthogonal cells'
        if dx == 0:
            if dy < 0:
                pieces.append(self.get_piece(sx, sy + index))
            else:
                pieces.append(self.get_piece(sx, sy - index))
                
        elif dy == 0:
            if dx < 0:
                pieces.append(self.get_piece(sx - index, sy))
            else:
                pieces.append(self.get_piece(sx + index, sy))
                    
        
    return pieces
    
  def occupied(self, position):
    "Checks if the cell is occupied with a Piece (0 Indexed)"

    if self.board[position].piece is not Piece.EMPTY:
        return True
    return False 



  def display_board(self, invert_board=False):
    chess_board = self.board
    iteration = 0
    row = 1
    ranks = 'ABCDEGHI'
    
    if invert_board:
      chess_board = reversed(chess_board())
    
    for piece in chess_board:
      if iteration != 0 and iteration % Board.WIDTH == 0:
        print(f' {row}')
        row += 1
      print(piece, end=' ')

      iteration += 1
      
    print(f' {row}')  
    print()
    
    for rank in ranks: 
      print(rank, end=' ')
    

def translate_2d_to_1d(position):
    "Translates 2D Positional Coordinate into 1D Position"
    x, y = position
    return x + y * Board.WIDTH


def trim_list(elements):
    "Removes the ends of pieces; Assumes atleast two elements."
    return elements[1:-1]
