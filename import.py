"""
Author  : Jabez Wilson (jwilson@iesys.com)
Created : dd/mm/2019

script to Import from CSV file

TODO
    - 

CHANGELOG
    dd/mm/2019 xx:00 - Created File 
"""
import pandas as pd
from datetime import datetime

tran_fname = 'C:/Users/jabez/Downloads/Transactions.csv'
budget_fname = 'C:/Users/jabez/Downloads/Budget.csv'
df = pd.read_csv(tran_fname, encoding = "ISO-8859-1")
df = df.drop(labels='Unnamed: 6', axis=1)
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b').apply(lambda dt: dt.replace(year=2019))
df = df.drop(labels='Day', axis=1)
#df.to_pickle('Transaction.pkl')

#df = pd.read_csv(budget_fname, encoding = "ISO-8859-1")
#df['Month'] = pd.to_datetime(df['Month'], format='%b-%y').apply(lambda dt: dt.replace(day=1))
#df.to_pickle('Budget.pkl')
