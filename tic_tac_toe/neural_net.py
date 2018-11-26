import math
import numpy as np

import tensorflow as tf
mnist = tf.keras.datasets.mnist

# percentage of input to train vs. test
TRAIN_PERCENTAGE = 0.85

def explode_player_states(player_states):
	return [
		1 if (player_states[0] & (1 << square) != 0) else 0
		for square in range(64)
	] + [
		1 if (player_states[1] & (1 << square) != 0) else 0
		for square in range(64)
	]


def train_and_test(winner_states, loser_states):
	winner_training_set_size = math.floor(len(winner_states) * TRAIN_PERCENTAGE)
	winner_test_set_size = len(winner_states) - winner_training_set_size
	loser_training_set_size = math.floor(len(loser_states) * TRAIN_PERCENTAGE)
	loser_test_set_size = len(loser_states) - loser_training_set_size

	x_train = np.array([
		explode_player_states(winner) for winner in winner_states[:winner_training_set_size]
	] + [
		explode_player_states(loser) for loser in loser_states[:loser_training_set_size]
	])
	y_train = np.array([ 1 ] * winner_training_set_size + [ 0 ] * loser_training_set_size)

	x_test = np.array([
		explode_player_states(winner) for winner in winner_states[winner_training_set_size:]
	] + [
		explode_player_states(loser) for loser in loser_states[loser_training_set_size:]
	])
	y_test = np.array([ 1 ] * winner_test_set_size + [ 0 ] * loser_test_set_size)

	model = tf.keras.models.Sequential([
	  tf.keras.layers.Dense(16, activation=tf.nn.relu),
	  tf.keras.layers.Dense(16, activation=tf.nn.relu),
	  tf.keras.layers.Dropout(0.2),
	  tf.keras.layers.Dense(2, activation=tf.nn.relu)
	])
	model.compile(optimizer='adam',
	              loss='sparse_categorical_crossentropy',
	              metrics=['accuracy'])

	print('fitting the model')
	model.fit(x_train, y_train, epochs=5)
	print('fit the model')
	test_loss, test_acc = model.evaluate(x_test, y_test)
	print('test_loss:', test_loss)
	print('test_acc:', test_acc)
