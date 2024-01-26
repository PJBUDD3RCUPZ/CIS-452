#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 2
#01/24/2024

#Task 15
import numpy as np 
import pandas as pd

data1 = [2, 4, 6, 8, np.nan]

output = pd.Series(data1)

print("Resulting Series:\n")
print(output,"\n")

newOutput = output * 5 

print("Resulting Series * 5:\n")
print(newOutput,"\n")