import pandas as pd 

data = pd.read_csv("E:\\Sem-4\\Lab_Assignments\\Python_Lab\\Experiment_12\\employees.csv")
data["Gender"].fillna("No Gender", inplace = True)
print(data)
