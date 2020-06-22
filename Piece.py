from Player import Player

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
  
  def __init__(self, id=EMPTY, side=Player.WHITE, position=(0,0)):
    self.id = id
    self.side = side
    self.position = position
    self.representation = self.create_representation()

    
    
  def __repr__(self):
    "Return a Representation of a Piece, corresponding to its Symbolic Code"
    return self.representation
  
  def create_representation(self):
    "Construct a representaiton for a piece; Uppercase for White, lowercase for black"
    piece_representation = Piece.piece_id_to_sym(self.id)
    if self.side is Player.WHITE:
      return piece_representation.upper()
    return piece_representation


  def validate_move(self, selected_cell, action_cell, board, game):
    "Returns whether a movement from selected_cell to action_cell is valid"
    return True


  def is_enemy(self, other_piece):
    if self.side != other_piece.side and other_piece.id != Piece.EMPTY:
      return True
    return False

    
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

  def validate_move(self, selected_cell, action_cell, board):
    selected_piece = board.get_piece_2d(selected_cell)
    active_piece   = board.get_piece_2d(action_cell)

    sx, sy = selected_cell
    ax, ay = action_cell

    dx = abs(sx - ax)
    dy = abs(sy - ay)

    if dx == 0 and dy == 1 or dx == 1 and dy == 0 or dx == 1 and dy == 1:
      return True

  def can_attack_piece(self, defending_piece):
    defending_position = defending_piece.position

    sx, sy = self.position
    ax, ay = defending_position

    dx = (sx - ax)
    dy = (sy - ay)

    if abs(dx) == abs(dy):
      print("<:>|[]|")
      return True
    return False
    
class QueenPiece(Piece):
  def __init__(self, side=Player.WHITE, position=(0,0)):
    Piece.__init__(self, Piece.QUEEN, side, position,)

  def validate_move(self, selected_cell, action_cell, board):
    selected_piece = board.get_piece_2d(selected_cell)
    active_piece   = board.get_piece_2d(action_cell)
    # Can move omni-directionally as many as it wants.

    sx, sy = selected_cell
    ax, ay = action_cell
    dx = abs(sx - ax)
    dy = abs(sy - ay)


    # dx == 0 and dy == 1 |> mid-left or mid-right
    # dx == 1 and dy == 0 |> mid-top or mid-bot
    # dx == 1 and dy == 1 |> diagonal 1 unit


    # dx == dy (Move same amount in any direction)
    if dx == dy:
      return True

    # Move unidirectionally any unit
    if sx == ax or sy == ay:
      return True
    

    return False


    
class BishopPiece(Piece):
  def __init__(self, side=Player.WHITE, position=(0,0)):
    Piece.__init__(self, Piece.BISHOP, side, position)

  def validate_move(self, selected_cell, action_cell, board):
    selected_piece = board.get_piece_2d(selected_cell)
    active_piece   = board.get_piece_2d(action_cell)
    # Can move omni-directionally as many as it wants.

    sx, sy = selected_cell
    ax, ay = action_cell
    dx = abs(sx - ax)
    dy = abs(sy - ay)

    if dx == dy:
      return True

  def can_attack_piece(self, defending_piece):
    defending_position = defending_piece.position

    sx, sy = self.position
    ax, ay = defending_position

    dx = (sx - ax)
    dy = (sy - ay)

    if abs(dx) == abs(dy):
      print("<:>|[]|")
      return True
    return False


class KnightPiece(Piece):
  def __init__(self, side=Player.WHITE, position=(0,0)):
    Piece.__init__(self, Piece.KNIGHT, side, position)

  def validate_move(self, selected_cell, action_cell, board):
    selected_piece = board.get_piece_2d(selected_cell)
    active_piece   = board.get_piece_2d(action_cell)

    sx, sy = selected_cell
    ax, ay = action_cell

    dx = abs(sx - ax)
    dy = abs(sy - ay)

    if dx == 2  or dx == 1:
      if dx == 2 and dy == 1 or dx == 1 and dy == 2:
        return True

    #board.(selected_piece, active_piece)

    return False

class RookPiece(Piece):
  def __init__(self, side=Player.WHITE, position=(0,0)):
    Piece.__init__(self, Piece.ROOK, side, position)

  def validate_move(self, selected_cell, action_cell, board):
    selected_piece = board.get_piece_2d(selected_cell)
    active_piece   = board.get_piece_2d(action_cell)
    # Can move omni-directionally as many as it wants.
    
    sx, sy = selected_cell
    ax, ay = action_cell
    
    if sx == ax or sy == ay:
      return True
    return False

class PawnPiece(Piece):
  def __init__(self, side=Player.WHITE, position=(0,0)):
    Piece.__init__(self, Piece.PAWN, side, position)
    self.bonus_movement = True


  def validate_move(self, selected_cell, action_cell, board):
    selected_piece = board.get_piece_2d(selected_cell)
    active_piece   = board.get_piece_2d(action_cell)
    # Can move omni-directionally as many as it wants.

    sx, sy = selected_cell
    ax, ay = action_cell

    dx = abs(sx - ax)
    dy = abs(sy - ay)

    # Move forward one unit
    # Or, hasn't been moved yet

    # print(selected_cell)
    # print(action_cell)
    # print(selected_piece.side)

    if dy == 1:
      # if movement in Y direction is 1 Unit
      # Is it valid for corresponding piece type?
      if selected_piece.side == Player.WHITE and sy - ay > 0:
        if dx == 0:
          self.bonus_movement = False
          return True
        elif dx == 1 and selected_piece.is_enemy(active_piece):
          self.bonus_movement = False
          return True
      elif selected_piece.side == Player.BLACK and sy - ay < 0:
        if dx == 0:
          self.bonus_movement = False
          return True
        elif dx == 1 and selected_piece.is_enemy(active_piece):
          self.bonus_movement = False
          return True
    elif dy == 2 and dx == 0 and self.bonus_movement:
      self.bonus_movement = False
      return True
    # If there is an enemy diagonally
    # If WHITE then downwards...
    #if selected_piece.side == Player.WHITE and dx > 0
    return False

  def can_attack_piece(self, defending_piece):
    defending_position = defending_piece.position

    sx, sy = self.position
    ax, ay = defending_position

    dx = abs(sx - ax)
    dy = abs(sy - ay)

    # if dy == 1: 
    #   if dx == 1 and piece.side == Player.WHITE and sy - ay > 0:
        
    #   elif dx == 1 and piece.side == Player.WHITE and sy - ay < 0:

    # Check if selfs' attacking has the ability of the defending position

    if dx == 1 and dy == 1:
      print("can_attack_piece=> in dx==1 and dy == 1:")
      if self.side == Player.WHITE and sy - ay > 0 or self.side == Player.BLACK and sy - ay < 0:
        print("~><@!>@<>#<@><#@")
        # Now they must correspond to an attack!
        return True
    return False

class EmptyPiece(Piece):
  def __init__(self, side=Player.WHITE, position=(0,0)):
    Piece.__init__(self, Piece.EMPTY, side, position)


def make_asset_name(symbol):

  # Check is Empty symbol

  if Piece.piece_sym_to_id(symbol) == Piece.EMPTY:
    return Piece.EMPTY
  
  asset_name = 'white' if symbol.isupper() else 'black'
  asset_name += '-'


  pieces_sym_to_name = {
    'k': 'king',
    'q': 'queen',
    'b': 'bishop',
    'n': 'knight',
    'r': 'rook',
    'p': 'pawn',
    '_': 'empty'
  } 
  return asset_name + pieces_sym_to_name.get(symbol.lower())

