import get_data as gd

list_of_dicts = gd.get_data_list_of_dicts()
final = []

for entry in list_of_dicts:
    if entry["date"] == "":
	pass
    else:
	try:
	    int(entry["recipient"][0])
	except:
	    final.append(entry)

final = sorted(final,key=lambda k: k["date"])

counter = 1
for entry in final:
    entry["id"]=counter
    counter+=1
    
filename = "letters_list.csv"
headers = ["id","date","recipient","creator"]
gd.write_data_dicts(filename, headers, final)
