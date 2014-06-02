import get_data as gd
import sys


# Now that we have the list of people connected with who they sent
# a letter to, we can calculate PageRank
# Parts of code taken from Brandon Smith's kdtree.py file
class Point:
    def __init__(self, person):
	self.name = person[0]
	self.my_id = person[1]
	self.pagerank = 0
    
    def __str__(self):
	return str(self.my_id)
    
    def __repr__(self):
	return str(self.my_id)

    def getId(self):
	return int(self.my_id)
    
    def getName(self):
	return self.name

    def setPageRank(self, val):
	self.pagerank = val

def make_points(people):
    points = []
    counter = 0
    for person in people:
        temp = [person,counter]
	temp_point = Point(temp)
	points.append(temp_point)
	counter += 1

    return points

def pageRank(nn_list, points):
    pageRanks = []
    newPageRanks = []
    InNodesList = []
    N = len(points)
    starter = 1.0/N
    oldPageRanks = []
    d = .85
    constant = (1.0-d)/N

    # initialize the page ranks list to the same initial values
    for x in range(len(points)+1):
	pageRanks.append(starter)
	oldPageRanks.append(0.0)
	InNodesList.append([])
    
    # need to find what nodes are pointing to what other nodes
    # once I have this, it will be a constant time lookup to find
    # In(u)
    for entry in nn_list:
	for item in entry["target"]:
	    InNodesList[item.getId()].append(entry["source"])
    """
    Code from original PageRank function, modified for my use above
    for entry in range(len(nn_list)):
	for item in nn_list[entry]["target"]:
	    InNodesList[item.getId()].append(points[entry])
	    InNodesList[entry].append(item)
    """
    counter = 0
    while not (oldPageRanks == pageRanks) and counter <=100:
	counter += 1
	for i in range(len(points)):
	    """
	    Page Rank:
		PageRank(point) = (1-d)/N + d*Sum(PR(v)/Out(v))
		for all v coming into the point
	    """
	    final = constant
	    summation = 0.0
	    InPoints = InNodesList[i]
	    for j in range(len(InPoints)):
		PR_v = pageRanks[InPoints[j].getId()]
		Out_v = len(InNodesList[InPoints[j].getId()])
		if Out_v == 0:
		    Out_v = len(points)-1
		summation = summation + (PR_v/Out_v)
	    summation = summation*d
	    final = final + summation
	    # This just makes sure it doesn't take forever to converge
	    final = float('%.5f'%(final))
	    newPageRanks.append(final)
	oldPageRanks = pageRanks[:]
	pageRanks = newPageRanks[:]
	newPageRanks = []

    return pageRanks

def find_point(name, points):
    for p in points:
	if name == p.getName():
	    return p
    sys.exit("Could not find point")

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

# Make the list of people into points
people = make_points(people)

# Look through the list of people and connect them to make the network
creator_recipient_list = []
creators_list = []
creator_lookup = {}
# Make a list of all the people who have written a letter
for entry in list_of_dicts:
    creator = entry["Creator"].replace(" ","")
    creator_point = find_point(creator,people)
    if not creator_point in creators_list:
	creators_list.append(creator_point)
# Make a dictionary with the people who have created a letter and
# then a list of the people they have written to
lookup_counter = 0
for person in creators_list:
    creator_recipient_list.append({"source":person, "target":[]})
    creator_lookup[person.getName()] = lookup_counter
    lookup_counter += 1
# Add the list of people that the person has written to
for entry in list_of_dicts:
    index = creator_lookup[entry["Creator"].replace(" ","")]
    creator_recipient_list[index]["target"].append(find_point(entry["Recipient"].replace(" ",""),people))


page_ranks = pageRank(creator_recipient_list,people)

json_string = "{\"nodes\":[\n"

counter = 0
for person in people:
    json_string += "{\"name\":\""+person.getName().replace("\"","'")+"\", \"pageRank\":"+str(page_ranks[counter])+"},\n"
    counter += 1

json_string += "],\n\"links\": [\n"

for item in creator_recipient_list:
    for target in item["target"]:
	json_string += "{\"source\":" + str(item["source"].getId()) + ", \"target\":" + str(target.getId()) + "},\n"
    
json_string += "]\n}"

print json_string
