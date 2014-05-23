import get_data as gd
import get_transcripts as gt

list_of_dicts = gd.get_data_list_of_dicts();

temp = []

transcripts = gt.get_full_transcripts()

for entry in list_of_dicts:
    entry["Transcript"] = transcripts[entry["Identifier"]]

for entry in list_of_dicts:
    if entry["Creator"] == "" or entry["Recipient"] == "" or entry["Creator"] == "Unknown":
	continue
    else:
	temp_string = entry["Recipient"].split(";")
	for i in temp_string:
	    if not i == "":
		my_dict = entry.copy()
		person = i.split("COMMA")
		if len(person) == 2:
		    person = person[1] + " " + person[0]
		elif len(person) == 3:
		    person = person[1] + " " + person[0] + ": " + person[2]
	
		my_dict["Recipient"] = person
		temp.append(my_dict)	    

headers_wanted = ["Title","Date","Creator","Identifier","Recipient", "Gender of Author","Age of Author","Identified People","Unidentified People","Subject","Geographic Subjects","Place Of Origin","Destination","Notes","Language","Transcript","Reference URL","CONTENTdm number","CONTENTdm file name"]

final = []
for entry in temp:
    temp_dict = {}
    for key in entry.keys():
	if key in headers_wanted:
	    temp_dict[key]=entry[key]
    final.append(temp_dict)

headers = headers_wanted
file_name = "Recipient_and_Creator_cleaned2.csv"
gd.write_data_dicts(file_name, headers, final)
