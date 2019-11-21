import os
class Cards():
	import random as rnd
	def __init__(self):
		#using ascii there are the four suits
		foursuits = ('♥','♣','♠','♦')
		#10 - Ace
		tenandface = ('J','Q','K','A')
		#number cards
		numbercards = range(2,11)

		thedeck = []

		amount = 100

		#using this to generate the ascii hand into a list	
		for suit in foursuits:
			for face in tenandface:
				thedeck.append([f'{face}',f'{suit}'])				
			for number in numbercards:
				thedeck.append([f'{number}',f'{suit}'])

		self.cards = thedeck
		self.player = []
		self.house = []
		#print(type(thedeck))

	def checkhandvalue(self,hand):
		pass

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
					
				else:
					values[2][2+(11*x)] = self.player[x][0]
					values[2][3+(11*x)] = self.player[x][1]
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
					
				else:
					values[2][2+(11*x)] = self.house[x][0]
					values[2][3+(11*x)] = self.house[x][1]
			return values



	def deposit(self,amount):
		self.amount += amount


	def bet(self,amount):
		if amount < self.amount:
			self.amount -= amount
			return 'bet placed!'
		else:
			return 'you don\'t have enough to place that bet'




cards = Cards()

val = 'N'
deal = 0
player = 'hit'
while str.upper(val) != 'Y':
	if deal == 0:
		cards.draw_card('player')
		cards.draw_card('player')
		cards.draw_card('house')
		cards.draw_card('house')		
		deal = 1
		os.system('clear')
		print ('you have 100$ to play with')
	else:
		cards.draw_card('player')
		os.system('clear')
	
	#this is dealers hand
	

	if player == 'stand':
		myline = ''
		values = cards.physical_card('house')
		for i in range(len(values)):
		    for j in range(len(values[i])):
		        myline += str(values[i][j])
		    print(myline)	
		    myline=''
	else:
		myline = ''
		values = cards.physical_card('house')
		for i in range(len(values)):
		    for j in range(len(values[i])):
		    	if (j > 11 and j < 20) and i not in [0,8]:
		    		myline += 'X'

		    	else:
		        	myline += str(values[i][j])
		    print(myline)
		    myline=''


	#this is the players hand

	myline = ''
	values = cards.physical_card('player')
	for i in range(len(values)):
	    for j in range(len(values[i])):
	        myline += str(values[i][j])
	    print(myline)
	    myline=''


	val = str.upper(input('want to quit? Y/N '))

