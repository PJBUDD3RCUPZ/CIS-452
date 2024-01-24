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



#Task 4
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6 ], [7, 8 ]])


arr3 = np.dot(arr1, arr2)

print("Arr3:", arr3)

#Task 5
arr4 = np.array([[1, 2], [3, 4]])
arr5 = np.array([[5, 6 ], [7, 8 ]])


arr6 = np.multiply(arr4, arr5)

print("Arr6:", arr6)

#Task 6
arr7 = np.array([[1, 2], [3, 4]])
arr8 = np.array([[5, 6 ], [7, 8 ]])


Axis0Arr = np.concatenate((arr7, arr8), axis = 0)
Axis1Arr = np.concatenate((arr7, arr8), axis = 1)

print("Concatenate along axis=0:", Axis0Arr)
print("Concatenate along axis=1:", Axis1Arr)

#Task 7 
arr9 = np.array([[1, 2], [3, 4]])

multplyArray = arr9 * 3 

print("Element-Wise Multiplication:", multplyArray)

#Task 8
arr10 = np.array([[1, 2], [3, 4]])

arr11 = np.copy(arr10)

print("arr11:", arr11)

arr11[0,0] = 0 

print("arr10:", arr10)
print("arr11:", arr11)

#Task 9 
arr12 = np.array([[1,2], [3,4]])

arr13 = arr12.view() 

arr13[0,0] = 0 

print("arr12: ", arr12)
print("arr13: ", arr13)
