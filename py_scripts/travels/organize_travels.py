import get_data as gd
import json

list_of_dicts = gd.get_data_list_of_dicts()

travelers = []
for entry in list_of_dicts:
    if entry["Person"] in travelers:
	pass
    else:
	travelers.append(entry["Person"])

travelers_dicts = []
counter = 0
travelers_indices = {}
for item in travelers:
    travelers_dicts.append({"id":counter, "Person":item, "Trips":[]})
    travelers_indices[item] = counter
    counter += 1

for entry in list_of_dicts:
    i = travelers_indices[entry["Person"]]
    travelers_dicts[i]["Trips"].append({"Date":entry["Date"],"Place":entry["Destination"]})

json_string = json.dumps(travelers_dicts)

print json_string
