#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 2
#01/24/2024
import numpy as np
import pandas as pd


#Task 8
arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.copy(arr1)

#print("arr2:\n", arr2)

arr2[0,0] = 0 

print("arr1:\n", arr1)
print("arr2:\n", arr2)