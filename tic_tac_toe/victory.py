from functools import lru_cache
from board import is_player_on_square


def game_over(board):
  return (
    won_game(board.player_states[0]) or 
    won_game(board.player_states[1])
  )


def won_game(player_state):
  for line in get_victory_lines():
    if won_line(player_state, line):
      return True
  return False


def won_line(player_state, line):
  for square in line:
    if not is_player_on_square(player_state, square):
      return False

  return True


@lru_cache(maxsize=1)
def get_victory_lines():
  lines = []
  with open('tic_tac_toe/data/victory_lines.txt') as file:
    for line in file:
      lines.append([int(val) for val in line.split(',')])

  return lines
