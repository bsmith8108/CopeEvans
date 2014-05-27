import get_data as gd

data = gd.get_data_list_of_dicts()

for x in data:
    print x["Destination"]
