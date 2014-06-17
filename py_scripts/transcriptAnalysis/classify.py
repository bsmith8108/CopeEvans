import get_data2 as gd2
import get_data3 as gd3
import numpy as np

def getDataSet(c, data):
    final = []
    for entry in data:
	try:
	    if entry["class"] == c:
		final.append(entry)
	except:
	    #print "ERROR: no class field: " + str(entry)
	    continue
    
    return final

def makeDictMatrix(D):
    final = []
    for entry in D:
	temp = []
	entry.pop("class",None)
	for item in entry.keys():
	    if not entry[item] == "":
		temp.append(int(entry[item]))
	    else:
		temp.append(0)

	# print "temp: " + str(temp)
	final.append(temp)
	# print "final: " + str(final)
    
    final = np.matrix(final)
    return final
	    
def makeDictArray(x):
    final = []
    for key in x.keys():
	if x[key] == "":
	    x[key] = 0

	final.append(int(x[key]))

    final = np.array(final)

    return final

def getValues(classes, data):
    final = []

    for i in range(len(classes)):
	
	D = getDataSet(classes[i],data) # get all points that are classified as class_i
	D_matrix = makeDictMatrix(D) # make the dictionary data into a numpy matrix
	n_i = len(D) # cardinality of D
	n = len(data) # size of the data set
	P_ci = float(n_i)/float(n) # prior probability of having that class
	mu_i = D_matrix.mean(0) # find the mean vector of the matrix
	# print classes[i]
	# print D_matrix
	# print mu_i
	size = (len(D),len(D[0].keys()))
	# print size
	ones =  np.ones(size)
	trans = np.asarray(mu_i.transpose())[0]
	# print ones
	# print trans
	# print D_matrix
	# print ones*trans
	Z_i = D_matrix - (ones*trans)
	# print (1.0/n_i)*(Z_i.transpose()*Z_i)
	Sigma_i = (1.0/n_i)*(Z_i.transpose()*Z_i)

	final.append([P_ci,mu_i,Sigma_i])

    return final

def probabilityDensity(x, mu_i, Sigma_i):
    dim = len(x.keys())
    x_vec = makeDictArray(x)
    
    # This is in case the determinant of the covariance matrix is 0
    if np.linalg.det(Sigma_i) >=1:
	first = float(1)/((np.power(np.sqrt(2*np.pi),dim))*(np.sqrt(np.linalg.det(Sigma_i))))
    else:
	first = 0
   
    part1 = x_vec-np.asarray(mu_i)
    
    try:
	part2 = np.linalg.inv(Sigma_i)
    except:
	part2 = np.linalg.pinv(Sigma_i)
    
    part3 = part1
    second = np.exp(-(part1*part2*part3.transpose())/2)
    
    return first*second

def test_single(x,values):
    classes = ["1800","1810","1820","1830","1840","1850","1860","1870","1880","1890","1900","1910","unkown"]
    max_prob = 0
    myClass = ""
    counter = 0

    for entry in values:
	temp = 0 
	try:
	    temp = probabilityDensity(x,entry[1],entry[2])*entry[0]
	except:
	    #print "error in probability Density: " + str(temp)
	    x = "dumb"
	if temp > max_prob:
	    max_prob = temp
	    myClass = classes[counter]
	counter += 1

    return myClass

def test():
    classes = ["1800","1810","1820","1830","1840","1850","1860","1870","1880","1890","1900","1910","unkown"]
    full_data = gd2.get_data_list_of_dicts()
    test_data = gd3.get_data_list_of_dicts()
    values = getValues(classes,test_data)
    
    correct = 0
    almost = 0
    total = len(full_data)
    for entry in full_data:
	decade = entry["class"]
	entry.pop("class",None)
	result = test_single(entry,values)
	if result == decade:
	    correct += 1
	try:
	    if abs(int(result[2])-int(decade[2])) <= 2:
		almost += 1
	except:
	    continue

    return [float(correct)/float(total), float(almost)/float(total)]

