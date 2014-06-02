import get_data as gd
import get_subjects as gs

list_of_dicts = gd.get_data_list_of_dicts()
subject_split = gs.get_subjects(list_of_dicts)[:-1]
final = ""

counter = 0
subjects = ["TRAVEL","EDUCATION","LOVE", "HEALTH","FAMILY","RELIGION","POLITICAL", "LIFESTYLE"]
for subject in subject_split:
    final += subjects[counter] + "\n\n"
    counter += 1 
    for letter in subject:
	try:
	    final += "--------------------------------------------------------"
	    final += "Creator: " + letter["Creator"] + "\n"
	    final += "Recipient: " + letter["Recipient"] + "\n"
	    final += "Date: " + letter["Date"] + "\n"
	    final += "Title: " + letter["Title"].replace("COMMA",",") + "\n\n"
	    transcript = letter["Transcript"].replace("COMMA",",") + "\n\n"
	    transcript = transcript.replace("<br>","\n")
	    final += transcript
	    final += "--------------------------------------------------------"
	except:
	    continue

print final


