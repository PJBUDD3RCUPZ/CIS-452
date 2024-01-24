#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 2
#01/24/2024
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

np.save('test.npy', arr1)


arr2 = np.load('test.npy')


print("Arr1", arr1)
print("Arr2", arr2)