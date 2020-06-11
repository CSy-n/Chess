from Piece import Piece
import math

class Cell:
    "A Cell is a space on the Board which may hold a Piece"
    def __init__(self, piece):
        self.piece = piece


class Board:
  HEIGHT = 8
  WIDTH  = 8
  
  INITIAL_BOARD ="\
r n b k q b n r \
p p p p p p p p \
_ _ _ _ _ _ _ _ \
_ _ _ _ _ _ _ _ \
_ _ _ _ _ _ _ _ \
_ _ _ _ _ _ _ _ \
P P P P P P P P \
R N B Q K B N R" 

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

  def get_piece_2d(self, coordinate):
      x, y = coordinate
      return self.board[int(x + y * Board.WIDTH)]
   
  def get_position_as_1d(self, piece):
      "Returns the `pieces' position as 1d"
      return translate_2d_to_1d(piece.position)
      
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




  def check_diagonal_collision(start_pos, end_pos):
      "Assumes start_pos and end_pos are diagonally apart"
      pass




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
