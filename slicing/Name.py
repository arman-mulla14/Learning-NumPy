import numpy as np

data = np.array([
    
    [ ['A','B','C','D','E'], ['F','G','H','I','J'] ],
                  [['K','L','M','N','O'],['P','Q','R','S','T']], 
                  [['U','V','W','X','Y'],   ['Z','1','2','4','5']]])

print(data[0][0][0])
print(data[1][1][2])
print(data[1][0][2])
print(data[0][0][0])
print(data[1][0][3])

data1 = np.array([data[0][0][0] , data[1][1][2], data[1][0][2], data[0][0][0], data[1][0][3]])

print(data1)