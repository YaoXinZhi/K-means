
# -*- coding : utf-8 -*-
# /usr/bin/python
# file K-means

import math
import sys
import getopt

def get_data(file):
    data = []
    with open(file) as f:
        for line in f:
            l = line.replace('\n','').split('\t')
            data.append((l[0],l[1]))
    return data 

def get_distance(a,b):
    x0 = float(a[0])
    y0 = float(a[1])
    x1 = float(b[0])
    y1 = float(b[1])
    
    distance = math.sqrt( (x0-x1)**2 + (y0-y1)**2 )
    return distance

def get_center(elements_list):
    x = 0
    y = 0
    list_center = (0,0)
    for i in elements_list:
        x += float(i[0])
        y += float(i[1])
    x = x / len(elements_list)
    y = y / len(elements_list)
    
    list_center = (x,y)
    return list_center
    
def Clustering(center={}):
    new_category = {}
    for i in range(K):
        new_category[str(i)] = []
    for i in range(len(data)):
        distance = {}
        for j in range(K):
            distance[str(j)] = get_distance(data[i],center[str(j)])
            if j == 0:
                min_distance = distance['0']
                min_category ='0'
            else:
                if distance[str(j)] < min_distance:
                    min_distance = distance[str(j)]
                    min_category = str(j)
        new_category[min_category].append(data[i])
    return new_category
        
        

def k_means():
    
    # Initialize the cluster center
    center = {}
    category = {}
    for i in range(K):
        center[str(i)] = data[i]
        category[str(i)] = []
        category[str(i)].append(data[i])
    print (center)

    # run k_means for t == 0
    for i in range(K,len(data)):
        distance = {}
        for j in range(K):
            distance[str(j)] = get_distance(data[i],center[str(j)])
            if j == 0:
                min_distance = distance['0']
                min_category = '0'
            else:
                if distance[str(j)] < min_distance:
                    min_distance = distance[str(j)]
                    min_category = str(j)
        category[min_category].append(data[i])
        
    for i in category.keys():
        new_center=get_center(category[i])
        if center[i] != new_center:
            center[i] = new_center

    # run k_means for t > 0
    o = 0
    while o != K: 
        category = Clustering(center)
        o = 0
        for i in category.keys():
            new_center=get_center(category[i])
            
            if center[i] == new_center:
                o += 1
                print (o)
            if center[i] != new_center:
                center[i] = new_center
                print (new_center)
            if o == K:
                print ('win')
                break
            
    return category
        
    
        
    

        
if __name__ == '__main__':
    
    opts,args = getopt.getopt(sys.argv[1:],'k:f:')
    
    file = 'K-means data'
    K = 5
    
    for op,value in opts:
        if op == '-f':
            file = value
        if op == '-k':
            K = value
    
    data = get_data(file)
    category = k_means()
    
    print ('result :')
    for i in category.keys():
        print (i + ':    ' + str(category[i]))