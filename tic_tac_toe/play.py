import random

from collections import namedtuple
from board import move_to_square
from board import Board

from victory import game_over
from victory import won_game


def advance_board_randomly(board, current_player):
	"""
	Choose a random location and go there.
	"""
	square_to_move_to = board.empty_squares[
		random.randint(0, len(board.empty_squares) - 1)
	]
	
	board.player_states[current_player] = move_to_square(
		board.player_states[current_player],
		square_to_move_to
	)

	board.empty_squares.remove(square_to_move_to)


def play_random_game():
	"""
	Player 0 vs. Player 1. 

	Completely random moves until somebody wins.
	"""
	current_player = random.randint(0, 1)
	board = Board()
	while not game_over(board):
		advance_board_randomly(
			board,
			current_player
		)

		current_player = 1 - current_player

	if won_game(board.player_states[0]):
		print('player 0 wins')
	elif won_game(board.player_states[1]):
		print('player 1 wins')
	else:
		print('nobody wins?')


for i in range(100):
	play_random_game()
