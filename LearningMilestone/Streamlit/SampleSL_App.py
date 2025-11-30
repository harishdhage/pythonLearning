import numpy as np
import streamlit as sl
import pandas as pd

sl.title("Employee Data")
data = pd.DataFrame({ 'Name':['Kariya','Kempa','Mabba','Dicchi','Tagadu'],
             'Age':[21,56,14,np.nan,46],
             'Dept':['HR','SSE',np.nan,'IT-Admin','QA'],
             'Salary':[12500,9200,28000,85000,3500]})

sl.write('Employee Records')
sl.write(data)
sl.bar_chart(data.set_index('Name')['Salary'])
sl.line_chart(data.set_index('Name')['Salary'])
charData =pd.DataFrame(np.random.randn(20,4),columns=['A','B','C','D'])
sl.line_chart(charData)