import random
import time
from colorama import Fore, Back, Style
#commands
from CuModules import cLs
from CuModules import cCalculator
from CuModules import crypto
#games
from CuCOGames import gLs
from CuCOGames import cards21
from CuCOGames import movement_test
from CuCOGames import dice

runModule = '''Type in a command name to run it:
'''

def exit():
	print("Shutting down...")
	time.sleep(2)
	quit()

#random messages
rndMsg1 = "I REALLY like placeholders :)"
rndMsg2 = "Use the command 'ls' to show a list of currently available commands."
rndMsg3 = "My code is an absolute mess"
rndMsg4 = "entering 'esc' as a command will exit the application"
rndMsg5 = "this project is still in beta. expect bugs and errors."
rndMsg6 = "e"

rndMsgList = [rndMsg1, rndMsg2, rndMsg3, rndMsg4, rndMsg5, rndMsg6]

#start messages
welcomeMsg = '''welcome to the Copper Python Operating System Project,
or CuPyOS for short.
'''
randomMsg = '''Random message for this boot is:'''

#games notice
gameL = ["game", "games"]
gWarn = '''In order to play games you must use an extended command,
this means that if you want to run a game you have to put a 'game/' before the game name,
for example: 'game/dice' .'''

print(Back.BLACK + Fore.WHITE + welcomeMsg)
print(Back.BLACK + Fore.WHITE + randomMsg)
print(Back.BLACK + Fore.RED + random.choice(rndMsgList))

pList = ["ls", "calc","crypto" , "mvmt", "games", "game/ls", "game/dice", "game/21"]

#command handler
#> very janky, not efficient, need to rewrite if adding more commands in the future
#> works for now :)
def openProgram():
	openP = input(Style.RESET_ALL + runModule)
	#regular commands
	if openP == "ls":
		cLs.ls()
		openProgram()
	if openP == "calc":
		cCalculator.calcRun()
		openProgram()
	if openP == "crypto":
		crypto.cipherPick()
		openProgram()
	#games ls
	if openP == "game/ls":
		gLs.ls()
		openProgram()
	#games
	if openP == "mvmt":
		movement_test
		openProgram()
	if openP == "game/dice":
		dice.diePicker()
		openProgram()
	if openP == "game/21":
		cards21.begin()
		openProgram()
	#games warning
	if openP in gameL:
		print(gWarn)
		openProgram()
	#exit
	if openP == "esc":
		exit()
	#error catcher
	if openP not in pList:
		print("Invalid command, try again.")
		openProgram()

openProgram()