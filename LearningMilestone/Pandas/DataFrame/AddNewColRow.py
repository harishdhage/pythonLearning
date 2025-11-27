import numpy as np
import pandas as pd

employee = { 'Name':['Kariya','Kempa','Mabba','Dicchi','Tagadu'],
             'Age':[21,56,14,np.nan,46],
             'Dept':['HR','SSE',np.nan,'IT-Admin','QA'],
             'Salary':[12500,9200,28000,85000,3500]}

employeeDF = pd.DataFrame(employee)
print(employeeDF)

#Add Column
employeeDF['Work Shift'] = ['Morning','Night','NA', 'Night','Intern']
print(employeeDF)

#Add Row
new_row = pd.DataFrame([{'Name':'Baccha','Age':16,'Dept':'Server','Salary':4700,
                         'Work Shift':'Any time'}])
employeeDF = pd.concat([new_row, employeeDF])
print(employeeDF)

#Multiple rows
multi_rows = pd.DataFrame([{'Name':'Blade Raja','Age':26,'Dept':'Dev','Salary':14700,
                         'Work Shift':'Morning'},
                           {'Name':'Circuit','Age':20,'Dept':'Admin','Salary':6200,
                         'Work Shift':'Any time'}])
employeeDF = pd.concat([multi_rows, employeeDF])
print(employeeDF)
print(employeeDF.loc[0])