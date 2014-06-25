from pygeocoder import Geocoder
import get_data as gd

############ Open up the locations file and save it ############
f = open("places.txt","r")
places = f.read()
f.close()

###############################################################

places = places.split("\n")
final = []

for entry in places:
    temp = {}
    temp["Place"] = entry
    try:
	result = Geocoder.geocode(name)
	temp["Latitude"] = result[0].coordinates[0]
	temp["Longitude"] = result[0].coordinates[1]
	final.append(temp)
    except:
	print "NOPE: " + entry

filename = "travelLocations.csv"
headers = ["Name","Latitude","Longitude"]

gd.write_data_dicts(filename, headers, final)
