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
print(tdata.tail(10))
GROCERIES = 'Groceries'
TRANSPORT = 'Transport'
UTILITIES = 'Utilities'
HOUSE     = 'House'
CASH      = 'Cash'
EATOUT    = 'Eat-Out'
SHOPPING  = 'Shopping'
VISA      = 'Visa'

REGULAR = 'Regular'
NOTAG   = np.nan

writeout = False
#writeout = True

#%%
data = [
        ['2019-10-10', 3.5, EATOUT, NOTAG, 'Romeos'],
        ['2019-10-10', 258, SHOPPING, NOTAG, 'Flight to Melb'],
        
        ['2019-10-11', 15.5, EATOUT, NOTAG, 'GyG'],
        ['2019-10-11', 27.75, EATOUT, NOTAG, 'Paragon'],
        ['2019-10-10', 1, EATOUT, NOTAG, '7-11'],
        ['2019-10-10', 99, SHOPPING, NOTAG, 'Jacket'],
        ['2019-10-10', 10.6, EATOUT, NOTAG, 'Messina'],
        
        ['2019-10-12', 79.79, UTILITIES, NOTAG, 'Arc'],
        ['2019-10-12', 15.5+3.6+10.75, GROCERIES, NOTAG, 'Coles'],
        ['2019-10-12', 13.55, GROCERIES, NOTAG, 'Meat'],
        
        ]

#%%
for row in data:
    tdata = tdata.append(pd.Series([np.datetime64(row[0])] + row[1:], index=tdata.columns), ignore_index=True)

#%%
print('Modifications:')
print(tdata.tail(10))

#%%
# WARNING!! Make certain!
if writeout:
    print('WARNING: Writing Out!!')
    tdata.to_pickle('Transaction.pkl')