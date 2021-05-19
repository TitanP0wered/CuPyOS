from time import sleep
import math

#> this is stupid but it works so I'm keeping it
def scriptEnd():
	sleep(0.5)
	input('''Hit your "ENTER" key to exit the program''')


def calcApp(num1,symbol,num2):
	print("Your answer is:")
	#converts number arguments to floats
	num1a = float(num1)
	num2a = float(num2)
	#checks for which math operator to use and then prints the answer
	if symbol == "+":
		print(math.floor(num1a + num2a))
	if symbol == "-":
		print(math.floor(num1a - num2a))
	if symbol == "*":
		print(math.floor(num1a * num2a))
	if symbol == "/":
		print(math.floor(num1a / num2a))
		#check for another calculation
	calcAgain = input('''Would you like to work out another equation? [y/n]
''')
	if calcAgain == "n":
		scriptEnd()
	if calcAgain == "y":
		calcRun()

def calcRun():
	print("This is the calculator app")
	equation = input('''Please input an equation into the calculator
or type 'esc' into the input field.
Use the provided operators: [+|-|*|/]
In the arrangement 'number1 operator number2'
(Make sure to put spaces between your arguments or it won't be recognised)
''')
	#exit before calculation
	if equation == "esc":
		scriptEnd()
	else:
		#> I have spent more time on catching errors rather that actually making it work
		#error catch:
		if equation.count(" ") == 2:
			#equation split into arguments:
				num1, symbol, num2 = equation.split(" ")
				print(num1, symbol, num2)
				inputCheck = input('''Correct? [y/n]
''')
				#check for another calculation
				if inputCheck == "n":
					calcRun()
				elif inputCheck == "y":
					calcApp(num1,symbol,num2)
		else:
			print("Invalid equation, try again")
			calcRun()