import constant

from collections import deque
from Card import Card
from Card import ascii_version_of_card

class Trick:
	# init Trick. Leftmost card is the bottom card played.
	# Trick entry contains tuple of card played and who played it.
	def __init__(self):
		self.trick = deque([])

	# Play a card into the trick if card assuming it was legal.
	def add(self, card, player):
		self.trick.append((card, player))

	# Size of the trick
	def size(self):
		return len(self.trick)

	# Return a trick as a list
	def listFormat(self):
		return list(self.trick)

	# Returns the winner of the trick
	def winner(self):
		if self.size() < constant.NUM_PLAYERS:
			return None
		firstItem = self.trick[0]
		maxItem = self.trick[0]
		for currItem in self.trick:
			if currItem[0] > maxItem[0] and currItem[0].suit == firstItem[0].suit:
				maxItem = currItem
		return maxItem[1]

	def __str__(self):
		# return str([str(item[0]) for item in self.listFormat()])
		return ascii_version_of_card(*self.listFormat())
