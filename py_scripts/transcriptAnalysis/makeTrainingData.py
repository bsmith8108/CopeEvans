import get_data as gd
from random import randint
import re

def makeTrainingData(wordList):
    list_of_dicts = gd.get_data_list_of_dicts()
    wordCounts = []
    probability = 3
    full = []
    partial = []

    for entry in list_of_dicts:
	tempDict = {}
	decade = "unkown"
	if len(entry["Date"]) > 3:
	    decade = entry["Date"][:3] + "0"
	
	tempDict["class"] = decade

	t = entry["Transcript"]
	t = t.replace("<br>", " ")
	t = t.replace("COMMA", " ")
	t = re.sub('\W',' ',t)
	t = t.split(" ")
	
	for word in t:
	    if not word == "" and word in wordList:
		word = word.lower()
		try:
		    tempDict[word] += 1
		except:
		    tempDict[word] = 1

	full.append(tempDict)	

	temp = randint(0,10)
	if temp > probability:
	    partial.append(tempDict)

    filename1 = "trainingData.csv"
    filename2 = "fullData.csv"
    wordList.append("class")
    headers = wordList
    gd.write_data_dicts(filename1,headers,partial)	
    gd.write_data_dicts(filename2,headers,full)
