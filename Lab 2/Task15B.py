#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 2
#01/24/2024

#Task 15
import numpy as np 
import pandas as pd

data1 = [2, 4, 6, 8, 10, 12, 14, 16, 18]

output = pd.Series(data1)
    

print("Orginal All Sereies Data:\n")
print(output,"\n")

booleanizedSeries = output >= 7
print("Booleanized Series Data\n")
print (booleanizedSeries,"\n")


