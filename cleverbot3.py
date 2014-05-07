# author: Hendrixthecool
answer = input("Speak human.")
answer = answer.lower()
two = answer.split()
battery = 100
while battery > 0:
	while len(two) > 0:
		if two[0] == "are":
			if two[1] == "you":
				if two[2] == "crazy!?!?":
					print("no, i am CLEVER")
			if two[1] == "you":
				if two[2] == "a":
					if two[3] == "superhero?":
						print "yes"
	else:
		print("I cant here you")
		battery = battery - 1
		print("so -1 battery and now i have"),
		print str (battery) + "% battery left"