import numpy as np 
data = np.array([[1,2,3,4,5,6,7,8,9,10], 
                 [11,12,13,14,15,16,17,18,19,20],
                 [21,22,23,24,25,26,27,28,29,30]])
#print(np.sum(data, axis=0)) # sum of each column
#print(np.sum(data, axis=1)) # sum of each row
#print(np.mean(data, axis=0)) # mean of each column
#print(np.mean(data,axis = 1)) # mean of each row
#print(np.std(data, axis=0)) # standard deviation of each column
print(np.std(data, axis=1)) # standard deviation of each row
print(np.var(data, axis=0)) # variance of each column
print(np.var(data, axis=1)) # variance of each row
print(np.min(data, axis=0)) # minimum of each column
print(np.min(data, axis=1)) # minimum of each row
print(np.max(data, axis=0)) # maximum of each column
print(np.max(data, axis=1)) # maximum of each row
print(np.argmin(data, axis=0)) # index of minimum of each column
print(np.argmin(data, axis=1)) # index of minimum of each row
print(np.argmax(data, axis=0)) # index of maximum of each column
print(np.argmax(data, axis=1)) # index of maximum of each row
print(np.median(data, axis=0)) # median of each column
print(np.median(data, axis=1)) # median of each row
print(np.percentile(data, 25, axis=0)) # 25th percentile of each column
print(np.percentile(data, 25, axis=1)) # 25th percentile of each row
print(np.percentile(data, 50, axis=0)) # 50th percentile of each column
print(np.percentile(data, 50, axis=1)) # 50th percentile of each row
