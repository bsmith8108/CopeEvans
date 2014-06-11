import get_data as gd

list_of_dicts = gd.get_data_list_of_dicts()

identifiers = []
final = []
for entry in list_of_dicts:
    if entry["Identifier"] in identifiers:
	continue
    else:
	final.append(entry)
	identifiers.append(entry["Identifier"])

filename = "transcriptsNoDups.csv"
headers = gd.get_headers()
gd.write_data_dicts(filename, headers, final)
	
