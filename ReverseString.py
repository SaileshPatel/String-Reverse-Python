keepProgramRunning = True
while keepProgramRunning:
	print "If you wish your reversed string to be printed in upper case letters, enter 1.\n"
	print "If you wish your reversed string to be printed in lower case letters, enter 2."
	choice = raw_input()
	if choice == "1":
		print "Enter the string you wish to be reversed."
		string = raw_input()
		print string[::-1].upper()
		keepProgramRunning = False
	elif choice == "2":
		print "Enter the string you wish to be reversed."
		string = raw_input()
		print string[::-1].lower()
		keepProgramRunning = False
	else:
		print "Enter a valid option.\n"
		keepProgramRunning = True