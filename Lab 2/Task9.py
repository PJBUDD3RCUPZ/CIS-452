#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 2
#01/24/2024
import numpy as np



#Task 9 
arr1 = np.array([[1,2], [3,4]])

arr2 = arr1.view() 

arr2[0,0] = 0 

print("arr12: ", arr1)
print("arr13: ", arr2)