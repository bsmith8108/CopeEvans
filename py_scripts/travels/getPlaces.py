import get_data as gd
from pygeocoder import Geocoder

places = "Newport, ME:Mount Desert, ME:Bar Harbor, ME:Franconia:Lake Winnipisseogee, NH:Lake Placid, NY:Caldwell Lake George, NY:Catskills, NY:Boston, MA:WestPoint, NY:Hopatcong, NJ:Philadelphia, PA:Washington D.C.:Sulfur Springs, WV:Sweet Springs, WV:Lynchburg, VA:Farmville, VA:Chalybeate Springs, NC:Charleston, SC:Oban, Scotland:Edinborough, Scotland:Lake Windermere, England:Liverpool, England:Ashbourne, England:London, England:Avebury, England:The Hague, Netherlands:Paris, France:Cannes, France:Mentone/Menton, France:Florence, Italy:Camaldoli, Italy:Rome, Italy:Lugano, Switzerland:Venice, Italy:Frohburg, Germany:Reichenbach, Germany"

places = places.split(":")
locations = {}
counter = 0
error = 0
for place in places:
    try:
        result = Geocoder.geocode(place)
        locations[place] = result[0].coordinates
    except:
        error += 1
        print "NOPE: " + name

    counter += 1

print "Errors: " + str(error)

final = []

for place in locations.keys():
  temp = {"place":place, "latitude":locations[place][0], "longitude":locations[place][1]}
  final.append(temp)

filename = "place_coordinates.csv"
headers = ["place", "latitude", "longitude"]
gd.write_data_dicts(filename, headers, final)
