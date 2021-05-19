from colorama import Fore, Back, Style
#> there is literally nothing to document here its literally just a print command
def ls():
	print("This is the current list of programs:")
	print(Back.BLACK + Fore.WHITE + '''ls (shows a list of all commands)
	cal (opens a text based calculator app)
	crypto (allows for encryption and dectryption of messages)
	game/ls (shows a list of currently included games)
''')