# importing pandas package
import pandas as pd
	
# making data frame from csv file
data = pd.read_csv("employees.csv")
	
# creating bool series True for NaN values
bool_series = pd.isnull(data["Gender"])
	
# displaying data only with Gender = NaN
print(data[bool_series])
