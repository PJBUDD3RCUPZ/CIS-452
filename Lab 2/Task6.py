#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 2
#01/24/2024
import numpy as np
import pandas as pd


#Task 6
arr1 = np.array([[1, 2], 
                 [3, 4]])
arr2 = np.array([[5, 6 ], 
                 [7, 8 ]])


Axis0Arr = np.concatenate((arr1, arr2), axis = 0)
Axis1Arr = np.concatenate((arr1, arr2), axis = 1)

print("\nAxis 0 has shape of: ", Axis0Arr.shape)
print("\nConcatenate along axis=0::\n", Axis0Arr)
print("\nAxis 1 has shape of: ", Axis1Arr.shape)
print("Concatenate along axis=1:\n", Axis1Arr)
