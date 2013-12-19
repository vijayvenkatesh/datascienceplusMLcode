def printfile(data = []):
	fo = open("foo.txt", "wb")
	fo.writelines('\t'.join(i) for i in ['ASIN','helpfulness','score','review text'])
	for line in data:
		fo.writelines("%s\t" % j for j in line.values())



if __name__ == "__main__":
	TSV = {}
	TSVList = []
	f = '/users/vijay/Google Drive/classes/datascience/data/amazondata/movies.small'
	lines = [line.strip() for line in open(f)]
#print lines
	for eachitem in lines:
		key =  eachitem.strip().split(":")
		#print key
		if len (key) == 2:
			if key[0].startswith("product"):
				TSV["ASIN"] = key[1].strip()
			if 'helpfulness' in key[0]:
				helpfulness = key[1][0:].strip().split("/")
				print helpfulness
				if float(helpfulness[1]) == 0:
					TSV['helpfulness'] = float(helpfulness[0])
				elif float(helpfulness[1]) > 0:
				#print helpfulness[0]
				#print helpfulness[1]
					TSV['helpfulness'] = float (helpfulness[0]) / float(helpfulness[1])
			if 'score' in key[0]:
				score = key[1].strip()
				TSV['score'] = int(float(score))
		elif len(key) == 3:
			if 'text' in key[0]:
				TSV['review text'] = key[2]
		TSVList.append(TSV)
printfile(TSVList)
print TSVList



