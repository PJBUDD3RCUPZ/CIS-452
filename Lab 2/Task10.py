#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 2
#01/24/2024

#Task 10
import numpy as np

arr1 = np.array([[1, 2],
                 [3, 4]])

np.save('test.npy', arr1)


arr2 = np.load('test.npy')


print("\narr1\n", arr1)
print("\narr2\n", arr2,"\n")