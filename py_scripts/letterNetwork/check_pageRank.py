import get_data as gd

list_of_dicts = gd.get_data_list_of_dicts()

counter = 0
for entry in list_of_dicts:
    creator = entry["Creator"].replace(" ", "")
    recipient = entry["Recipient"].replace(" ", "")
    if creator == "RachelReeveCopeEvans:1850-1939" or recipient == "RachelReeveCopeEvans:1850-1939":
	counter += 1

print counter
