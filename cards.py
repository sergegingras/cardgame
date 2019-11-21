import os
class Cards():
	"""this is my cards class"""
	import random as rnd
	def __init__(self):
		#using ascii there are the four suits
		foursuits = ('♥','♣','♠','♦')
		#10 - Ace
		tenandface = ('J','Q','K')
		theace= ('A')
		#number cards
		numbercards = range(2,11)
		#the deck of cards
		thedeck = []
		amount = 100
		printhand = ''
		playerhand  = 0
		househand  = 0
		bet = 0
		#using this to generate the ascii hand into a list	
		for suit in foursuits:
			for face in tenandface:
				thedeck.append([f'{face}',f'{suit}',10])
			for ace in theace:
				thedeck.append([f'{ace}',f'{suit}',11])
			for number in numbercards:
				thedeck.append([f'{number}',f'{suit}',number])

		self.cards = thedeck
		self.player = []
		self.house = []
		self.printhand = printhand
		self.amount = amount
		self.foursuits = foursuits
		self.tenandface = tenandface
		self.theace = theace
		self.numbercards = numbercards
		self.betval = bet

	def __str__(self):
		return self.playerhand

		#print(type(thedeck))
	def shuffle(self):
		cards.cards = []
		for suit in cards.foursuits:
			for face in cards.tenandface:
				cards.cards.append([f'{face}',f'{suit}',10])
			for ace in cards.theace:
				cards.cards.append([f'{ace}',f'{suit}',11])
			for number in cards.numbercards:
				cards.cards.append([f'{number}',f'{suit}',number])
		cards.player =[]
		cards.house = []




	def checkhandvalue(self,hand):
		#worth = {'J':10,'Q',10,'K',10}
		#my_array=[[1,2],[1,3],[2,3]]
		#my_sum=sum(v[1] for v in my_array if v[0]==1)
		#i have put the value in the player[2]
		
		if hand == 'player':
			#does the player have an ace ?
			if sum(v[2] for v in self.player) == 21:
				return 'Blackjack'
			elif 'A' in [v[0] for v in self.player] :
				#is the player over 21 with 11 and with -10?
				if sum(v[2] for v in self.player) > 21 and sum(v[2] for v in self.player) -10 > 21:
					return 'playerbusts'
				elif sum(v[2] for v in self.player) -10 == 21 or sum(v[2] for v in self.player) == 21:
					return 21
				elif sum(v[2] for v in self.player) > 21 and sum(v[2] for v in self.player) -10 < 21:
					return sum(v[2] for v in self.player) -10
				else:
					return sum(v[2] for v in self.player)
			#no the player doesn't have an ace
			else:
				if sum(v[2] for v in self.player) == 21:
					return 21
				elif sum(v[2] for v in self.player) > 21:
					return 'playerbusts'
				else:
					return sum(v[2] for v in self.player)
		else:
			if sum(v[2] for v in self.house) == 21:
				return 'Blackjack'
			elif 'A' in [v[0] for v in self.house] :
				#is the player over 21 with 11 and with -10?
				if sum(v[2] for v in self.house) > 21 and sum(v[2] for v in self.house) -10 > 21:
					return 'dealerbusts'
				
				elif sum(v[2] for v in self.house) -10 == 21 or sum(v[2] for v in self.house) == 21:
					return 21
				elif sum(v[2] for v in self.house) > 21 and sum(v[2] for v in self.house) -10 < 21:
					return sum(v[2] for v in self.house) -10
				else:
					return sum(v[2] for v in self.house)
			#no the player doesn't have an ace
			else:
				if sum(v[2] for v in self.house) == 21:
					return 21
				elif sum(v[2] for v in self.house) > 21:
					return 'dealerbusts'
				else:
					return sum(v[2] for v in self.house)
	def draw_card(self,turn):
		if turn == 'player':
			#print(len(self.cards))
			draw = self.rnd.randint(1,len(self.cards)-1)
			#print(draw)
			self.player.append(self.cards[draw])
			del self.cards[draw]
			#print(self.player[-1])
			
		else:
			#print(len(self.cards))
			draw = self.rnd.randint(1,len(self.cards)-1)
			#print(draw)
			self.house.append(self.cards[draw])
			del self.cards[draw]
			#print(self.house[-1])

	def physical_card(self,hand):
		if hand == 'player':
			num = 8
			cards = len(self.player)
			values = [[' ','-','-','-','-','-','-','-','-','  ']*cards,['|','=','=','=','=','=','=','=','=','|',' ']*cards,['|','=',num,'♥','=','=','=','=','=','|',' ']*cards,['|','=','=','=','=','=','=','=','=','|',' ']*cards,['|','=','=','=','=','♡','=','=','=','|',' ']*cards,['|','=','=','=','=','=','=','=','=','|',' ']*cards,['|','=','=','=','=','=',num,'♡','=','|',' ']*cards,['|','=','=','=','=','=','=','=','=','|',' ']*cards,[' ','-','-','-','-','-','-','-','-','  ']*cards]
			for x in range(0,cards):
				
				if self.player[x][0] == '10':
					
					values[2][2+(11*x)] = self.player[x][0]
					values[2][3+(11*x)] = self.player[x][1]
					values[2][4+(11*x)] = ''

					values[6][6+(11*x)] = self.player[x][0]
					values[6][7+(11*x)] = self.player[x][1]
					values[6][5+(11*x)] = ''
					
				else:
					values[2][2+(11*x)] = self.player[x][0]
					values[2][3+(11*x)] = self.player[x][1]

					values[6][6+(11*x)] = self.player[x][0]
					values[6][7+(11*x)] = self.player[x][1]
			return values
		else:
			num = 8
			cards = len(self.house)
			values = [[' ','-','-','-','-','-','-','-','-','  ']*cards,['|','=','=','=','=','=','=','=','=','|',' ']*cards,['|','=',num,'♥','=','=','=','=','=','|',' ']*cards,['|','=','=','=','=','=','=','=','=','|',' ']*cards,['|','=','=','=','=','♡','=','=','=','|',' ']*cards,['|','=','=','=','=','=','=','=','=','|',' ']*cards,['|','=','=','=','=','=',num,'♡','=','|',' ']*cards,['|','=','=','=','=','=','=','=','=','|',' ']*cards,[' ','-','-','-','-','-','-','-','-','  ']*cards]
			for x in range(0,cards):
				
				if self.house[x][0] == '10':
					
					values[2][2+(11*x)] = self.house[x][0]
					values[2][3+(11*x)] = self.house[x][1]
					values[2][4+(11*x)] = ''

					values[6][6+(11*x)] = self.house[x][0]
					values[6][7+(11*x)] = self.house[x][1]
					values[6][5+(11*x)] = ''
					
					
				else:
					values[2][2+(11*x)] = self.house[x][0]
					values[2][3+(11*x)] = self.house[x][1]

					values[6][6+(11*x)] = self.house[x][0]
					values[6][7+(11*x)] = self.house[x][1]
			return values



	def deposit(self,amount):
		self.amount += amount

	def withdraw(self,amount):
		self.amount -= amount

	def bet(self,amount):
		if amount <= self.amount:
			cards.betval = amount
			return 'bet placed!'
		else:
			return 'you don\'t have enough to place that bet'

	def buildasciihand(self,hand):

		if hand == 'stand':
			myline = ''
			values = cards.physical_card('house')
			for i in range(len(values)):
			    for j in range(len(values[i])):
			        myline += str(values[i][j])
			    #print(myline)
			    cards.printhand += myline + '\n'	
			    myline=''
		elif hand == 'hit':
			myline = ''
			values = cards.physical_card('house')
			for i in range(len(values)):
			    for j in range(len(values[i])):
			    	if (j > 11 and j < 20) and i not in [0,8]:
			    		myline += 'X'

			    	else:
			        	myline += str(values[i][j])
			    #print(myline)
			    cards.printhand += myline + '\n'
			    myline=''


		#this is the players hand
		elif hand == 'player':
			myline = ''
			values = cards.physical_card('player')
			for i in range(len(values)):
			    for j in range(len(values[i])):
			        myline += str(values[i][j])
			    #print(myline)
			    cards.printhand += myline + '\n'
			    myline=''

