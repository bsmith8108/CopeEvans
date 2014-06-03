import get_data as gd

list_of_dicts = gd.get_data_list_of_dicts()

list_of_dicts = sorted(list_of_dicts, key=lambda k : k["Date"])

counter = 0
for entry in list_of_dicts:
    creator = entry["Creator"].replace(" ", "")
    recipient = entry["Recipient"].replace(" ", "")
    if (creator == "AnnaStewardsonBrownCope:1822-1916" or recipient == "AnnaStewardsonBrownCope:1822-1916") and len(entry["Transcript"]) >= 10:
	counter += 1
	print "\n-------------------------------------------------------"
	transcript = entry["Transcript"].replace("<br>","\n")
	transcript = transcript.replace("COMMA",",")
	print transcript
	print "\n------------------------------------------------------"

print counter
