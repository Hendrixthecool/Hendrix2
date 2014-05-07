# author: Hendrixthecool
switch = "off"
Round = range(1, 101)
people = range(1, 101)
for noobs in Round:
	for p in people:
		if p % noobs == 0:
			if switch == "on":
				switch = "off"
			elif switch == "off":
				switch = "on"
print str (switch)