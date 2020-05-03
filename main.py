

#import board

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
    #self.board = [Piece()] * 64
    self.board = Board.init_board()
    self.board_height = Board.HEIGHT
    self.board_width = Board.WIDTH
    
  def init_board():
    board = []
    position = 1
    
    # For each Letter in the Text:
    #  Create a corresponding Piece on the board.
    
    for letter in Board.INITIAL_BOARD:
      piece = Piece.create_piece_from_sym(letter)
      if piece is not None:
        board.append(piece)
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
    
  def set_piece(self, piece, position):
    self.board[position] = piece
     
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
    
    



class Player:
  BLACK = 0
  WHITE = 1
  
  def __init__(self, side=WHITE):
    self.side = side    
    
class Piece:
  """Pieces: {King, Queen, Rook, Knight, Bishop, Pawn}
    Each piece has a coordinate(x,y), Color:{Black,White}
  """
  
  EMPTY = 0
  KING = 1
  QUEEN = 2
  BISHOP = 3
  KNIGHT = 4
  ROOK = 5
  PAWN = 6
  
  def __init__(self, piece=EMPTY, side=Player.WHITE, position=(0,0)):
    self.piece = piece
    self.side = side
    self.position = position
    self.representation = self.create_representation()
    
    
  def __repr__(self):
    "Return a Representation of a Piece, corresponding to its Symbolic Code"
    return self.representation
  
  def create_representation(self):
    "Construct a representaiton for a piece; Uppercase for White, lowercase for black"
    piece_representation = Piece.piece_id_to_sym(self.piece)
    if self.side is Player.WHITE:
      return piece_representation.upper()
    return piece_representation
    
  def create_king(side=Player.WHITE, position=(0,0)):
    return KingPiece(side, position)
  def create_queen(side=Player.WHITE, position=(0,0)):
    return QueenPiece(side, position)
  def create_bishop(side=Player.WHITE, position=(0,0)):
    return BishopPiece(side, position)
  def create_knight(side=Player.WHITE, position=(0,0)):
    return KnightPiece(side, position)
  def create_rook(side=Player.WHITE, position=(0,0)):
    return RookPiece(side, position)
  def create_pawn(side=Player.WHITE, position=(0,0)):
    return PawnPiece(side, position)
  def create_empty(side=Player.WHITE, position=(0,0)):
    return EmptyPiece(side, position) 
    
    
      
  pieces_sym_to_id = {
      'k': KING,
      'q': QUEEN,
      'b': BISHOP,
      'n': KNIGHT,
      'r': ROOK,
      'p': PAWN,
      '_': EMPTY
    }

  pieces_id_to_sym = {
    KING: 'k',
    QUEEN: 'q',
    BISHOP: 'b',
    KNIGHT: 'n',
    ROOK: 'r',
    PAWN: 'p',
    EMPTY: '_',
  }


  #def piece_from_sym(symbol):
  #  """
  #   Creates a Piece from a symbol
  #  """
  #  piece_id = piece_sym_to_id(symbol)
  #  
  #  return Piece(piece_id)

  def create_piece_from_sym(symbol):
    piece_id = Piece.piece_sym_to_id(symbol)
    is_white = symbol.isupper()
    
    pieces = {
      Piece.KING: Piece.create_king,
      Piece.QUEEN: Piece.create_queen,
      Piece.BISHOP: Piece.create_bishop,
      Piece.KNIGHT: Piece.create_knight,
      Piece.ROOK: Piece.create_rook,
      Piece.PAWN: Piece.create_pawn,
      Piece.EMPTY: Piece.create_empty,
    }
    #deval()
    constructor = pieces.get(piece_id)

    if constructor is not None:
      if is_white:
        return constructor()
      else:
        return constructor(Player.BLACK)
    
  def piece_id_to_sym(id):
    """
      Convert an id to a Pieces' symbolic character.
      Returns Piece.EMPTY if nothing found.
    """
    return Piece.pieces_id_to_sym.get(id)
   
    
  def piece_sym_to_id(symbol):
    """ 
      Convert a symbolic-character to a Pieces' id.
      Returns Piece.EMPTY if nothing found.
    """
    return Piece.pieces_sym_to_id.get(symbol.lower())   
    
# self, piece=EMPTY, side=Player.WHITE, position=(0,0)



class KingPiece(Piece):
  def __init__(self, side=Player.WHITE, position=(0,0)):
    Piece.__init__(self, Piece.KING, side, position)

class QueenPiece(Piece):
  def __init__(self, side=Player.WHITE, position=(0,0)):
    Piece.__init__(self, Piece.QUEEN, side, position,)

class BishopPiece(Piece):
  def __init__(self, side=Player.WHITE, position=(0,0)):
    Piece.__init__(self, Piece.BISHOP, side, position)

class KnightPiece(Piece):
  def __init__(self, side=Player.WHITE, position=(0,0)):
    Piece.__init__(self, Piece.KNIGHT, side, position)

class RookPiece(Piece):
  def __init__(self, side=Player.WHITE, position=(0,0)):
    Piece.__init__(self, Piece.ROOK, side, position)

class PawnPiece(Piece):
  def __init__(self, side=Player.WHITE, position=(0,0)):
    Piece.__init__(self, Piece.PAWN, side, position)

class EmptyPiece(Piece):
  def __init__(self, side=Player.WHITE, position=(0,0)):
    Piece.__init__(self, Piece.EMPTY, side, position)


  




