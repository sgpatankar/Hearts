import constant

from collections import deque
from Card import Card
from Card import ascii_version_of_card

class Hand: 
	# Init hand. Leftmost item is the left of the hand (should be ordered by type).
	def __init__(self):
		self.hand = deque([])

	# Add a card to the hand
	def addCard(self, card):
		insIdx = 0
		while insIdx < self.size() and self.hand[insIdx] < card:
			insIdx += 1
		self.hand.insert(insIdx, card)

	# Remove a card from the hand
	def removeCard(self, card):
		if card in self.hand:
			self.hand.remove(card)
			return card
		return None

	# Whether the hand contains the card
	def contains(self, card):
		return card in self.hand

	# Return the size of the hand
	def size(self):
		return len(self.hand)

	# Return hand as a list
	def listFormat(self):
		return list(self.hand)

	def __str__(self):
		return ascii_version_of_card(*self.listFormat())
