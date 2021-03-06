import os,csv

queryDict = {"src_acceptable_source":True}
queryDictColumnNumberAndString = {}
headerRowColumnNumDict = {}
dataFile = "data.csv"
def main():
	with open(dataFile,"rU") as csvFile:
		newFileData = [list(line) for line in csv.reader(csvFile)]

	#For the new file, get header data in dict
	headerRow = newFileData[0]
	headerRowColumnNumDict = getHeaderColumnNumbers(headerRow)
	#Remove the header row from the top of the list
	newFileData.pop(0)

	for columnTitle in queryDict:
		#Get column number for query column name
		columnNumberFromQuery = headerRowColumnNumDict[columnTitle]
		valueFromQuery = queryDict[columnTitle]
		queryDictColumnNumberAndString[columnNumberFromQuery] = valueFromQuery

	#Logic for finding rows I care about
	for line in newFileData:
		pass				

def getHeaderColumnNumbers(headerRow):
	global headerRowColumnNumDict
	for index,column in enumerate(headerRow):
		headerRowColumnNumDict[column] = index
	return(headerRowColumnNumDict)


if __name__ == "__main__":
	main()