def move_to_square(player_state, square):
  return player_state | (1 << square)


def is_player_on_square(player_state, square):
  return ( player_state & (1 << square) ) != 0


class Board:  
  def __init__(self):
    self.player_states = [0, 0]
    self.empty_squares = [i for i in range(64)]

  def print(self):
    print('-- board --')    
    board_str = ''
    for square in range(64):
      if is_player_on_square(self.player_states[0], square):
        board_str = board_str + '0 '
      elif is_player_on_square(self.player_states[1], square):
        board_str = board_str + '1 '
      else:
        board_str = board_str + '- '

      if ((square+1) % 4) == 0:
        print(board_str)
        board_str = ''
      if ((square+1) % 16) == 0:
        print()

    print('player 0', self.player_states[0])
    print('player 1', self.player_states[1])
    print('empty_squares', self.empty_squares)

