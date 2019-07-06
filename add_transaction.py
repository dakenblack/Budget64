"""
Author  : Jabez Wilson (jwilson@iesys.com)
Created : 02/07/2019

Adds new entries

TODO
    - 

CHANGELOG
    dd/mm/2019 xx:00 - Created File 
"""
import pandas as pd
import numpy as np

tdata = pd.read_pickle('Transaction.pkl')
print(tdata.tail())
GROCERIES = 'Groceries'
TRANSPORT = 'Transport'
UTILITIES = 'Utilities'
HOUSE     = 'House'
CASH      = 'Cash'
EATOUT    = 'Eat-Out'
SHOPPING  = 'Shopping'

REGULAR = 'Regular'
NOTAG   = np.nan

date = '2019-07-06'
writeout = False

#%%
data = [
        [date, 29.92, GROCERIES, NOTAG, 'Bunnings'],
        [date, 21.59, GROCERIES, NOTAG, 'Coles'],
        ]

#%%
for row in data:
    tdata = tdata.append(pd.Series([np.datetime64(row[0])] + row[1:], index=tdata.columns), ignore_index=True)

#%%
print('Modifications:')
print(tdata.tail())

#%%
# WARNING!! Make certain!
if writeout:
    print('WARNING: Writing Out!!')
    tdata.to_pickle('Transaction.pkl')