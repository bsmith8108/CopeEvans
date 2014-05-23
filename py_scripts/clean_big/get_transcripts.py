import get_data as gd

def get_full_transcripts():
    list_of_dicts = gd.get_data_list_of_dicts()

    final = {}
    identifiers = []

    for entry in list_of_dicts:
	if not entry["Identifier"] in identifiers:
	    identifiers.append(entry["Identifier"])
	    final[entry["Identifier"]] = [entry]
	else:
	   final[entry["Identifier"]].append(entry)

    for i in final.keys():
	final[i] = sorted(final[i], key= lambda k: k['Title'])

    transcripts = {}

    for entry in final.keys():
	temp_string = ""
	for item in final[entry]:
	    temp_string += item["Transcript"]
	transcripts[entry] = temp_string

    return transcripts
