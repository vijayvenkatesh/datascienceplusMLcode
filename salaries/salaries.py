import sys

def average(salaries):
	playerIdNames = names(salaries.keys()) # Make a call to the names function to get the real list of names
	
	for key, value in salaries.items():
		x = 0.0
		for pay in value:
			x = x + pay
		print playerIdNames[key], x/len(value)

# This function takes the list of names and returns a dictionary of playerId: "FirstName + LastName"
def names( keys = []):
	IdToNames = {}
	master = sys.argv[2]
	with open(master) as f:
		next(f)
		for line in f:
			lines = line.split(",")
			playerId = lines[1]
			fname = lines[16]
			lname = lines[17]
			IdToNames[playerId] = fname + " " + lname
	return IdToNames


avg = {}
salary = sys.argv[1]
with open(salary) as f:
	next(f)
	for l in f:
		lines = l.split(",")
		key = lines[3]
		value = lines[4].strip("\r\n")
		#value_int = int (value)
		#print value_int
		if key in avg:
			avg[key].append(int(value))
		else:
			avg[key] = list()
			avg[key].append(int(value))

	#print avg.values()

	average(avg)

