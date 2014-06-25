
	copeParent = re.sub(r'[^a-zA-Z]',' ', root["Cope Member"])
	copeParent = copeParent.split(" ")
	if len(copeParent) == 1 or len(copeParent) == 2:	
	    copeParent = copeParent[0]
	elif len(copeParent) == 0:
	    copeParent = " "
	else:
	    copeParent = copeParent[0]+copeParent[2]
	try:
	    myID = copeID[copeParent]
	    copeID[copeParent] += 1
	except:
	    myID = 1
	    copeID[copeParent] = 2
	# Get the Partner Name
	otherParent = re.sub(r'[^a-zA-Z]',' ', root["Partner"])
	otherParent = otherParent.split(" ")
	if len(otherParent) == 1 or len(otherParent) == 2:	
	    otherParent = otherParent[0]
	elif len(otherParent) == 0:
	    otherParent = " "
	else:
	    otherParent = otherParent[0]+otherParent[2]
