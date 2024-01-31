import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import pandas as pd


df = pd.read_csv("BostonHousing.csv")

sns.pairplot(df)


plt.show()