import get_data as gd

def get_subjects(list_of_dicts):
	# list_of_dicts = gd.get_data_list_of_dicts()
	has_subject = []
	for entry in list_of_dicts:
	    if entry["Subject"] == "":
		continue
	    else:
		has_subject.append(entry)

	travel_keywords = ["travel","voyage","ocean","transportation", "voyages","travels","railroad","railroads",
			    "business","steamboats","shipping","sailing"]
	education_keywords = ["school","college","haverford","education","college","university"]
	love_keywords = ["Love","love"]
	health_keywords = ["health","disease","diseases","fever","dysentery"]
	family_keywords = ["family","pets","death","vacation","deeds","suicide","housing","home","vacations"]
	religion_keywords = ["faith","quaker","quakers","quakerism","spiritual","spirituality","religious","religion","god","friends"]
	political_keywords = ["lincoln","event","government","pennsylvania","united","states","war","wars","politics","political"]
	lifestyle_keywords = ["children","clothes","dress","life","ornithology","letter","finance",
				"tax","music","dreams","land","nature","birthdays","birthday","weather",
				"outdoor","literature","sympathy","entertaining","child","letters","gossip",
				"trusts","legal","cards"]

	# The bins that will hold letters of different types
	travel_bin = []
	education_bin = []
	love_bin = []
	health_bin = []
	family_bin = []
	religion_bin = []
	political_bin = []
	lifestyle_bin = []
	unidentified = []

	max_age = ["0-10"]*8
	min_age = ["100-110"]*8
	ages = ["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100",""]
	age_count = []
	for x in range(8):
	    age_count.append([])
	    for y in range(11):
		age_count[x].append(0)

	for entry in has_subject:
	    # Clear out all of the punctuation from the entries
	    subjects = entry["Subject"].replace(";"," ")
	    subjects = subjects.replace(","," ")
	    subjects = subjects.replace("--"," ")
	    subjects = subjects.replace("COMMA"," ")
	    subjects = subjects.replace("("," ")
	    subjects = subjects.replace(")"," ")
	    # Split the string based on spaces now to get individual words
	    subjects = subjects.split(" ")
	    inBin = False
	    for word in subjects:
		word = word.lower()
		if word in travel_keywords and not entry in travel_bin:
		    travel_bin.append(entry)
		    try: 
			age_count[0][ages.index(entry["Age of Author"])] += 1
		    except:
			age_count[0][10] += 1

		    if entry["Age of Author"] > max_age[0]:
			max_age[0] = entry["Age of Author"]
		    if entry["Age of Author"] < min_age[0] and not entry["Age of Author"] == "":
			min_age[0] = entry["Age of Author"]
		    inBin = True	
		if word in education_keywords and not entry in education_bin:
		    education_bin.append(entry)
		    try: 
			age_count[1][ages.index(entry["Age of Author"])] += 1
		    except:
			age_count[1][10] += 1
		    if entry["Age of Author"] > max_age[1]:
			max_age[1] = entry["Age of Author"]
		    if entry["Age of Author"] < min_age[1] and not entry["Age of Author"] == "":
			min_age[1] = entry["Age of Author"]
		    inBin = True	
		if word in love_keywords and not entry in love_bin:
		    love_bin.append(entry)
		    try: 
			age_count[2][ages.index(entry["Age of Author"])] += 1
		    except:
			age_count[2][10] += 1
		    if entry["Age of Author"] > max_age[2]:
			max_age[2] = entry["Age of Author"]
		    if entry["Age of Author"] < min_age[2] and not entry["Age of Author"] == "":
			min_age[2] = entry["Age of Author"]
		    inBin = True	
		if word in health_keywords and not entry in health_bin:
		    health_bin.append(entry)
		    try: 
			age_count[3][ages.index(entry["Age of Author"])] += 1
		    except:
			age_count[3][10] += 1
		    if entry["Age of Author"] > max_age[3]:
			max_age[3] = entry["Age of Author"]
		    if entry["Age of Author"] < min_age[3] and not entry["Age of Author"] == "":
			min_age[3] = entry["Age of Author"]
		    inBin = True	
		if word in family_keywords and not entry in family_bin:
		    family_bin.append(entry)
		    try: 
			age_count[4][ages.index(entry["Age of Author"])] += 1
		    except:
			age_count[4][10] += 1
		    if entry["Age of Author"] > max_age[4]:
			max_age[4] = entry["Age of Author"]
		    if entry["Age of Author"] < min_age[4] and not entry["Age of Author"] == "":
			min_age[4] = entry["Age of Author"]
		    inBin = True	
		if word in religion_keywords and not entry in religion_bin:
		    religion_bin.append(entry)
		    try: 
			age_count[5][ages.index(entry["Age of Author"])] += 1
		    except:
			age_count[5][10] += 1
		    if entry["Age of Author"] > max_age[5]:
			max_age[5] = entry["Age of Author"]
		    if entry["Age of Author"] < min_age[5] and not entry["Age of Author"] == "":
			min_age[5] = entry["Age of Author"]
		    inBin = True	
		if word in political_keywords and not entry in political_bin:
		    political_bin.append(entry)
		    try: 
			age_count[6][ages.index(entry["Age of Author"])] += 1
		    except:
			age_count[6][10] += 1
		    if entry["Age of Author"] > max_age[6]:
			max_age[6] = entry["Age of Author"]
		    if entry["Age of Author"] < min_age[6] and not entry["Age of Author"] == "":
			min_age[6] = entry["Age of Author"]
		    inBin = True	
		if word in lifestyle_keywords and not entry in lifestyle_bin:
		    lifestyle_bin.append(entry)
		    try: 
			age_count[7][ages.index(entry["Age of Author"])] += 1
		    except:
			age_count[7][10] += 1
		    if entry["Age of Author"] > max_age[7]:
			max_age[7] = entry["Age of Author"]
		    if entry["Age of Author"] < min_age[7] and not entry["Age of Author"] == "":
			min_age[7] = entry["Age of Author"]
		    inBin = True

	    if not inBin:
		unidentified.append(subjects)
	
	return [travel_bin, education_bin, love_bin, health_bin, family_bin, religion_bin, political_vin, lifestyle_bin]

