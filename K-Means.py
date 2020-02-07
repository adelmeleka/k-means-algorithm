import random
import sys
import copy
import numpy as np

# Takes on point and list of centroids
# Retuns index of the corresponding cluster assignment
def min_Eclidean(p,centroids):
    minInd = -1
    minDis = sys.maxsize
    for i in range (0,len(centroids)):
        dis = (p[0]-centroids[i][0])**2 + (p[1]-centroids[i][1])**2 
        if dis < minDis:
            minDis = dis
            minInd = i
    return minInd

#Kmeans algorithm
    #returns set of clusters
def K_Means(dataSet,k,e):
    
    # number of iterations 
    t = 0
    #initialize k random UNIQUE centroids
    centroids = []
    chosenIndx = []*k
    for i in range(0,k):
        t = random.randint(0,len(dataSet)-1)
        while t in chosenIndx :
            t = random.randint(0,len(dataSet)-1)
        chosenIndx.append(t)
        x = dataSet[t][:]
        centroids.append(x)   
    
    while True:        
        t = t + 1
    
        #initialize label holding clustered dataset 
        labels = [None] * len(dataSet)
        #initialize clusters -each row contains data set of same cluster-
        clusters =[]
        for q in range(0,k):
            clusters.append([])
                    
        #clusters & labels assignment
        for i in range(0,len(dataSet)):
            j = min_Eclidean(dataSet[i],centroids)      
            clusters[j].append(dataSet[i])
            labels[i] = j
        
        #centroids update
        l = len(centroids)
        prevCentroids = []
        prevCentroids = copy.deepcopy(centroids)
        centroids = []
        for i in range (0,l):
            sumX = 0
            sumY = 0

            for j in range (0,len(clusters[i])):
                sumX = sumX + clusters[i][j][0]
                sumY = sumY + clusters[i][j][1]
            
            x = []
            x.append(sumX/len(clusters[i]))
            x.append(sumY/len(clusters[i]))
            centroids.append(x)   
        
        #stopping condition - can be added here: max # of iterations 't's
        if np.all(prevCentroids) == np.all(centroids) :
            break
        
    print ("k: ",k)
    print("Iterations: ",t)
    return labels


    
########################################################## MAIN ##############################################################

### storing current data points
    #rows: number of points
    #cols: number of dimensions
data = [(2,4),(3,3),(3,4),(5,4),(6,4),(7,3),(7,4),(8,2),(9,4)
        ,(6,5),(5,6),(6,7),(5,8),(11,5),(10,6),(10,7),(10,8),
        (11,8),(12,7),(13,6),(13,7),(14,6),(15,4),(15,5)]
dataMatrix = []
for i in range(0,len(data)):
    x = []
    x.append(data[i][0])
    x.append(data[i][1])
    dataMatrix.append(x)        

print("Data matrix",len(dataMatrix))

## (a) performing K-means Algorithm
k = [2, 3, 4, 5, 6]

#c = K_Means(dataMatrix,6,0)
c = K_Means(np.array(dataMatrix),3,0)

print("Labels")
print(c)

'''
print("Clusters")
#show clusters
for i in range (0,len(c)):
    print("cluster ",i+1)
    print(c[i])
'''