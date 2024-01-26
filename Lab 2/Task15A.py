#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 2
#01/24/2024

#Task 15
import numpy as np 
import pandas as pd

data1 = [2, 4, 6, 8, 10, 12, 14, 16, 18]

output = pd.Series(data1)

print("All Sereies Data:\n")
print(output,"\n")

output2 = output[output > 7]
print("Series Data > 7:\n")
print(output2,"\n")
