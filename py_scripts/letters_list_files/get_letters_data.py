import urllib2
import get_data as gd


# Since there are 16 different pages that have the information
# that have the information we need, we need to rotate through all
# of the urls
url_list = [0]*17
def get_page_data(page_number):
	##### Get the raw HTML #####
	file_source = "page_sources/page"+str(page_number)
	my_file = open(file_source,"r")
	source = my_file.read()
	my_file.close()

	###########################
	##### Parse Through the html string for the sections we want #####
	i = 0
	raw_list = []

	while i < len(source):
	    if source[i:i+35] == "<div class=\"marginTopTextAdjuster\">": #Every field of information that we want is stored in a certain div
		temp = ""
		counter=i+35
		while not source[counter] == "<":
		    temp = temp + source[counter]
		    counter+=1

		raw_list.append(temp)
		i += 35
	    elif source[i:i+18] == "class=\"body_link_11\"":
		print "here"
	    else:
		i+=1

	counter = 0
	item = 0
	final_dicts =[]
	while counter < len(raw_list):
	    if counter%3 == 0:
		final_dicts.append({})
		final_dicts[counter//3]["creator"] = raw_list[item]
		counter += 1
		item += 1
	    elif counter%3 == 1:
		final_dicts[counter//3]["recipient"] = raw_list[item]
		counter += 1
		item += 1
	    elif counter%3 == 2:
		is_int = 0
		try:
		    is_int = int(raw_list[item][0])
		except:
		    is_int = -1
		
		if is_int >= 0:
		    final_dicts[counter//3]["date"] = raw_list[item]
		    counter += 1
		    item += 1
		else:
		    final_dicts[counter//3]["date"] = "unknown"
		    counter +=1
		

	return final_dicts

list_of_dicts = []

for x in range(1,17):
    print x
    temp = get_page_data(x)
    if temp == list_of_dicts:
	print "what"
    else:
	list_of_dicts = list_of_dicts + temp

filename = "letters_list.csv"
headers = ["date","recipient","creator"]
gd.write_data_dicts(filename, headers, list_of_dicts)
