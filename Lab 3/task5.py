import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import pandas as pd


df = pd.read_csv("BostonHousing.csv")

sns.boxplot(x=df['dis'])

plt.xlabel('Distance')
plt.title('Boxplot')

plt.show()