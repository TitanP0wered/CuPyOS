dieLs = ["d6", "d10", "esc"]
YorN = ["y", "n"]

import random
import time

def exitCmd():
	print("Exiting 'Dice'")

def diePicker():
	selDie = input('''What kind of dice would you like to roll?
Currently supported dice: [d6/d10]
(input adapting dice will be implemented to accomodate any side numbers,
in a future update)
''')
	if selDie == "esc":
		exitCmd()
	side_list = list(range(1, selDie))
	
	if selDie == "d6":
			pass
		d6Arr = ["1", "2", "3", "4", "5", "6"]
		dieAns = random.choice(d6Arr)
		print("Your rolled ", dieAns)
		time.sleep(1)
		reRoll = input('''Would you like to roll again? [y/n]
''')
		if reRoll == "y":
			diePicker()
		if reRoll == "n":
			exitCmd()
		if reRoll not in YorN:
			print("Answer not understood, exiting anyway...")
			exitCmd()
	if selDie == "d10":
		pass
		d10Arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
		dieAns = random.choice(d10Arr)
		print("Your rolled ", dieAns)
		time.sleep(1)
		reRoll = input('''Would you like to roll again? [y/n]
''')
		if reRoll == "y":
			diePicker()
		if reRoll == "n":
			exitCmd()
		if reRoll not in YorN:
			print("Answer not understood, exiting anyway...")
			exitCmd()
	if selDie not in dieLs:
		pass
		print("Invalid die side ammount, try again.")
		diePicker()