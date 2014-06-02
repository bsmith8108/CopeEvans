import get_data as gd

list_of_dicts = gd.get_data_list_of_dicts()

# Add an id number so that data will work with force directed graph
counter = 0
for entry in list_of_dicts:
    entry["id"] = counter
    counter += 1

# Checking the number of people and getting a full list of people
people = []
for entry in list_of_dicts:
    creator = entry["Creator"].replace(" ","")
    recipient = entry["Recipient"].replace(" ","")
    if not creator in people:
	people.append(creator)
    if not recipient in people:
	people.append(recipient)

# Look through the list of people and connect them to make the network
creator_recipient_list = []
creators_list = []
creator_lookup = {}
for entry in list_of_dicts:
    creator = entry["Creator"].replace(" ","")
    if not creator in creators_list:
	creators_list.append(creator)

lookup_counter = 0
for person in creators_list:
    creator_recipient_list.append({"source":person, "target":[]})
    creator_lookup[person] = lookup_counter
    lookup_counter += 1

for entry in list_of_dicts:
    index = creator_lookup[entry["Creator"].replace(" ","")]
    creator_recipient_list[index]["target"].append(entry["Recipient"])

# Now that we have the list of people connected with who they sent
# a letter to, we need to export it to a json file
