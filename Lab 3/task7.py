#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 3
#02/04/2024
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import pandas as pd


#save dataframe as df
df = pd.read_csv("BostonHousing.csv")

#make a pairwise correlation of columns in df, new variable = newdf
newdf = df.corr()

sns.heatmap(data = newdf)   
plt.title('Task 7')
plt.show()
