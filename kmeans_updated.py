import math as m
import copy

#x = [12,18,22,11,9,3,5,6,111,10]
y = [[1,9],
	 [9,2],
	 [3,3],
	 [10,5],
	 [3,7],
	 [10,3]]
	
check_min=[]
test=[]

def checkminimum(test):
	#test has the intracluster distances for your data point,refer to kmeans function, first for loop
	min_dist = test[0]
	c=0
	p=0	
	for i in test:
		if min_dist > i:
			min_dist = i
			p=c #c is the position of the minimum intracluster distance element
		c=c+1					
	return p


def kmeans():
	medians=[]
	clusters={}
	clusters2={}
	k = int(input("Please enter a value for how many clusters you want")) #k classes would be made
	count=0
	for i in y:
		if count<k:
			medians.append(i)
			count=count+1

	for i in range(k):
		clusters[i]=[] #empty list holds your members of each class
	count=0
	q=0
	test=[]
	for i in y:
		for x in range(k):
			q=q+1
			test.append(m.sqrt((medians[x][0]-i[0])**2 + (medians[x][1]-i[1])**2))
		pos = checkminimum(test)
		clusters[pos].append(i)
		test=[]	
	print(clusters)
	while(True):
		medians=[]
		for x in clusters.values():
			#b = [sum(x[0])/len(clusters[x]), sum(clusters[x[1]])/len(clusters[x])] #centroid of the cluster
			b=[0,0]
			for e in x:
				b[0] = b[0] + e[0]/len(x)
				b[1] = b[1] + e[1]/len(x)
			medians.append(b)	
		for i in range(k):
			clusters[i]=[]
		for i in y:
			for x in range(k):
				test.append(m.sqrt((medians[x][0]-i[0])**2 + (medians[x][1]-i[1])**2))
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
		
	
	
		
	
			
		
	 
	
	
