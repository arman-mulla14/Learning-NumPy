import numpy as np 
ages = np.array([[10,20,30,40,50],
                [60,70,80,90,100]])

teen = ages[ages < 18]
print(teen)