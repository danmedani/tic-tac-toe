import random

from collections import namedtuple
from board import move_to_square
from board import Board

from victory import game_over
from victory import won_game

from neural_net import train_and_test

winner_states = []
loser_states = []

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

	# record all player 0 and 1's states throughout the game
	all_player_states = [[], []]

	while not game_over(board):
		advance_board_randomly(
			board,
			current_player
		)

		other_player = 1 - current_player

		all_player_states[current_player].append([
			board.player_states[current_player],
			board.player_states[other_player]
		])
		current_player = other_player

	if won_game(board.player_states[0]):
		# print('player 0 wins')
		record_results(all_player_states, 0)
	elif won_game(board.player_states[1]):
		# print('player 1 wins')
		record_results(all_player_states, 1)
	else:
		print('nobody wins?')


def record_results(all_player_states, winner):
	loser = 1 - winner
	
	for state in all_player_states[winner]:
		winner_states.append(state)

	for state in all_player_states[loser]:
		loser_states.append(state)

for i in range(1000):
	play_random_game()


train_and_test(winner_states, loser_states)