cards = Cards()

val = 'N'
deal = 0
player = 'hit'
betval = ''
while str.upper(val) != 'Y':
	if deal == 0:
		if cards.amount <= 0:
			print('you\'re broke, goodbye')
			break
		deal +=1
		cards.draw_card('player')
		cards.draw_card('player')
		cards.draw_card('house')
		cards.draw_card('house')		
		os.system('clear')
		cards.printhand = f'You have {cards.amount} to play with. \nHow much do you want to bet?\n'
		print(cards.printhand)
		betval = cards.bet(int(input()))
		#do you have enough to bet?

		while betval != 'bet placed!':
			print(f"You don\'t have enough to place that bet, you have {cards.amount}!\n")
			betval = cards.bet(int(input()))

		#cards.printhand =''
		cards.printhand = f'Your bet has been placed.\n'
		os.system('clear')
		#this is where I build the first hand after the bet is placed

		if cards.checkhandvalue('house') == 'Blackjack' and cards.checkhandvalue('player') == 'Blackjack':
			cards.buildasciihand('stand')
			cards.buildasciihand('player')
			cards.printhand += '\n PUSH!!!\n\n play again?'
			print(cards.printhand)
			val = str.upper(input('want to quit? Y/N '))
			cards.shuffle()
			deal = 0
			os.system('clear')
		elif cards.checkhandvalue('house') == 'Blackjack': 
			cards.buildasciihand('stand')
			cards.buildasciihand('player')
			cards.printhand += '\n Dealer has BlackJack!!!\n\n play again?'
			print(cards.printhand)
			val = str.upper(input('want to quit? Y/N '))
			cards.shuffle()
			cards.withdraw(cards.betval)
			deal = 0
			os.system('clear')
		elif cards.checkhandvalue('player') == 'Blackjack':
			cards.buildasciihand('stand')
			cards.buildasciihand('player')
			cards.printhand += '\n You have BlackJack!!!\n\n play again?'
			print(cards.printhand)
			val = str.upper(input('want to quit? Y/N '))
			cards.shuffle()
			deal = 0
			cards.deposit(cards.betval)
			os.system('clear')
		else:

			cards.buildasciihand('hit')
			cards.buildasciihand('player')
			cards.printhand += 'Hit or Stand? H/S?'
			print(cards.printhand)
			player = str.upper(input())
			os.system('clear')
	else:
		'''
		cards.draw_card('player')
		os.system('clear')
		'''
		if player == 'H':
			os.system('clear')
			cards.printhand = ''
			cards.draw_card('player')
			#os.system('clear')
			cards.buildasciihand('hit')
			cards.buildasciihand('player')
		#cards.printhand  += f'\n \nPlace your bet, you currently have {cards.amount} \n'
		#my_sum=sum(v[1] for v in my_array if v[0]==1)
			if cards.checkhandvalue("player") == 'playerbusts':
				#cards.buildasciihand('hit')
				#cards.buildasciihand('player')
				cards.printhand += '\n YOU LOOSE\nDo you want to quit? Y/N'
				print(cards.printhand)
				val = str.upper(input())
				cards.shuffle()
				cards.withdraw(cards.betval)
				deal = 0
				os.system('clear')
			elif  cards.checkhandvalue("player") == 21:
				cards.printhand += '\n YOU WIN\nDo you want to quit? Y/N'
				print(cards.printhand)
				val = str.upper(input())
				cards.shuffle()
				cards.deposit(cards.betval)
				deal = 0
			else:
				cards.printhand += '\nHit or Stand? H/S?'
				print(cards.printhand)
				player = str.upper(input())
		else:

			os.system('clear')
			cards.printhand =''
			cards.draw_card('house')
			#cards.buildasciihand('stand')
			#	cards.buildasciihand('player')
			#see if the house is winning or loosing. 
			if cards.checkhandvalue('dealer') == '21':
				cards.buildasciihand('stand')
				cards.buildasciihand('player')
				cards.printhand += '\n Dealer Wins!!!\n\n play again?'
				print(cards.printhand)
				cards.withdraw(cards.betval)
				val = str.upper(input('want to quit? Y/N '))
				cards.shuffle()
				deal = 0
				os.system('clear')
			elif cards.checkhandvalue('dealer') == 'dealerbusts':
				cards.buildasciihand('stand')
				cards.buildasciihand('player')
				cards.printhand += '\n Dealer Busts, you WIN!!!\n\n play again?'
				print(cards.printhand)
				val = str.upper(input('want to quit? Y/N '))
				cards.shuffle()
				cards.deposit(cards.betval)
				deal = 0
				os.system('clear')
			elif cards.checkhandvalue('dealer') > cards.checkhandvalue('player'):
				cards.buildasciihand('stand')
				cards.buildasciihand('player')
				cards.printhand += '\n Dealer Wins!!!\n\n play again?'
				print(cards.printhand)
				val = str.upper(input('want to quit? Y/N '))
				cards.shuffle()
				cards.withdraw(cards.betval)
				deal = 0
				os.system('clear')
			elif cards.checkhandvalue('dealer') == cards.checkhandvalue('player'):
				cards.buildasciihand('stand')
				cards.buildasciihand('player')
				cards.printhand += '\n PUSH!!!\n\n play again?'
				print(cards.printhand)
				val = str.upper(input('want to quit? Y/N '))
				cards.shuffle()
				deal = 0
				os.system('clear')




			#cards.printhand += f'player {cards.player} {cards.checkhandvalue("player")} (house{cards.house} {cards.checkhandvalue("house")} {cards.checkhandvalue("house")}\n'
			#print(cards.printhand)

		#print('How much do you want to bet?')
		#if the deal is == 0 I need to see if the dealer won with a 
		

		#val = str.upper(input('want to quit? Y/N '))
		#cards.printhand = ''

