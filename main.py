import os,csv

headerRowColumnNumDict = {}
dataFile = "data.csv"
def main():
	with open(dataFile,"rU") as csvFile:
		newFileData = [list(line) for line in csv.reader(csvFile)]

	#For the new file, get header data in dict
	headerRow = newFileData[0]
	getHeaderColumnNumbers(headerRow)


def getHeaderColumnNumbers(headerRow):
	global headerRowColumnNumDict
	for index,column in enumerate(headerRow):
		headerRowColumnNumDict[column] = index


if __name__ == "__main__":
	main()