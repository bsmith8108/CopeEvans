import get_data as gd
import numpy as np

def getDataSet(c, data):
    final = []
    for entry in data:
	if entry["class"] == c:
	    final.append(entry)

    return final

def makeDictMatrix(D)
    final = np.array()
    for entry in D:
	temp = []
	for item in entry.keys():
	    temp.append(entry[item])
	final.append([temp],final,axis=0)

    return final
	    
def makeDictArray(x):
    final = []
    for key in x.keys():
	final.append(x[key])

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
	mu_i = D_matrix.mean(1) # find the mean vector of the matrix
	size = (len(D[0].keys()), len(D))
	Z_i = D_matrix - (np.ones(size)*mu_i)
	Sigma_i = (1/n_i)(Z_i.transpose()*Z_i)

	final.append([P_ci,mu_i,Sigma_i])

    return final

def probabilityDensity(x, mu_i, Sigma_i):
    dim = len(x.keys())
    x_vec = makeDictArray(x)
    first = float(1)/((np.sqrt(2*np.pi)^dim)*(sqrt(np.linalg.det(Sigma_i))))
    second = np.exp(-((x_vec-mu_i)*np.linalg.inv(Sigma_i)*(x_vec-mu_i))/2)

    return first*second

def test(x):
    

