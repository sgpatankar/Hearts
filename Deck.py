import constant
import random

from collections import deque
from Card import Card

class Deck: 
	# Init deck. Leftmost item is the top of the deck.
	def __init__(self):
		self.deck = deque([])
		for suit in range(constant.NUM_SUITS):
			for val in range(constant.MIN_CARD_VALUE, constant.MAX_CARD_VALUE):
				self.deck.append(Card(val, suit))

	# Draw the top card of the deck
	def draw(self):
		return self.deck.popleft()

	# Shuffle the deck
	def shuffle(self):
		random.shuffle(self.deck)

	# Return the size of the deck
	def size(self):
		return len(self.deck)
