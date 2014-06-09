import get_data as gd

list_of_dicts = gd.get_data_list_of_dicts()

def getYear(year):
    year = year.split("-")
    year = year[0]
    return year

final = {}
for entry in list_of_dicts:
    year = getYear(entry["Date"])
    try:
	final[year] += 1
    except:
	final[year] = 1

list_of_lists = []
for item in sorted(final.keys()):
    list_of_lists.append([item,final[item]])

headers = ["year","letters"]
filename = "year_letter.csv"
gd.write_data(filename, headers, list_of_lists)
