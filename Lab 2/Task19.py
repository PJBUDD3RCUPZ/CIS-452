#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 2
#01/24/2024

#Task 19

import numpy as np 
import pandas as pd


df = pd.read_csv("tips.csv")

crossTable = pd.crosstab(df['day'], df['size'])

print(crossTable)

