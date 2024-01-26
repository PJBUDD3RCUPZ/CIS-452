#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 2
#01/24/2024

#Task 20


import numpy as np 
import pandas as pd


df = pd.read_csv("tips.csv")

crossTable = pd.crosstab(df['day'], df['size'])

# n(i,j) = (orignal value(i,j)) / sum of column j 
normalizedCrossTable = crossTable.div(crossTable.sum(axis=0), axis=1)

# Print the normalized cross table
print("\nNormalized Cross Table:")
print("\n",normalizedCrossTable)
