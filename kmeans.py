import copy

#x = [12,18,22,11,9,3,5,6,111,10]
y = [9,19,21,3,33,2,56,31,77,1]

test=[]

def checkminimum(test):
	#test has the intracluster distances for your data point,refer to kmeans function, first for loop
	min_dist = test[0]
	c=0
	p=0	
	for i in test:
		if min_dist>i:
			min_dist = i
			p=c #c is the position of the minimum intracluster distance element
		c=c+1			
	return p


def kmeans():
	medians=[]
	clusters={}
	clusters2={}
	k = input("Please enter a value for how many clusters you want") #k classes would be made
	count=0
	for i in y:
		if count<k:
			medians.append(i)
			count=count+1

	for i in range(k):
		clusters[i]=[] #empty list holds your members of each class
	count=0
	test=[]
	for i in y:
		for x in range(k):
			test.append(abs(i-medians[x]))
		pos = checkminimum(test)
		clusters[pos].append(i)
		test=[]	
	print(clusters)
	while True:	
		medians=[]
		for x in clusters:
			b = sum(clusters[x])/len(clusters[x]) #centroid of the cluster
			medians.append(b)
		for i in range(k):
			clusters[i]=[] #empty list holds your members of each class
		for i in y:
			for x in range(k):
				test.append(abs(i-medians[x]))
			pos = checkminimum(test)
			clusters[pos].append(i)
			test=[]
		if clusters2==clusters:
			break	
		print(clusters)
		for i in range(k):
			clusters2[i]=[] #empty list holds your members of each class
		clusters2=copy.deepcopy(clusters)
	

kmeans()
