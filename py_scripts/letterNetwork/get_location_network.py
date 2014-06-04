import get_data as gd
import get_data2 as gd2
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

has_both = []
for entry in list_of_dicts:
    if not (entry["Place Of Origin"] == "") and not (entry["Destination"] == ""):
	has_both.append(entry)

list_of_places = gd2.get_data_list_of_dicts()

places = []
for entry in list_of_places:
    places.append(entry["Name"])

has_full = []
for item in has_both:
    # Have to clean the name so it will match the one we have listed
    # for the places
    Poo = item["Place Of Origin"].replace(" ","")
    Poo = Poo.replace("(","COMMA")
    Poo = Poo.replace(")","COMMA")
    Poo = Poo.split("COMMA")
    Poo2 = []
    for word in Poo:
	if not word == "":
	    Poo2.append(word)
    Poo = Poo2[:]
    if len(Poo) == 1:
	Poo = Poo[0]
    else:
	Poo = Poo[0] +", "+Poo[1]
	
    Dest = item["Destination"].replace(" ","")
    Dest = Dest.replace("(","COMMA")
    Dest = Dest.replace(")","COMMA")
    Dest = Dest.split("COMMA")
    Dest2 = []
    for word in Dest:
	if not word == "":
	    Dest2.append(word)
    Dest = Dest2[:]
    if len(Dest) == 1:
	Dest = Dest[0]
    else:
	Dest = Dest[0] +", "+Dest[1]

    if Poo in places and Dest in places:
	has_full.append({"Poo":places.index(Poo),"Dest":places.index(Dest), "Letter":item})

filename="letterTravels.csv"
headers = ["Poo","Dest","Letter"]
gd.write_data_dicts(filename,headers,has_full)
