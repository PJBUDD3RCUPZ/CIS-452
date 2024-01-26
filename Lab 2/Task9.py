#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 2
#01/24/2024
import numpy as np



#Task 9 
arr1 = np.array([[1,2], 
                 [3,4]])

arr2 = arr1.view() 

arr2[0,0] = 0 

print("\narr1: \n", arr1)
print("\narr2: \n", arr2,"\n")