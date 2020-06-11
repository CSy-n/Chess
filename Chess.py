
from Board import Board
from Player import Player
from Piece import Piece
class Chess:
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

  
  def play(self):
      input("Would you like to play a game of Chess [Y/n]: ")






