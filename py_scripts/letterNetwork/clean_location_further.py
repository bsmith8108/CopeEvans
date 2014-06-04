import get_data as gd

list_of_dicts = gd.get_data_list_of_dicts()

not_right = [
"Airdrie",
"Wildmere",
"Cherrelyn",
"CliffHouse",
"Lancaster",
"Awbury?",
"Awbury",
"NewCastle, Del.",
"Kingwood",
"Magnolia",
"WestonSchool",
"WashingtonSt.",
"Mulford",
"Lakewood ?",
"NorthEast ?",
"Overbrook",
"Wheeling, VA",
"Bloomsdale ?",
"LakeWindermere ?",
"SchoolLane",
"Overlook",
"Blythewood ?",
"CapeIsland, N.J.",
"Weston",
"SnowShoe ?",
"Lodore ?",
"LocustShade ?",
"Germantown ?",
"OceanHouse, CapeIsland",
"Connymeade?",
"6CavendishCrescent",
"LocustGrove, Rockway ?",
"MarbleheadNeck ?",
"Burtlington ?",
"ElizabethCitycounty, Va.",
"Asticou ?",
"FairHill, ArchStreet",
"Sunnyside, Mayfield",
"NewGarden",
"SchoolHouseLane",
"MeadowFarm",
"Keswick, Cumbria",
"LaurelHouse",
"Fellsworth",
"Bristol",
"Connymede",
"HighlandHouse",
"MauchChurch ?",
"DevonInn",
"11PlaceReineMathilde",
"MapleShade, Odessa",
"London;Paris",
"NewGardenBoardingSchool",
"NewGardenBoardingSchool, N.C.",
"BlissCottage",
"SurfHouse",
"SurfHaven",
"WestChester, Pa.",
"ProspectSt.",
"2ndBeach, Newport",
"Mossgiel, R.I.",
"Mossgiel"
]
print len(not_right)
not_right_clean = [] 
for entry in not_right:
    not_right_clean.append(entry.replace(" ?",""))
right = []
counter = 0
left_out = []
for entry in list_of_dicts:
    if entry["Name"] in not_right_clean:
	counter += 1
	left_out.append(entry["Name"])
    else:
	right.append(entry)

print counter

for entry in not_right_clean:
    if entry in left_out:
	continue
    else:
	print entry

filename = "partialCurrectLocations.csv"
headers = gd.get_headers()
gd.write_data_dicts(filename,headers,right)

