
from Board import Board
from Player import Player
from Piece import Piece


class Chess:

  LOSS = 0
  WIN = 1
  PLAYING = 2
  
  """
      A game of Chess;
       - board (board status)
       - turn  ( current players' turn)
       - player_1 (player 1)
       - player_2 (player 2)
       - 

  """

  def __init__(self):
      self.board = Board()
      self.turn = Player.BLACK
      self.player_1 = Player(side=Player.WHITE)
      self.player_2 = Player(side=Player.BLACK)
      self.current_player = self.player_1
      self.game_check = False
      self.state = Chess.PLAYING


  def switch_player(self):
    "Switch to next player"
    self.turn = Player.WHITE if self.turn == Player.BLACK else Player.BLACK
    self.current_player = self.player_1 if self.turn == Player.WHITE else self.player_2


  def validate_move(self, selected_cell, action_cell):
    "Checks if the current_cell and action_cell are valid in terms of the rules of Chess"
    # Obtain selected_cell's piece aswell as active_cell
    selected_piece = self.board.get_piece_2d(selected_cell)
    active_piece   = self.board.get_piece_2d(action_cell)

    """
      Pawn (Semi Complete)
      Rook (Complete; but needs block)
      Knight (Complete)
      Bishop (Complete; but needs block)
      King   (King, Complete but missing)
      Queen  (Complete)

    Game Logic
       Switch Game Teams (Completed)
       Verify Game Team is same as current piece (Completed)
       
       En Passant - (Not implemeneted)
       
    """

    # The move is valid if:
    # - It operates on the pieces logic
    # - It 
    result = selected_piece.validate_move(selected_cell, action_cell, self.board)






    return result

  def find_side_pieces(self, side):
    "Find pieces in a corresponding side"
    pieces = []

    for piece in self.board:
      if piece.side == side:
        pieces.append(piece)
    return pieces

  def find_identity_pieces(identity):
    "Find pieces in a corresponding denomination"
    return find_pieces(identity)

  def find_pieces(self, identity, side=None):
    "Finds all pieces with a given identity"
    pieces = []

    for piece in self.board:
      if piece.id is identity and (side == None or piece.side == side):
        pieces.append(piece)
    return pieces
    

  def find_king(self, side):
    "Finds a King for a given side if available"
    return self.find_pieces(Piece.KING, side).pop()


  def find_attacker(self, piece):
    "Find pieces if they are attacking *piece*"
    position = piece.position
    side = piece.side
    enemy_side = Player.get_enemy(side)
    enemy_pieces = self.board.find_side_pieces(enemy_side)
    attackers = []
    for epiece in enemy_pieces:
      if self.can_attack_piece(epiece, piece):
        attackers.append(epiece)

    if len(attackers) == 0:
      return None

    return attackers

  
  def check_is_attacked(self, piece):
    "Check if the piece is being attacked, and which piece is attacking"
    position = piece.position
    side = piece.side
    enemy_side = Player.get_enemy(side)

    enemy_pieces = self.board.find_side_pieces(enemy_side)

    # Now the hard part;
    # assessing each piece, to see whether it is attacking
    # A given piece...
    for epiece in enemy_pieces:
      if self.can_attack_piece(epiece, piece):
        return True
    return False


  def can_attack_piece(self, attacking_piece, defending_piece):
    "Check if a piece is being attacked by another piece"
    return attacking_piece.can_attack_piece(defending_piece)
    


  def is_check(self, piece):
    "Checks if the opposing team is under check"
    enemy_side = Player.get_enemy(piece.side)
    king = self.find_king(enemy_side)
    
    if self.can_attack_piece(piece, king):
      self.game_check = True
  

  def find_king_attackers(self, side):
    return self.find_attacker(self.find_king(side))


  def resolve_check(self, attacking_piece, defending_piece):
    "Check whether the action is valid in terms of Check"
    pass
    

    
  def play(self):
      input("Would you like to play a game of Chess [Y/n]: ")






