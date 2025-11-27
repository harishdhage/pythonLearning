import numpy as np
import pandas as pd

employee = { 'Name':['Kariya','Kempa','Mabba','Dicchi','Tagadu'],
             'Age':[21,56,14,np.nan,46],
             'Dept':['HR','SSE',np.nan,'IT-Admin','QA'],
             'Salary':[12500,9200,28000,85000,3500]}

print(employee)
employeeDataFrame = pd.DataFrame(employee)
print(employeeDataFrame)
print(employeeDataFrame['Name'])
print(employeeDataFrame[['Name','Dept']])
print(employeeDataFrame.head(3))
print(employeeDataFrame.tail(2))
print(employeeDataFrame.iloc[1:3])
print(employeeDataFrame.iloc[1:3, :2])
#print(employeeDataFrame.iloc[1:3, ['Name','Salary']]) #Not allowed
print(employeeDataFrame.loc[1:4,['Name','Dept','Salary']])
print(employeeDataFrame.shape)
print(employeeDataFrame.info())
print(employeeDataFrame.describe())