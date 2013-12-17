def average(salaries):
	for key, value in salaries.items():
		x = 0.0
		for pay in value:
			x = x + pay
		print key, x/len(value), value


avg = {}
with open('/Users/vjbu/Google Drive/classes/datascience/data/Salaries.csv') as f:
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

