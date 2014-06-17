import get_data as gd
import makeTrainingData as td
import classify as cl

while(True):
    words = raw_input("Enter a comma separated list of\nwords you would like to test:")
    words = words.replace(" ", "")
    words = words.split(",")

    # get_data.py should grab the data from transcriptsNoDups.csv
    # Makes the training data list and puts it into trainingData.csv
    # Puts the full word frequency count in fullData.csv
    td.makeTrainingData(words)

    # get_data2.py should grab the data from fullData.csv
    # get_data3.py should grab the data from trainingData.csv
    result = cl.test()
    print "Accuracy: " + str(result[0])
    print "Within 2 decades: " + str(result[1])
    print
