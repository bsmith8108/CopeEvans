import get_data as gd

file_full = open("export.txt","r")
file_text = file_full.read()
file_full.close()

file_text = file_text.replace(",", "COMMA")
file_text = file_text.replace("\t",",")

print file_text
