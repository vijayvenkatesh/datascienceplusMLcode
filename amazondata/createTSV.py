
TSV = {}
TSVList = []
f = '/Users/vjbu/Google Drive/classes/datascience/data/amazondata/movies.small'
lines = [line.strip() for line in open(f)]
print lines
for eachitem in lines:
	key =  eachitem.strip().split(":")
	#print key
	if len (key) == 2:
		if key[0].startswith("product"):
			TSV["ASIN"] = key[1].strip()
		if 'helpfulness' in key[0]:
			helpfulness = key[1][0:].strip().split("/")
			if helpfulness[1] == 0:
				TSV['helpfulness'] = float(helpfulness[0])
			elif helpfulness[1] > 0:
				print helpfulness[0]
				print helpfulness[1]
				#TSV['helpfulness'] = float (helpfulness[0]) / float(helpfulness[1])
		if 'score' in key[0]:
			score = key[1].strip()
			TSV['score'] = int(float(score))
	elif len(key) == 3:
		if 'text' in key[0]:
			TSV['review text'] = key[2]
	TSVList.append(TSV)
print TSVList

		#if key.end 
	#elif len(key) == 3:

	#print key.
	#print key
# for l in f:
# 	lines = l.split(",")
# 		key = lines[3]
# 		value = lines[4].strip("\r\n")
		#value_int = int (value)
		#print value_int
		# salaries[playerID] = salaries.get(playerID, []) + [salary]
		#salaries.get(playerID,[]).append(salary)
		