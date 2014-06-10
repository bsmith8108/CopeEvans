import get_data as gd
import get_subjects as gs

list_of_dicts = gd.get_data_list_of_dicts()
subject_list = gs.get_subjects(list_of_dicts)

def getYear(year):
    year = year.split("-")
    year = year[0]
    return year

def getFullCount():
    final = {}
    for entry in list_of_dicts:
	year = getYear(entry["Date"])
	try:
	    final[year] += 1
	except:
	    final[year] = 1

    list_of_lists = []
    for item in sorted(final.keys()):
	list_of_lists.append([item,final[item]])

    return list_of_lists

def getSubjectCount():
    final = []
    subjects = ["Travel","Education","Love","Health","Family","Religion","Political","Lifestyle","Unidentified"]
    for subject in subjects:
	final.append({"subject":subject,"yearDate": {}})
    
    counter = 0
    for entry in subject_list:
	for letter in entry:
	    year = getYear(letter["Date"])
	    try:
		final[counter]["yearDate"][year] += 1
	    except:
		final[counter]["yearDate"][year] = 1
	
	counter += 1

    return final


def makeSubjectCsv(subjects_sorted):
    final = []
    yearLookup = {}
    subjects = ["Travel","Education","Love","Health","Family","Religion","Political","Lifestyle","Unidentified"]
    
    counter = 0
    for x in range(1800,1912):
	final.append({"year":x})
	for subject in subjects:
	    final[counter][subject] = 0
	yearLookup[x] = counter
	counter += 1

    for entry in subjects_sorted:
	mySub = entry["subject"]
	for year in entry["yearDate"].keys():
	    if not year == '':
		try:
		    index = yearLookup[int(year)]
		    final[index][mySub] = entry["yearDate"][year]
		except:
		    print year
	
    headers = ["year","Travel","Education","Love","Health","Family","Religion","Political","Lifestyle","Unidentified"]
    filename = "subject_year.csv"
    gd.write_data_dicts(filename,headers,final)


temp = getSubjectCount()
makeSubjectCsv(temp)
