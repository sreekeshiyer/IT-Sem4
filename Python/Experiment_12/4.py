import pandas as pd 
import numpy as np

data = pd.read_csv("E:\\Sem-4\\Lab_Assignments\\Python_Lab\\Experiment_12\\employees.csv") 
data.replace(to_replace = np.nan, value = -99) 
print(data)
