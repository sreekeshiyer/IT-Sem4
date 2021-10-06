import pandas as pd 
import numpy as np
data = pd.read_csv("employees.csv") 
data.replace(to_replace = np.nan, value = -99) 
print(data)