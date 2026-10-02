import numpy as np 
#0-D Array 
arry = np.array('A'); 
print(arry.ndim)
print(arry.shape)

# 1 - D Array 
b = np.array([21,23,45,6,7,76])
print(b.ndim)
print(b.shape)


# 2 - D Array 
c = np.array([
    [23,34,55],
    [67,89,32]
])
print(c.ndim)
print(c.shape)


#3-D Array 

d = np.array([
[[11,12,13], [14,15,16] , [14,15,909]], 
[[19,21,32], [34,75,96], [104,15,16]], 
[[29,42,83], [74,25,96], [14,15,166]]


])

print(d.ndim)
print(d.shape)
print(d[2][2][2])

table = d[0][0][2] + d[0][1][0] + d[0][2][2] 
print(table)