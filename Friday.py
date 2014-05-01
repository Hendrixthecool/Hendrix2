# author: Hendrixthecool
day = 1
month = 1
year = 1900
total = 0

def daysinMonth():
	return 30

while year < 2015:
	for number in year:
		total = total + 1
		if day == 30:
			day = 1
			month = month + 1
			if month == 12:
				month = 1
				year = year + 1
			else:
					month = month + 1
		else:
			day = day + 1
print str(total) + " ohh"