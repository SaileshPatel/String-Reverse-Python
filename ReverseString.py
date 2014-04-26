# importing exit from sys
from sys import exit

# creating a function to kill the program
def dead(why):
	# exits program without error
	exit(0)

# creating a function called start
def start():
	# printing multiple string
	print("Select one of the two options!")
	print("1. Lower Case")
	print("2. Upper Case")
	print("Press any other key to exit.")

	# assigning user input to variable 'option'
	option = input("> ")
	# if the variable of option == '1'
	if option == "1":
		# then lowerCase is activated
		lowerCase()
	# if the variable of option == '2'
	elif option == "2":
		# then upperCase is activated
		upperCase()
	# if the value of option is anything else
	else:
		# uses 'dead' function to kill the program
		dead("Thank you for using ReverseString!")

# creating a function called 'lowerCase()'
def lowerCase():
	# printing string
	print("Enter the string you wish to reverse.")
	# assigning value to variable
	word = input("> ")
	# printing the value of word and reversing it
	print(word[::-1].lower())
	# user is then refered back to the function 'start()'
	start()

# creating a function called upperCase
def upperCase():
	# printing string
	print("Enter the string you wish to reverse.")
	# assigning value to variable
	word = input("> ")
	# reversing string in variable and printing the result
	print(word[::-1].upper())
	# user is then refered back to the function 'start()'
	start()

# loads the function 'start()'
start()