import get_data as gd

list_of_dicts = gd.get_data_list_of_dicts()
final = []

for entry in list_of_dicts:
    if entry["Transcript"] != "":
	final.append(entry)

filename = "justTranscripts.csv"
headers = gd.get_headers()
gd.write_data_dicts(filename, headers, final)
	
