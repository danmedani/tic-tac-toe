import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


def record_results(player_states, winner):
	loser = 1 - winner
	
	print([player_state for player_state in player_states[winner]])
	print([player_state for player_state in player_states[loser]])
