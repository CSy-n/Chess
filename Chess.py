
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

    # If the current side is the same as the selected Player
    # (Check if you are moving your own piece)
    if selected_piece.side != self.turn:
      return False

    
    # If the King is the player is under attack (1)
    # The attacker must be killed, or
    # The attacker must be blocked, or
    # The attack must be evaded, otherwise
    # It's WIN


    # (1) - King under Attack
    # So essentially if you're under attack from a piece
    # Whether that's from a distance;
    # Iterate through each of opponents pieces and

    if self.game_check:
      pass
      
    

    # Validate the essential pieces' move
    result = selected_piece.validate_move(selected_cell, action_cell, self.board)

    # Is the King under Attack?
    # if self.board.check_is_check()

    return result

    

  def check_is_attacked(piece):
    "Check if the piece is being attacked, and which piece is attacking"
    position = piece.position
    side = piece.side
    enemy_side = Player.get_enemy(side)

    enemy_pieces = self.board.find_pieces(enemy_side)

    # Now the hard part;
    # assessing each piece, to see whether it is attacking
    # A given piece...
    for epiece in enemy_pieces:
      if piece.can_attack_piece(epiece, piece):
        return True
    return False


  def can_attack_piece(attacking_piece, defending_piece):
    "Check if a piece is being attacked by another piece"
    return attacking_piece.can_attack_piece(defending_piece)
    





  def play(self):
      input("Would you like to play a game of Chess [Y/n]: ")






