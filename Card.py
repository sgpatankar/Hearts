import re
import constant

class Card:
	def __init__(self, value, suit):
		self.value = CardValue(value)
		self.suit = Suit(suit)

	def value(self):
		return self.value

	def suit(self):
		return self.suit

	def parseCard(cardString):
		cardRegEx = re.compile(constant.CARD_FORMAT)
		matches = cardRegEx.search(cardString)
		if matches != None:
			groups = matches.groups()
			return Card(constant.CARDVAL_TO_NUM[groups[0]], constant.SUIT_TO_NUM[groups[1]])
		return None

	def __eq__(self, other):
		return self.value == other.value and self.suit == other.suit

	def __lt__(self, other):
		return self.value < other.value or (self.value == other.value and self.suit < other.suit)

	def __gt__(self, other):
		return self.value > other.value or (self.value == other.value and self.suit > other.suit)

	def __ge__(self, other):
		return not (self < other)

	def __le__(self, other):
		return not (self > other)

	def __ne__(self, other):
		return not (self == other)

	def __str__(self):
		return ascii_version_of_card(self)

"""
Suits
0: clubs
1: diamonds
2: hearts
3: spades
"""
class Suit:
	def __init__(self, suitID):
		self.id = suitID
		self.string = ""
		suits = ["c", "d", "h", "s"]
		if suitID <= 3 and suitID >= 0:
			self.string = suits[suitID]
		else:
			print("Invalid card identifier")

	def __eq__(self, other):
		return self.id == other

	def __lt__(self, other):
		return self.id < other.id

	def __gt__(self, other):
		return self.id > other.id

	def __ne__(self, other):
		return not (self == other)

	def __ge__(self, other):
		return not (self < other)

	def __le__(self, other):
		return not (self > other)

	def __str__(self):
		return self.string

"""
CardValue represented by numbers 2-14 are 2-Ace, respectively.
"""
class CardValue:
	def __init__(self, value):
		self.value = value
		self.string = ""

		strings = ["j", "q", "k", "a"]

		if value >= 2 and value <= 10:
			self.string = str(value)
		elif value >= 11 and value <= 14:
			self.string = strings[value - 11]
		else:
			print("Invalid rank identifier")

	def __eq__(self, other):
		return self.value == other

	def __lt__(self, other):
		return self.value < other.value

	def __gt__(self, other):
		return self.value > other.value

	def __ge__(self, other):
		return not (self < other)

	def __le__(self, other):
		return not (self > other)

	def __ne__(self, other):
		return not (self == other)

	def __str__(self):
		return self.string

# Card ASCII art formatting is partially written by me; I have only made slight modifications to a preexisting piece of code.
# Credit goes to post at link: https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards
def ascii_version_of_card(*cards, return_string=True):
	"""
	Instead of a boring text version of the card we render an ASCII image of the card.
	:param cards: One or more card objects
	:param return_string: By default we return the string version of the card, but the dealer hide the 1st card and we
	keep it as a list so that the dealer can add a hidden card in front of the list
	"""
	# we will use this to prints the appropriate icons for each card
	suits_name = ['s', 'd', 'h', 'c']
	suits_symbols = ['♠', '♦', '♥', '♣']

	# create an empty list of list, each sublist is a line
	lines = [[] for i in range(9)]

	for index, card in enumerate(cards):
		if type(card) == tuple:
			rank = card[0].value
			# "King" should be "K" and "10" should still be "10"
			if str(card[0].value) == '10':  # ten is the only one who's rank is 2 char long
				space = ''  # if we write "10" on the card that line will be 1 char to long
			else:
				space = ' '  # no "10", we use a blank space to will the void
			# get the cards suit in two steps
			suit = suits_name.index(str(card[0].suit))
			suit = suits_symbols[suit]
		else:
			rank = card.value
			# "King" should be "K" and "10" should still be "10"
			if str(card.value) == '10':  # ten is the only one who's rank is 2 char long
				space = ''  # if we write "10" on the card that line will be 1 char to long
			else:
				space = ' '  # no "10", we use a blank space to will the void
			# get the cards suit in two steps
			suit = suits_name.index(str(card.suit))
			suit = suits_symbols[suit]			

		# add the individual card on a line by line basis
		lines[0].append('┌─────────┐')
		lines[1].append('│{}{}       │'.format(str(rank).upper(), space))  # use two {} one for char, one for space or char
		lines[2].append('│         │')
		lines[3].append('│         │')
		lines[4].append('│    {}    │'.format(suit))
		lines[5].append('│         │')
		lines[6].append('│         │')
		lines[7].append('│       {}{}│'.format(space, str(rank).upper()))
		lines[8].append('└─────────┘')

	result = []
	for index, line in enumerate(lines):
		result.append(''.join(lines[index]))

	# hidden cards do not use string
	if return_string:
		return '\n'.join(result)
	else:
		return result
