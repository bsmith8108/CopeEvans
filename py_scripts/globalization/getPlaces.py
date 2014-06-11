import get_data as gd

list_of_dicts = gd.get_data_list_of_dicts()

places_list = [{"decade":"1800","places":[], "letters":0},
	       {"decade":"1810","places":[], "letters":0},
	       {"decade":"1820","places":[], "letters":0},
	       {"decade":"1830","places":[], "letters":0},
	       {"decade":"1840","places":[], "letters":0},
	       {"decade":"1850","places":[], "letters":0},
	       {"decade":"1860","places":[], "letters":0},
	       {"decade":"1870","places":[], "letters":0},
	       {"decade":"1880","places":[], "letters":0},
	       {"decade":"1890","places":[], "letters":0},
	       {"decade":"1900","places":[], "letters":0},
	       {"decade":"1910","places":[], "letters":0},
	       {"decade":"unkown","places":[], "letters":0}
	      ]

place_lookup = {"80":0,
		"81":1,
		"82":2,
		"83":3,
		"84":4,
		"85":5,
		"86":6,
		"87":7,
		"88":8,
		"89":9,
		"90":10,
		"91":11,
		"unkown":12
		}

places = []
for entry in list_of_dicts:
    decade = "unkown"
    if len(entry["Date"]) > 4:
	decade = entry["Date"][1:3]
    try:
	index = place_lookup[decade]
    except:
	index = 12

    myPlaces = entry["Geographic Subjects"]
    myPlaces = myPlaces.split(";")
    places_list[index]["letters"] += 1
    for place in myPlaces:
	if not place in places:
	    places_list[index]["places"].append(place)
	    places.append(place)

print "Decade\tPlaces Mentioned\tNumber of Letters"
for entry in places_list:
    print entry["decade"] + "\t" + str(len(entry["places"]))+"\t"+str(entry["letters"])

