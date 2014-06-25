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
{"Cope Member": ...,
 "Partner": ...,
 "Partner Parents": [...],
 "Children": [
    {"Cope Member": ...,
     "Partner": ...,
     "Partner Parents": ...,
     "Children": [
     ...
     ]
    }
    {"Husband": ...

    }
    ...
 ]
}
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
root = {"Cope Member":startCope["Name"],"Partner":startCope["Partner"],"children":[]}
info = startCope
used = [] # To know whether or not a person can be placed in the tree again

print copeLookup["Caleb Cope"]
def findChildren(root, info):
    for child in info["Children"]:
	copeParent = re.sub(r'[^a-zA-Z]',' ', root["Cope Member"])
	copeParent = copeParent.replace(" ", "")
	otherParent = re.sub(r'[^a-zA-Z]',' ', root["Partner"])
	otherParent = otherParent.replace(" ", "")
	child_info = getInfo([copeParent, otherParent], child)
	# print child
	if len(child_info) == 1:
	    child_info = child_info[0]
	    if not child_info["id"] in used:
		child_object = {"Cope Member":child_info["Name"],"Partner":child_info["Partner"],"children":[]}
		used.append(child_info["id"])
		root["children"].append(findChildren(child_object,child_info))
	else:
	    for marriage in child_info:
		if not marriage["id"] in used:
		    child_object = {"Cope Member":marriage["Name"],"Partner":marriage["Partner"],"children":[]}
		    used.append(marriage["id"])
		    # print used
		    root["children"].append(findChildren(child_object,marriage))
	
    return root

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
    
final = findChildren(root, info)
print len(used)
f = open("familytree.json","w")
json.dump(final,f, indent=2)
f.close()
