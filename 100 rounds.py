# author: Hendrixthecool
switch = 
Round = 0
people = range(1, 101)
while Round < 100:
	if people % Round == 0:
		if switch == True:
			switch = False
			switch = switch + 1
		if switch == False:
			switch = True
			switch = switch + 1
print str (switch)