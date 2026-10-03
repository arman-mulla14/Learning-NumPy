import numpy as np 

#vectorizing the scalar operations

array = np.array([1,2,3,4,5,6,7,8,9,10])
array1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(array == 9)
print(array + array1) #--> that will print the addition of the two arrays which is [ 2  4  6  8 10 12 14 16 18 20]
print(array - array1) #--> that will print the subtraction of the two arrays which is
print (array * array1) #--> that will print the multiplication of the two arrays which is [  1   4   9  16  25  36  49  64  81 100]
print(array / array1) #--> that will print the division of the two arrays which is
print(array ** array1) #--> that will print the power of the two arrays which is [         1          4         27        256       3125      46656     823543   16777216 387420489 10000000000]
print(np.sqrt(array)) #-> that will print the square root of the array which is [1.         1.41421356 1.73205081 2.         2.23606798 2.44948974 2.64575131 2.82842712 3.         3.16227766]     
print(np.round(array)) #-> that will print the rounded values of the array which is [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
print(np.floor(array)) #-> that will print the floor values of the array which is [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
print(np.ceil(array)) #-> that will print the ceiling values of the array which is [ 1.  2.  3.  4.  5.  6.  7. 
print(np.exp(array))#--> that will print the exponential values of the array which is [2.71828183e+00 7.38905610e+00 2.00855369e+01 5.45981500e+01 1.48413159e+02 4.03428793e+02 1.09663316e+03 2.98095799e+03 8.10308393e+03 2.20264658e+04]
print(np.log(array))#--> that will print the logarithmic values of the array which is [0.         0.69314718 1.09861229 1.38629436 1.60943791 1.79175947 1.94591015 2.07944154 2.19722458 2.30258509]
print(np.log10(array))#--> that will print the logarithmic values of the array which is [0.         0.30103    0.47712125 0.60205999 0.69897    0.77815125 0.84509804 0.90308999 0.95424251 1.        ]
print(np.sin(array))#--> that will print the sine values of the array which is [ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427 -0.2794155   0.6569866   0.98935825  0.41211849 -0.54402111]
print(np.cos(array))#--> that will print the cosine values of the array which is [ 0.54030231 -0.41614684 -0.9899925  -0.65364362  0.28366219  0.96017029  0.75390225 -0.14550003 -0.91113026 -0.83907153]
print(np.tan(array))#--> that will print the tangent values of the array which is [ 1.55740772 -2.18503986 -0.14254654  1.15782128 -3.38051501 -0.29100619  0.87144798 -6.79971146 -0.45231566  0.64836083] 
print(np.arcsin(array))
print(np.arccos(array))
print(np.arctan(array))
print(np.sinh(array))
print(np.cosh(array))
print(np.tanh(array))
print(np.arcsinh(array))
print(np.arccosh(array))
