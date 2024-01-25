#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 2
#01/24/2024
import numpy as np
import pandas as pd


#Task 1
A = np.array([[1,2,3],[4,5,6]])

print("Shape of A", A.shape)

#Task 2
B = A.reshape(3,2)

print("Shape of B", B.shape)

#Task 3
C = B.transpose()

print("Shape of C", C.shape)
