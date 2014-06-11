import get_data as gd
import re
import operator

list_of_dicts = gd.get_data_list_of_dicts()

decades_list = [{"decade":"1800","words":{}, "letters":0, "wordCount":0},
	      {"decade":"1810", "words":{}, "letters":0, "wordCount":0},
	      {"decade":"1820", "words":{}, "letters":0, "wordCount":0},
	      {"decade":"1830", "words":{}, "letters":0, "wordCount":0},
	      {"decade":"1840", "words":{}, "letters":0, "wordCount":0},
	      {"decade":"1850", "words":{}, "letters":0, "wordCount":0},
	      {"decade":"1860", "words":{}, "letters":0, "wordCount":0},
	      {"decade":"1870", "words":{}, "letters":0, "wordCount":0},
	      {"decade":"1880", "words":{}, "letters":0, "wordCount":0},
	      {"decade":"1890", "words":{}, "letters":0, "wordCount":0},
	      {"decade":"1900", "words":{}, "letters":0, "wordCount":0},
	      {"decade":"1910", "words":{}, "letters":0, "wordCount":0},
	      {"decade":"unknown", "words":{}, "letters":0, "wordCount":0}
	      
	    ]

decade_lookup = {"80":0,
		 "81":1,
		 "82":2,
		 "83":3,
		 "84":4,
		 "85":5,
		 "86":6,
		 "87":7,
		 "88":8,
		 "89":9,
		 "90":10,
		 "91":11,
		 "unknown":12
		}
word_dict = {}
counter = 0
for entry in list_of_dicts:
    decade = "unknown"
    if len(entry["Date"]) > 2:
	decade = entry["Date"][1:3]

    try:
	index = decade_lookup[decade]
    except:
	index = 12
	
    decades_list[index]["letters"] += 1

    t = entry["Transcript"]
    t = t.replace("<br>", " ")
    t = t.replace("COMMA", " ")
    t = re.sub('\W',' ',t)
    t = t.split(" ")
    for word in t:
	decades_list[index]["wordCount"] += 1
	word = word.lower()
	try:
	    word_dict[word] += 1
	    decades_list[index]["words"][word] += 1
	except:
	    word_dict[word] = 1
	    decades_list[index]["words"][word] = 1
    counter += 1

sorted_words = sorted(word_dict.iteritems(), key=operator.itemgetter(1))

"""
testWord = "day"
print "Decade\t# of \""+testWord+"\"\tLetters that Decade\tPercentage of Words"
for decade in decades_list:
    try:
	percentage = float(decade["words"][testWord])/float(decade["wordCount"])
	instances = str(decade["words"][testWord])
    except:
	percentage = 0
	instances = "0"
    print decade["decade"] + "\t" + instances + "\t\t\t" + str(decade["letters"])+"\t\t"+str(percentage)
"""
for entry in sorted_words:
    print entry

