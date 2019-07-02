"""
Author  : Jabez Wilson (jwilson@iesys.com)
Created : dd/mm/2019

Visualises Data

TODO
    - 

CHANGELOG
    dd/mm/2019 xx:00 - Created File 
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.defchararray import add as npStrAdd
tdata = pd.read_pickle('Transaction.pkl')
months = np.array(['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])


#%%
# Selecting the month and plotting a pie graph of Categories
month = 6
year = 2019

mask = (tdata['Date'].dt.year == year) & (tdata['Date'].dt.month == month)
df = tdata[mask]

cats = df['Category'].unique().astype('str')
total = np.zeros(cats.shape)
for i in range(cats.shape[0]):
    total[i] = df[df['Category'] == cats[i]]['Amt'].sum()

ratio = (total *100 / sum(total)).astype('|S4').astype('str')
cats = npStrAdd( npStrAdd(npStrAdd(cats,' (') , ratio) , '%)')
fig, ax = plt.subplots()
ax.pie(total, labels=cats)

#%%
# Selecting a category and plotting time varying plot of total amt
cat = 'Groceries'
year = 2019

mask = (tdata['Date'].dt.year == year) & (tdata['Category'] == cat)
df = tdata[mask]
grouped = df.groupby(by=df['Date'].dt.month)['Amt'].sum()
grouped.index = pd.CategoricalIndex(months[grouped.index])

fig, ax = plt.subplots()
ax = grouped.plot.bar(x='Date', y='Amt', rot=0)
for p in ax.patches:
    ax.annotate(str(p.get_height()) + '$', (p.get_x()+0.04, p.get_height() - 15), c='white')