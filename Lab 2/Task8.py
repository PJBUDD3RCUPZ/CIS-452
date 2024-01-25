#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 2
#01/24/2024
import numpy as np
import pandas as pd


#Task 8
arr10 = np.array([[1, 2], [3, 4]])

arr11 = np.copy(arr10)

print("arr11:", arr11)

arr11[0,0] = 0 

print("arr10:", arr10)
print("arr11:", arr11)