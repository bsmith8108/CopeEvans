import get_data as gd
import re

list_of_dicts = gd.get_data_list_of_dicts()

exclude = ["Cope","Elizabeth","Aunt","Uncle","I","Brother","Where","Dear","Howell",
	    "Yarnall","Tell","Cousin","Anna","Hannah","Williams","Alfred","Carry",
	    "Ellie","Rico","Elisabeth","Henry","Evans","Brown","Evans.","Frank",
	    "Samuel","Dr","My","On","Eleanor","Newport","Aug","Love","Dr.","We",
	    "Allan","Copes","E","Jr","Francis","Stokes","Both","With",""]

include = ["Imperial", "Dictionary", "Colored","Summer","Rose","Island"]
names = []
errors = 0
entryCounter = 0
for entry in list_of_dicts:
    t = entry["Transcript"]
    t = t.split(" ")
    counter = 0
    names.append("################## Transcript " + str(entryCounter) + " ##############")
    entryCounter += 1
    for x in range(len(t)):
	t[x] = t[x].replace("COMMA", "")
	t[x] = t[x].replace("<br>", "")
	try:
	    if t[x][0].isupper():
		counter += 1
	    else:
		counter = 0
	    
	    if counter == 2 and not (t[x-1] in exclude) and not (t[x] in exclude) and len(t[x-1]) > 2 and len(t[x]) > 2:
		names.append(t[x-1] + " " + t[x])
		counter = 0
	except:
	    errors += 1
    
for item in names:
    print "\""+ item +"\""

print "Names: " + str(len(names))
print "Errors:\t" + str(errors)
