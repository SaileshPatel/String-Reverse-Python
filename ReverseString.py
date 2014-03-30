program = True

while program:
	string = raw_input("Enter the string you wish to reverse:\n")
	print string[::-1]
	print "Please choose what you'd like to do:\n"
	print "1: Restart the program"
	print "2: Exit the program\n"
	print "Enter the number:\n"
	choice = raw_input()

	if choice == '1':
		program = True

	elif choice == '2':
		print "Goodbye!"
		program = False

	else:
		print "Choose a valid option!!"