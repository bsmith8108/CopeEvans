import get_data as gd
from pygeocoder import Geocoder

list_of_dicts = gd.get_data_list_of_dicts()
places = []

for entry in list_of_dicts:
    PoO = entry["Place Of Origin"].replace(" ", "")
    dest = entry["Destination"].replace(" ", "")
    if len(PoO) > 1 and not PoO in places:
	places.append(PoO)
    if len(dest) > 1 and not dest in places:
	places.append(dest)
new_places = []
for place in places:
    place = place.replace("(","COMMA")
    place = place.replace(")","COMMA")
    place = place.split("COMMA")
    place2 = []
    for word in place:
	if not word == "":
	    place2.append(word)
    place = place2[:]
    new_places.append(place)

place_names = []
for entry in new_places:
    name = "";
    if len(entry) == 1:
	name = entry[0]
    if len(entry) >= 2:
	name = entry[0] +", "+entry[1]
    place_names.append(name)

locations = {}
counter = 0
error = 0
for place in new_places:
    name = "";
    if len(place) == 1:
	name = place[0]
    if len(place) >= 2:
	name = place[0] +", "+place[1]
    try:
	result = Geocoder.geocode(name)
	locations[place_names[counter]] = result[0].coordinates
    except:
	error += 1
	print "NOPE: " + name

    counter += 1

print "Errors: " + str(error)

final = []
for loc in locations.keys():
    print locations[loc][1]
    temp = {}
    temp["Name"] = loc
    temp["Latitude"] = locations[loc][0]
    temp["Longitude"] = locations[loc][1]
    final.append(temp)

filename = "letterLocation.csv"
headers = ["Name","Latitude","Longitude"]
gd.write_data_dicts(filename, headers, final)
