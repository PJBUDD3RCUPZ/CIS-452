#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 2
#01/24/2024
import numpy as np
import pandas as pd


#Task 6
arr7 = np.array([[1, 2], [3, 4]])
arr8 = np.array([[5, 6 ], [7, 8 ]])


Axis0Arr = np.concatenate((arr7, arr8), axis = 0)
Axis1Arr = np.concatenate((arr7, arr8), axis = 1)

print("Concatenate along axis=0:", Axis0Arr)
print("Concatenate along axis=1:", Axis1Arr)
