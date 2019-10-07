# List of all constants
CARDS_IN_DECK = 52
NUM_SUITS = 4
MIN_CARD_VALUE = 2
MAX_CARD_VALUE = 15
NUM_PLAYERS = 4
HAND_SIZE = 13
MAX_SCORE = 100
CARD_FORMAT = r'^([2-9jqka]|10)\sof\s(clubs|c|diamonds|d|hearts|h|spades|s)$'
SUIT_TO_NUM = {'clubs': 0, 'c': 0, 'diamonds': 1, 'd': 1, 'hearts': 2, 'h': 2, 'spades': 3, 's': 3}
CARDVAL_TO_NUM = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 11, 'q': 12, 'k': 13, 'a': 14}
EXPAND_SHORT = {'c': 'Clubs', 'd': 'Diamonds', 'h': 'Hearts', 's': 'Spades'}