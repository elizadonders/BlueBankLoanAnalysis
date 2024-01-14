# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 06:53:15 2023

@author: eliza
"""

import json
import pandas as pd
import numpy as np


# method to open json file in data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#transform to dataframe (convert from json to table)
loandata = pd.DataFrame(data)

#finding unique values for the purpose column
loandata['purpose'].unique()

#to describe the data
loandata.describe()

#describe the data for a specific column

loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#using fico (Fico score): vc deve olhar na colunna na tabela a condicao aplicada no intervalo.
#fico = category , ficocat significa classicar as caterorias de acordo com o intervalo.
#fico >= 300 and < 400:    ficocat = 'Very Poor" 
#fico >= 400 and ficoscore < 600:  ficocat = 'Poor'
#fico >= 601 and ficoscore < 660: ficocat = 'Fair'
#fico >= 660 and ficoscore < 780:  ficocat = 'Good'
#fico >= 780: ficocat = 'Excellent'
#else   ficocat = 'Unknown'
#applying for loops to loan data

length = len(loandata)
ficocat =[]

for x in range (0,length):
    category = loandata['fico'][x]
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category>= 601 and category < 660:
            cat = 'Fair'
        elif category>= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Unknown'
    
    ficocat.append(cat)
ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat

# df.loc as conditional statements
# df.loc[df[columnname] condition, newcolumnname] = 'value if the condition'

#for interest rates, a new column is wanted. rate > 0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] ='Low'




#write to csv
loandata.to_csv('loan_cleaned.csv', index = True)



















            
            
















