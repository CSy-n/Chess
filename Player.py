class Player:
  BLACK = 0
  WHITE = 1
  
  def __init__(self, side=WHITE):
    self.side = side    
    


  def get_enemy(side):
    return Player.WHITE if side == Player.BLACK else Player.BLACK
