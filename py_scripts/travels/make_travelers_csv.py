import get_data as gd

f = open("travels.txt","r")

line = f.readline()

temp_lines = []
final = []
while not line == "":
    temp_lines.append(line)
    line = f.readline()

for item in temp_lines:
    if item == "\n":
	pass
    else:
	item = item.replace("\n","")
	final.append(item)

final_dicts = []
for entry in final:
    temp_list = entry.split(",")
    temp_dict = {}
    
    # Create a dictionary with the person, where they are and at what
    # time
    temp_dict["Person"] = temp_list[0]
    temp_dict["Date"] = temp_list[1] + " " + temp_list[2]
    temp_destination = temp_list[3].replace(" ","")
    temp_dict["Destination"] = temp_destination
    """
    This is to get the full information, but all we need are the cities
    for x in temp_list[3:]:    
	temp_dict["Destination"] += " " + x
    """
    
    # Then append it to the final list of dicts
    final_dicts.append(temp_dict)


headers = ["Person", "Date", "Destination"]
filename = "travelers_cities.csv"
gd.write_data_dicts(filename,headers, final_dicts)