"""
The below code prints out the results of the above in a nice tabular format

total = len(travel_bin)+len(education_bin)+len(love_bin)+len(health_bin)+len(family_bin)+len(religion_bin)+len(political_bin)+len(lifestyle_bin)
print "BIN\t   |   LENGTH  |	MIN AGE	    |	MAX AGE"
print "travel:\t\t" + str(len(travel_bin))+"\t\t"+str(min_age[0])+"\t\t"+str(max_age[0])
print "education:\t" + str(len(education_bin))+"\t\t"+str(min_age[1])+"\t\t"+str(max_age[1])
print "love:\t\t" + str(len(love_bin))+"\t\t"+str(min_age[2])+"\t\t"+str(max_age[2])
print "health:\t\t" + str(len(health_bin))+"\t\t"+str(min_age[3])+"\t\t"+str(max_age[3])
print "family:\t\t" + str(len(family_bin))+"\t\t"+str(min_age[4])+"\t\t"+str(max_age[4])
print "religion:\t" + str(len(religion_bin))+"\t\t"+str(min_age[5])+"\t\t"+str(max_age[5])
print "political:\t" + str(len(political_bin))+"\t\t"+str(min_age[6])+"\t\t"+str(max_age[6])
print "lifestyle:\t" + str(len(lifestyle_bin))+"\t\t"+str(min_age[7])+"\t\t"+str(max_age[7])
print "---------------------------------------------"
print "Total:\t\t" + str(total)
print "---------------------------------------------"
print "unidentified:	 " + str(len(unidentified))
print "max_age: " + str(max_age)
print "min_age: " + str(min_age)
print
print "Distribution:"
print "\t\t0-10\t10-20\t20-30\t30-40\t40-50\t50-60\t60-70\t70-80\t80-90\t90-100\tunkown"
age_strings = []
for entry in age_count:
    temp = ""
    for item in entry:
	temp += str(item) + "\t"
    age_strings.append(temp)
print "travel:\t\t"+age_strings[0] 
print "education:\t"+age_strings[1]
print "love:\t\t"+age_strings[2]
print "health:\t\t" +age_strings[3]
print "family:\t\t" +age_strings[4]
print "religion:\t" +age_strings[5]
print "political:\t"+age_strings[6]
print "lifestyle:\t"+age_strings[7]
"""

"""
filename = "organized.csv"
headers = gd.get_headers()
gd.write_data_dicts(filename, headers, has_subject)
"""

