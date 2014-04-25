from sys import exit

def dead(why):
	exit(0)

def start():
	print("Select one of the two options!")
	print("1. Lower Case")
	print("2. Upper Case")
	print("Press any other key to exit.")

	option = input("> ")
	if option == "1":
		lowerCase()
	elif option == "2":
		upperCase()
	else:
		dead("Thank you for using ReverseString!")

def lowerCase():
	print("Enter the string you wish to reverse.")
	word = input("> ")
	print(word[::-1].lower())
	start()

def upperCase():
	print("Enter the string you wish to reverse.")
	word = input("> ")
	print(word[::-1].upper())
	start()

start()