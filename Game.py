import random
import constant
import time
from Player import Player
from Trick import Trick
from Deck import Deck

automated = False
delay = True

class Game:
	# Set up a game object
	def __init__(self, playerName):
		self.roundNum = 0
		self.trickNum = 0
		self.currentTrick = Trick()
		self.trickWinner = None
		self.heartsBroken = False
		self.playerName = playerName
		self.players = [Player("Cole", True), Player("Alyssa", True), Player("Jayasri", True), Player(playerName, automated)]
		self.setGame()

	# initialize a game
	def setGame(self):
		self.roundNum += 1
		self.trickNum = 1
		self.deck = Deck()
		self.deck.shuffle()
		self.heartsBroken = False
		self.currentTrick = Trick()
		for player in self.players:
			player.reset()

		# deal the cards
		i = 0
		while(self.deck.size() > 0):
			card = self.deck.draw()
			if card.suit == constant.SUIT_TO_NUM['clubs'] and card.value == constant.CARDVAL_TO_NUM['2']:
				self.trickWinner = i % len(self.players)
			self.players[i % len(self.players)].acceptCard(card)
			i += 1

	# Play a trick, starting with player at index starter
	def playTrick(self, starter):
		playersPlayed = 0
		while playersPlayed < constant.NUM_PLAYERS:
			currPlayer = self.players[starter]

			while True:
				nextCard = currPlayer.chooseCard()
				if self.cardIsLegal(currPlayer, nextCard, playersPlayed):
					break
				if currPlayer.name == self.playerName and not automated:
					print("Seems like you can't play that card, according to the rules. Choose another one!")

			if not self.heartsBroken and (nextCard.suit == constant.SUIT_TO_NUM['hearts'] or (nextCard.suit == constant.SUIT_TO_NUM['spades'] and nextCard.value == constant.CARDVAL_TO_NUM['q'])):
				self.heartsBroken = True

			self.currentTrick.add(currPlayer.playCard(nextCard), starter)
			print(currPlayer.getName(), "played", str(nextCard.value).upper(), "of", constant.EXPAND_SHORT[str(nextCard.suit)])
			print("The trick is now: ")
			print(self.currentTrick)
			playersPlayed += 1
			starter = (starter + 1) % constant.NUM_PLAYERS

			# optional delay to make game easier to follow in terminal
			if delay and self.players[starter].name != self.playerName: 
				time.sleep(2)

		self.trickWinner = self.currentTrick.winner()
		winningPlayer = self.players[self.trickWinner]
		self.players[self.trickWinner].acceptTrick(self.currentTrick)

		print(winningPlayer.getName(), "won the trick")
		
		# optional delay to make game easier to follow in terminal
		if delay: time.sleep(2)

		self.currentTrick = Trick()
		self.trickNum += 1

	# determines whether a given card can be played at the current state
	def cardIsLegal(self, player, card, playersPlayed):
		# First trick of round rules
		if self.trickNum == 1:
			if playersPlayed == 0:
				if card.suit != constant.SUIT_TO_NUM['clubs'] or card.value != constant.CARDVAL_TO_NUM['2']: # first card must be 2 of clubs
					return False
			elif card.suit == constant.SUIT_TO_NUM['hearts'] or (card.suit == constant.SUIT_TO_NUM['spades'] and card.value == constant.CARDVAL_TO_NUM['q']): # can't break hearts on first trick
				return False

		# you can never open a trick with a hearts unless hearts has been broken or if you have nothing but point cards
		if playersPlayed == 0 and not self.heartsBroken and (card.suit == constant.SUIT_TO_NUM['hearts'] or (card.suit == constant.SUIT_TO_NUM['spades'] and card.value == constant.CARDVAL_TO_NUM['q'])):
			if player.has(constant.SUIT_TO_NUM['clubs']) or player.has(constant.SUIT_TO_NUM['diamonds']):
				return False

			playerSpades = player.cardsOfSuit('spades')
			if len(playerSpades) == 1 and playerSpades[0].value == constant.CARDVAL_TO_NUM['q']:
				return True

			playerHearts = player.cardsOfSuit('hearts')
			if len(playerHearts) == player.hand.size():
				return True

			return False

		# If you have a card of the opening suit of a trick, you must play it
		if playersPlayed > 0:
			firstCardSuit = self.currentTrick.listFormat()[0][0].suit
			if card.suit != firstCardSuit and player.has(firstCardSuit):
				return False

		return True

	# Determines game winner and returns the player's name
	def getWinner(self):
		minPlayer = self.players[0]
		minScore = minPlayer.getScore()
		for player in self.players:
			currScore = player.getScore()
			if currScore < minScore:
				minPlayer = player
				minScore = currScore
		return minPlayer


	# updates the player's scores based on the tricks won
	def updateScores(self):
		moonShot = False
		for player in self.players:
			playerScore, shotMoon = player.calculateCumulativeScore()
			if shotMoon:
				moonShot = True
				print(player.getName(), "shot the moon!")
				for otherPlayer in self.players:
					if otherPlayer != player:
						otherPlayer.setScore(otherPlayer.getScore() + 26)
				return	
		
		if not moonShot:
			for player in self.players:
				playerScore, _ = player.calculateCumulativeScore()
				player.setScore(playerScore)	


	# game is active (a player has not reached score of MAX_SCORE yet)
	def active(self):
		for player in self.players:
			if player.getScore() >= constant.MAX_SCORE:
				return False
		return True

def main():
	game = Game(input('What is your name? '))

	while True:
		print("\nRound #", game.roundNum, "------------------------------------------------------------------------------\n")
		while game.trickNum <= constant.HAND_SIZE:
			print("\nTrick ", game.trickNum, ":")
			game.playTrick(game.trickWinner)
		game.updateScores()

		print('\nCURRENT SCORES:')
		[print(player.getName() + " has " + str(player.getScore()) + " points") for player in game.players]

		if not game.active():
			break
		game.setGame()
	print("\n" + game.getWinner().getName(), "wins!\n")


if __name__ == '__main__':
	main()