import get_data as gd
from random import randint
import re

def makeTrainingData(wordList):
    list_of_dicts = gd.get_data_list_of_dicts()
    wordCounts = []
    probability = 3
    full = []
    partial = []
    added = {"0-10":False,
	     "10-20":False,
	     "20-30":False,
	     "30-40":False,
	     "40-50":False,
	     "50-60":False,
	     "60-70":False,
	     "70-80":False,
	     "80-90":False,
	     "unkown":False
	     }

    for entry in list_of_dicts:
	tempDict = {}
	decade = "unkown"
	if len(entry["Age of Author"]) > 3 and len(entry["Age of Author"]) < 9:
	    decade = entry["Age of Author"]
	
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
	if temp > probability or not added[decade]:
	    added[decade] = True
	    partial.append(tempDict)

    filename1 = "trainingData.csv"
    filename2 = "fullData.csv"
    wordList.append("class")
    headers = wordList
    gd.write_data_dicts(filename1,headers,partial)	
    gd.write_data_dicts(filename2,headers,full)
