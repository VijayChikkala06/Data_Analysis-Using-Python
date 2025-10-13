# 1. (a) Write a Pandas program to create and display a one-dimensional 
# array-like object containing an array of data using Pandas module.

import pandas as pd
import numpy as np

data_list = pd.Series([5,10,15,20,25])
print(data_list)


# 1. (b) Write a Pandas program to convert a Panda 
# module Series to Python list and it's type.

import pandas as pd
import numpy as np

data_list = pd.Series([5,10,15,20,25])
print(data_list)

data_list = data_list.tolist()
print(data_list)


# 2. Consider sample Python dictionary data and list labels:
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
#                    'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'], 
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
# 'attempts': [1, 3, 2, 3, 1, 1, 1, 2, 1], 
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']} 
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# (a) Write a Pandas program to create and 
# display a DataFrame from a specified dictionary data which has the index labels.

import pandas as pd 
import numpy as np 

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily','Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'], 
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']} 
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 

df = pd.DataFrame(exam_data, index = labels) 
print(df)


# (b) Write a Pandas program to change the name 'James' to 'Suresh' in name column of the DataFrame.

import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily','Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'], 
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index = labels)
df.loc['d', 'name'] = 'Suresh'
print(df)


# (c) Write a Pandas program to insert a new column in existing DataFrame. 
# (d) Write a Pandas program to get list from DataFrame column headers. 
# (e) Write a Pandas program to get list from DataFrame column headers.import pandas as pd

import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily','Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'], 
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index = labels)
df.loc['d', 'name'] = 'Suresh'

salaries = [50000, 60000, 70000, 450000, 55000, 80000, 70000, 48000, 62000, 78000]
df['salary'] = salaries
print(df)