encORdec = ["enc", "dec"]
cryptTypes = ["ceasar", "esc"]

def intCeasar():
	EncDec = input('''Would you like to encrypt or decrypt some text?
[enc/dec]
''')
	if EncDec == "enc":
		trueMsg = input('''Enter the text you would like to encrypt:
''')
		transMsg = trueMsg.replace("a", "!").replace("b", "£").replace("c", "$").replace("d", "€").replace("e", "^").replace("f", "&").replace("g", "*").replace("g", "(").replace("h", ")").replace("i", "-").replace("k", "_").replace("l", "=").replace("m", "+").replace("n", "[").replace("o", "]").replace("p", "{").replace("q", "}").replace("r", ";").replace("s", ":").replace("t", "'").replace("u", "@").replace("v", "#").replace("w", "~").replace("x", "|").replace("y", "/").replace("z", "?")
		trans2Msg = transMsg.replace("!", "d").replace("£", "e").replace("$", "f").replace("€", "g").replace("^", "h").replace("&", "i").replace("*", "j").replace("(", "k").replace(")", "l").replace("-", "m").replace("_", "n").replace("=", "o").replace("+", "p").replace("[", "q").replace("]", "r").replace("{", "s").replace("}", "t").replace(";", "u").replace(":", "v").replace("'", "w").replace("@", "x").replace("#", "y").replace("~", "z").replace("|", "a").replace("/", "b").replace("?", "c")
		print("Your encrypted message is:")
		print(trans2Msg)
	if EncDec == "dec":
		trueMsg = input('''Enter the text you would like to decrypt:
''')
	transMsg = trueMsg.replace("a", "!").replace("b", "£").replace("c", "$").replace("d", "€").replace("e", "^").replace("f", "&").replace("g", "*").replace("g", "(").replace("h", ")").replace("i", "-").replace("k", "_").replace("l", "=").replace("m", "+").replace("n", "[").replace("o", "]").replace("p", "{").replace("q", "}").replace("r", ";").replace("s", ":").replace("t", "'").replace("u", "@").replace("v", "#").replace("w", "~").replace("x", "|").replace("y", "/").replace("z", "?")
	trans2Msg = transMsg.replace("!", "x").replace("£", "y").replace("$", "z").replace("€", "a").replace("^", "b").replace("&", "c").replace("*", "d").replace("(", "e").replace(")", "f").replace("-", "g").replace("_", "h").replace("=", "i").replace("+", "j").replace("[", "k").replace("]", "l").replace("{", "m").replace("}", "n").replace(";", "o").replace(":", "p").replace("'", "q").replace("@", "r").replace("#", "s").replace("~", "t").replace("|", "u").replace("/", "v").replace("?", "w")
	print(transMsg)
	if EncDec == "esc":
		leave()
	if EncDec not in encORdec:
		print("invalid input, try again...")
		intCeasar()

def leave():
	print("Exiting the cryptography program...")

#selection
def cipherPick():
	cryptSel = input('''What type of cipher would you like to use?
[ceasar]
''')
	if cryptSel == "ceasar":
		intCeasar()
	if cryptSel == "esc":
		leave()
	if cryptSel not in cryptTypes:
		print("Invalid input, try again...")
		cipherPick()