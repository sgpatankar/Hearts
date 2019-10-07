import constant
import random
from Hand import Hand
from Card import Card
from Trick import Trick
from collections import deque

class Player:
	# Initialize a player.
	def __init__(self, name, automatic):
		self.name = name
		self.hand = Hand()
		self.tricks = deque([])
		self.score = 0
		self.automatic = automatic

	# Deal a card to a player, put it into the player's hand
	def acceptCard(self, card):
		self.hand.addCard(card)

	# Play a chosen card from the hand if it is in the hand
	def playCard(self, card):
		if card in self.hand.listFormat():
			self.hand.removeCard(card)
			return card
		return None

	# Add to player's tricks
	def acceptTrick(self, trick):
		self.tricks.append(trick)

	# Reset a player for a new round
	def reset(self):
		self.hand = Hand()
		self.tricks = deque([])

	def getScore(self):
		return self.score

	def getName(self):
		return self.name

	def setScore(self, value):
		self.score = value

	# whether a player has a certain suit in their hand
	def has(self, suit):
		for card in self.hand.listFormat():
			if card.suit == suit:
				return True
		return False

	# returns a list of cards of a given suit that are in the player's hand
	def cardsOfSuit(self, suit):
		result = []
		for card in self.hand.listFormat():
			if card.suit == constant.SUIT_TO_NUM[suit]:
				result += [card]
		return result

	# Calculates score for current round and returns whether player "shot the moon"
	def calculateCurrentRoundScore(self):
		heartCount = 0
		queenCount = 0
		for trick in self.tricks:
			for card in trick.listFormat():
				if card[0].suit == constant.SUIT_TO_NUM['hearts']:
					heartCount += 1
				if card[0].suit == constant.SUIT_TO_NUM['spades'] and card[0].value == constant.CARDVAL_TO_NUM['q']:
					queenCount += 1
		if heartCount + queenCount == 14:
			return 0, True
		return heartCount + (13 * queenCount), False

	# Calculates total game score
	def calculateCumulativeScore(self):
		currScore, shotMoon = self.calculateCurrentRoundScore()
		return self.score + currScore, shotMoon


	# Determine which card to play
	def chooseCard(self):
		if self.automatic:
			return random.sample(self.hand.listFormat(), 1)[0]
		else:
			card = None
			print("Cards in your hand: ")
			print(self.hand)
			while card is None:
				cardStr = input(self.name + ", select a card to play: ")
				card = Card.parseCard(cardStr.lower().strip())
				if card is None:
					print("That was not a valid card entry. Please enter a card in the following format: 'a of hearts', 'j of clubs', '2 of spades', etc.\n")
					continue
				if not self.hand.contains(card):
					print("You do not have access to that card! Pick a different card.\n")
					card = None
			return card
