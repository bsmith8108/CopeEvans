import get_data as gd
import json

list_of_dicts = gd.get_data_list_of_dicts()

temp = []
for entry in list_of_dicts:
    if not entry["recipient"] in temp:
	temp.append(entry["recipient"])
    if not entry["creator"] in temp:
	temp.append(entry["creator"])

counter = 0
nodes = []
for entry in temp:
    nodes.append([counter,entry])
    counter += 1

def lookup(name):
    for entry in nodes:
	if name == entry[1]:
	    return entry[0]

links = []
for entry in list_of_dicts:
    recipient_id = lookup(entry["recipient"])
    creator_id = lookup(entry["creator"])
    links.append([creator_id,recipient_id])
    

json_string = "{\"nodes\":["

for node in nodes:
    json_string = json_string+"\n{\"name\":\""+node[1]+"\"},"

json_string = json_string+"],\n\"links\":["

for link in links:
    json_string = json_string+"\n{\"source\":"+str(link[0])+", \"target\":"+str(link[1])+"},"

json_string = json_string+"]\n}"

print json_string
