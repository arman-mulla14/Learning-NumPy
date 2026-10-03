import numpy as np 

scores = np.array([56,67,90,55,75,61,17,28,29,40])
scores[scores < 60 ] = 0 ; 
print(scores) #--> that will print the array with all the values greater than 60 replaced with 0 which is [ 0  0  0 55 75 61 17 28 29 40]