import numpy as np 

num = np.array([[1,2,3,4,5,6,7,8,9,10]])
table = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(table.shape)
print(num.shape)
table = num * table
print(table)