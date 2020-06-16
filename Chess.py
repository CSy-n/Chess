
from Board import Board
from Player import Player
from Piece import Piece


class Chess:

  WIN = 1
  LOSS = 0
  
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
      self.turn = Player.WHITE
      self.player_1 = Player(side=Player.WHITE)
      self.player_2 = Player(side=Player.BLACK)
      self.current_player = self.player_1


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
    if selected_piece.side != self.turn:
      return False


    # If the King is the player is under attack
    # The attacker must be killed, or
    # The attacker must be blocked, or
    # The attack must be evaded, otherwise
    # It's WIN
    

    result = selected_piece.validate_move(selected_cell, action_cell, self.board)



    return result

    



  def play(self):
      input("Would you like to play a game of Chess [Y/n]: ")






