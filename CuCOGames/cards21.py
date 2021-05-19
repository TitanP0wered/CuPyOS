import random

#hearts
h2 = 2
h3 = 3
h4 = 4
h5 = 5
h6 = 6
h7 = 7
h8 = 8
h9 = 9
h10 = 10
h_j = 10
h_q = 10
h_k = 10
h_a = 10
#diamonds
d2 = 2
d3 = 3
d4 = 4
d5 = 5
d6 = 6
d7 = 7
d8 = 8
d9 = 9
d10 = 10
d_j = 10
d_q = 10
d_k = 10
d_a = 10
#clubs
c2 = 2
c3 = 3
c4 = 4
c5 = 5
c6 = 6
c7 = 7
c8 = 8
c9 = 9
c10 = 10
c_j = 10
c_q = 10
c_k = 10
c_a = 10
#spades
s2 = 2
s3 = 3
s4 = 4
s5 = 5
s6 = 6
s7 = 7
s8 = 8
s9 = 9
s10 = 10
s_j = 10
s_q = 10
s_k = 10
s_a = 10
deck = [h2,h3,h4,h5,h6,h7,h8,h9,h10,h_j,h_q,h_k,h_a,d2,d3,d4,d5,d6,d7,d8,d9,d10,d_j,d_q,d_k,d_a,c2,c3,c4,c5,c6,c7,c8,c9,c10,c_j,c_q,c_k,c_a,s2,s3,s4,s5,s6,s7,s8,s9,s10,s_j,s_q,s_k,s_a]

playerScore = 0
comp1Score = 0
comp2Score = 0

#selects a card at random from the deck and assignes it to
def cardPick():
	print("game loop")
	#selects 1 card for the player
	pickedCardP = random.choice(deck)
	playerScore == playerScore + pickedCardP
	deck.remove(pickedCardP)
	print(playerScore)
	#selects 1 card for opponent 1
	pickedCardC1 = random.choice(deck)
	comp1Score == comp1Score + pickedCardC1
	deck.remove(pickedCardC1)
	print(comp1Score)
	#selects 1 card for opponent 2
	pickedCardC2 = random.choice(deck)
	comp2Score == comp2Score + pickedCardC2
	deck.remove(pickedCardC2)
	print(comp2Score)

def gameLoop():
	cardPick()

def cardsPlay():
	playCheck = input('''Are you sure you want to play? [y/n]
''')#check to start game or leave
	if playCheck == "y":
		print("Let's begin...")
		gameLoop()
	if playCheck == "n":
		exitCmd()

def exitCmd():
	print("Exiting cards...")

def begin():
	print("Welcome to the 21 card game.")
	print('''This version uses default rules
(Number cards equal their number,
 Kings, Queens and Jacks are equal to 10 each,
 and Aces are also 10.)
''')
	cardsPlay()


#/self reminder: to remove a variable from an array use
#/ arrayName.remove(variableName)