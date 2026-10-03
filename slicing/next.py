import numpy as np 

data = np.array([[1,2,3,4,5], 
                 [6,7,8,9,10],
                 [11,12,13,14,15],
                [16,17,18,19,20]

                 
                 ])

print(data) #----> that will print the whole array which is [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
#array[start : end  : step ] 

#1st layer if i want 
#print(data[1]) #----> that will  print the 2nd row of the array which is [6,7,8,9,10]

#print(data[5]) #----> that will show error because there is no 6th row in the array

#print(data[-1]) #-----> that will print the last row of the array which is [16,17,18,19,20] 

#print(data[-2]) #-----> that will print the 2nd last row of the array which is [11,12,13,14,15]
 

 # multi layer slicing

#print(data[2:4]);  ----> that will print the 3rd and 4th row of the array which is [[11,12,13,14,15],[16,17,18,19,20]]

#print(data[0:4]) ---> that will print the 1st, 2nd, 3rd and 4th row of the array which is [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]

#print(data[0:3:2]) --> that will print the 1st and 3rd row of the array which is [[1,2,3,4,5],[11,12,13,14,15]]
print("\n")
#print(data[1:4:2]) ---> that will print the 2nd and 4th row of the array which is [[6,7,8,9,10],[16,17,18,19,20]]
print("\n")
#print(data[2:4:1]) ---> that will print the 3rd and 4th row of the array which is [[11,12,13,14,15],[16,17,18,19,20]]


#print(data[::-1]) #----> that will print the array in reverse order which is [[16,17,18,19,20],[11,12,13,14,15],[6,7,8,9,10],[1,2,3,4,5]]   

#print(data[::-2]) #----> that will print the 4th and 2nd row of the array which is [[16,17,18,19,20],[6,7,8,9,10]]


#column slicing 
#print(data[:,1]) #--> that will print the 2nd column of the array which is [2,7,12,17]
#print("\n")
#print(data[:,2]) #--> that will print the 1st and 2nd row of the array which is [[1,2,3,4,5],[6,7,8,9,10]]
#print("\n")
#print(data[:,-1]) #--> that will print the last column of the array which is [5,10,15,20]


# multiple column slicing

#print(data[:,0 : 4]) #---> that will print the 1st, 2nd, 3rd and 4th column of the array which is [[1,2,3,4],[6,7,8,9],[11,12,13,14],[16,17,18,19]]


#print(data[:,1:4:1])  #-->  that will print the 2nd, 3rd and 4th column of the array which is [[2,3,4],[7,8,9],[12,13,14],[17,18,19]]

#print(data[:,0 : 3]) #--> that will print the 1st, 2nd and 3rd column of the array which is [[1,2,3],[6,7,8],[11,12,13],[16,17,18]]


#print(data[:,1:]) #--> that will print the 2nd, 3rd, 4th and 5t    h column of the array which is [[2,3,4,5],[7,8,9,10],[12,13,14,15],[17,18,19,20]]

#print(data[:,::2]) 
#print(data[:, ::-1]) #---> that will print the array in reverse order of columns which is [[5,4,3,2,1],[10,9,8,7,6],[15,14,13,12,11],[20,19,18,17,16]]


#print(data[0:2, 0 : 2]) #---> that will print the 1st and 2nd row and 1st and 2nd column of the array which is [[1,2],[6,7]])

#print(data[0 : 3 , 0: 3]  ) #--> that will print the 1st, 2nd and 3rd row and 1st, 2nd and 3rd column of the array which is [[1,2,3],[6,7,8],[11,12,13]]

print(data[2: , 2:2])