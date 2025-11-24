#To write a Pandas program to convert a Pandas module series to python list and its type
import pandas as pd
import numpy as np
data_list = pd.Series([10, 20, 30, 40, 50])
print(data_list)
data_list = data_list.tolist()
print(data_list)
