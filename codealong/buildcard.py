import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True

class card():
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank + " of " + self.suit

class decks():
	
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(card(suit, rank))

	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp += '\n' + card.__str__()
		return "the deck has: "+deck_comp


	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card

class hand():
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		#the card passed in is from the deck.deal() --> card(suit,rank)
		#remember that the list of cards is actually a list of pointers to the object
		#when i pull it from the list the object still exists but it has been moved into 
		#the players hand. (there is always an object...)
		#very poorly explained. 
		self.cards.append(card)
		self.value += values[card.rank]

		#track the ace
		if card.rank == 'Ace':
			self.aces +=1


	def adjust_for_aces(self):
		#is the value over 21, and i still have an ace, then change my ace to be a 1 instead
		#of an 11
		while self.value > 21 and self.aces:
			self.value -=10
			self.aces -=1

class chips():

	def __init__(self, total=100):
		self.total = total
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

#here is will be accepting an object which will be my chips object.
#i don't know the name of it yet but it is getting an object. 
def take_bet(chips):
	while True:

		try:
			chips.bet = int(input("How many chips would you like to bet? "))
		except:
			print("sorry please provide an integer")

		else:
			if chips.total < chips.bet:
				print("sorry you don't have enough chips {}".format(chips.total))
			else:
				#if all was good, no errors I break out of the closest loop
				#and the bet has been successfully set (from the try above)
				break

def hit(deck,hand):
	single_card = deck.deal()
	hand.add_card(single_card)
	hand.adjust_for_aces()

def hit_or_stand(deck,hand):
	global playing # this is used to control an upcomming while loop

	while True:
		x = input('hit or stand? Enter h or s ')
		#if they typed out more than H like (hit, or stand) then I take the first char and lower
		#case it. 
		if x[0].lower() =='h':
			hit(deck,hand)
			break
		elif x[0].lower() == 's':
			print('Player stands, dealer\'s turn')
			playing = False
			break
		else:
			print('Sorry, didn\'t understand, H or S only!')


def player_busts(player, dealer, chips):
	print("Bust Player!")
	chips.lose_bet()


def player_wins(player, dealer, chips):
	print('Plyaer Wins!')
	chips.win_bet()

def dealer_busts(player, dealer, chips):
	print('Player Winds, dealer busted!')
	chips.win_bet()

def dealer_wins(player, dealer, chips):
	print('Dealer Wins!!')
	chips.lose_bet()

def push(player, dealer):
	print('Dealer and player tie, PUSH')

def show_some(player,dealer):
	#remember that I am passin in objects here and those objects have attributes and 
	#methods. 
	print('Dealers Hand:')
	print('one card hidden!')
	print(dealer.cards[1])
	print('\n')
	print('Players Hand:')
	for card in player.cards:
		print(card)

def show_all(player,dealer):
	'''
	this is my docstring
	'''
	print('\nDealer Hand:')
	for card in dealer.cards:
		print(card)
	print('\n')
	print('Player Hand:')
	for card in player.cards:
		print(card)



while True:

	#builsing the logic of the game here. 

	print('Welcome to BlackJack')
	deck = decks()
	#remember that the deck is a list of pointers to 52 individually created card objects.

	deck.shuffle()

	player_hand = hand()
	#deck deal pops off a single card and passes brings back the pointer to the card
	#that pointer to the card object is passed into the hand object x2
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())
	
	#this defaults to 100 but I could pass in more if I wanted
	player_chips = chips()

	take_bet(player_chips)

	show_some(player_hand, dealer_hand)

	while playing:

		hit_or_stand(deck,player_hand)


		show_some(player_hand, dealer_hand)

		if player_hand.value > 21:
			player_busts(player_hand, dealer_hand, player_chips)
			break

	if player_hand.value <=21:

		while dealer_hand.value < 17:
			hit(deck,dealer_hand)
		
		show_all(player_hand, dealer_hand)

		if dealer_hand.value > 21:
			dealer_busts(player_hand, dealer_hand, player_chips)
		elif dealer_hand.value > player_hand.value: 
			dealer_wins(player_hand, dealer_hand, player_chips)
		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand, dealer_hand, player_chips)
		else:
			push(player_hand, dealer_hand)

	print('\n Player\'s total chips are at {}'.format(player_chips.total))

	new_game = input('would you like to play another hand? y/n')
	if new_game[0].lower() == 'y':
		playing = True
		continue
	else:
		print('thank you for playing')
		break







'''
test_deck = deck()
test_deck.shuffle()
	
#test player
test_player = hand()
#deal 1 card from deck card(suit,rank) this is a card object I'm pulling
#really you are pulling the memory location to the card
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)
test_player.add_card(test_deck.deal())
print(test_player.value)
for card in test_player.cards:
	print(card.__str__())
'''

show_all	
