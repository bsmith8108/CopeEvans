import get_data as gd
import sys
import os
import re
from bs4 import BeautifulSoup
import json
""""
Data Structure:

{"Name": ..., "Parents":[...], "Children":[...], "Info":{...}, "Partner": ...}
-if Couple is true, parents is just a list of the two peoples names
-if Couple is true, Name is husband name + " and " + wife name
"""

filename = "peopleFiles/"
files = ["wc04_","wc05_","wc08_","wc36_","wc37_"]
people = {} #povides the index of each person's data withn the people_data list
people_data = [] # stores the dictionaries of everybody's data
counter = 0 # for the indices of the people
for entry in files:
    files_current = []
    for f in os.listdir('peopleFiles/'):
	if re.search(entry, f):
	    files_current.append(f)

    for item in files_current:
	myFile = open(filename+item,"r")
	raw_html = myFile.read()
	myFile.close()
	parsed_html = BeautifulSoup(raw_html)
	try:
	    husband_father = parsed_html.body.find('span', attrs={'class':'wcHFather'}).text
	except:
	    husband_father = ""

	try:
	    husband_mother = parsed_html.body.find('span', attrs={'class':'wcHMother'}).text
	except:
	    husband_mother = ""
	try:
	    wife_father = parsed_html.body.find('span', attrs={'class':'wcWFather'}).text
	except:
	    wife_father =""
	try:
	    wife_mother = parsed_html.body.find('span', attrs={'class':'wcWMother'}).text
	except:
	    wife_mother = ""
	try:
	    husband = parsed_html.body.find('div', attrs={'class':'wcHusbandWrapper'}).text
	except:
	    husband = ""
	try:
	    wife = parsed_html.body.find('div', attrs={'class':'wcWifeWrapper'}).text
	except:
	    wife = ""
	try:
	    children_list = []
	    children = parsed_html.body.find_all('span', attrs={'class':'wcChildName'})
	    for child in children:
		children_list.append(child.text)
	except:
	    children_list = []
	wife_data = {"Name":wife,"Parents":[wife_father,wife_mother],"Children":children_list, "Partner":husband}
	husband_data = {"Name":husband,"Parents":[husband_father,husband_mother],"Children":children_list, "Partner":wife}
	people_data.append(wife_data)
	people[wife] = counter
	counter += 1
	people_data.append(husband_data)
	people[husband] = counter
	counter += 1

"""
This was used to check that actually grabbing all of the data worked


for person in people.keys():
    print person

Now I have to construct the tree/graph structure to connect up the whole family
"""

copeFamily = []
copeLookup = {}

counter = 0
for entry in people_data:
    isCope = False
    try:
	temp = entry["Name"].index("Cope")
	isCope = True
    except:
	isCope = False
    
    if isCope:
	copeFamily.append(entry)
	try:
	    entry["id"] = counter
	    copeLookup[entry["Name"]].append(entry)
	    counter += 1
	except:
	    entry["id"] = counter
	    copeLookup[entry["Name"]] = [entry]
	    counter += 1

startCope = []
for cope in copeFamily:
    if cope["Parents"][0] == "":
	startCope.append(cope)

startCope = startCope[0]
root = [{"v":startCope["Name"] + str(1), "f":startCope["Name"]+"<div class=\"partner\">"+startCope["Partner"] +"</div>"},None,None]
info = startCope
used = [] # To know whether or not a person can be placed in the tree again
finalFamily = []
finalFamily.append(root)
copeID = {}
copeID["John Cope"] = 2

def findChildren(info, parentName):
    for child in info["Children"]:
	copeParent = re.sub(r'[^a-zA-Z]',' ', info["Name"])
	copeParent = copeParent.replace(" ", "")
	otherParent = re.sub(r'[^a-zA-Z]',' ', info["Partner"])
	otherParent = otherParent.replace(" ", "")
	child_info = getInfo([copeParent, otherParent], child)
	if len(child_info) == 1:
	    child_info = child_info[0]
	    copeParent = re.sub(r'[^a-zA-Z]',' ', child_info["Name"])
	    copeParent = copeParent.split(" ")
	    if len(copeParent) == 1 or len(copeParent) == 2:	
		copeParent = copeParent[0]
	    elif len(copeParent) == 0:
		copeParent = " "
	    else:
		copeParent = copeParent[0]+copeParent[2]
	    
	    if not child_info["id"] in used:
		try:
		    myID = copeID[copeParent]
		    copeID[copeParent] += 1
		except:
		    myID = 1
		    copeID[copeParent] = 2
		child_object = [{"v":child_info["Name"] + str(myID), "f":child_info["Name"]+"<div class=\"partner\">"+child_info["Partner"] +"</div>"},parentName,None]
		used.append(child_info["id"])
		finalFamily.append(child_object)
		findChildren(child_info, child_info["Name"] +str(myID))
	else:
	    for marriage in child_info:
		copeParent = re.sub(r'[^a-zA-Z]',' ', marriage["Name"])
		copeParent = copeParent.split(" ")
		if len(copeParent) == 1 or len(copeParent) == 2:	
		    copeParent = copeParent[0]
		elif len(copeParent) == 0:
		    copeParent = " "
		else:
		    copeParent = copeParent[0]+copeParent[2]
		
		if not marriage["id"] in used:
		    try:
			myID = copeID[copeParent]
			copeID[copeParent] += 1
		    except:
			myID = 1
			copeID[copeParent] = 2
		    child_object = [{"v":marriage["Name"] + str(myID), "f":marriage["Name"]+"<div class=\"partner\">"+marriage["Partner"] +"</div>"},parentName,None]
		    used.append(marriage["id"])
		    finalFamily.append(child_object)
		    findChildren(marriage, marriage["Name"] +str(myID))

def getInfo(p, name):
    try:
	index = copeLookup[name]
    except:
	print "not a Cope: " + name
	return []
    final = []
    if len(index) > 1:
	for item in index:
	    for parent in item["Parents"]:
		parent = [a for a in re.split(r'([A-Z][a-z]*)', parent) if a]
		# print "Parent list: " + str(parent)
		if len(parent) == 1 or len(parent) == 2:
		    parent = parent[0]
		elif len(parent) == 0:
		    parent = " "
		else:
		    parent = parent[0]+parent[2]
		parent = re.sub(r'[^a-zA-Z]',' ', parent)
		parent = parent.replace(" ", "")
		# print "actual parents: \"" + p[1] + "\" \""+ p[0] + "\""
		# print "search parent: \"" + parent + "\""
		if parent == p[0] or parent == p[1]:
		    final.append(item)
    else:
	return index

    return final
    
findChildren(info,startCope["Name"] + str(1)) 

print len(used)
f = open("familyTreeCope.json","w")
json.dump(finalFamily,f, indent=2)
f.close()
