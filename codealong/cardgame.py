from buildcard import * 

import random

class deck():
	
	def __init__(self):
		self.deck = []
		for suit in buildcard.suits:
			for rank in buildcard.ranks:
				self.deck.append(buildcard.card(suit, rank))

	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp += '\n' + buildcard.card.__str__()
		return "the deck has: "+deck_comp


	def shuffle(self):
		random.shuffle(self.deck)

	def deal():
		single_card = self.deck.pop()
		return single_card


test_deck = deck()
print(test_deck)



