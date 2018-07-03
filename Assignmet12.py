
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np


# In[11]:


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})
df


# In[12]:


#Some values in the  FlightNumber column are missing. These numbers are meant 
#to increace by 10 with each row so 10055 and 100075 need to be put in place. Fill in
#these missing numbers and make the column an integer column (instead of a float column).



new_flight_number = []
val = 10045
for x in range(len(df['FlightNumber'])):
    new_flight_number.append(val)
    val = val + 10
df['FlightNumber'] = new_flight_number
df


# In[14]:


# The From_To column would be better as two separate columns. Split each string on
#the undercore delimiter _ togive a new temporary Data Frame with the correct values.
# Assign the correct Column names to this temporaly DataFrame.

new_from = []
new_to = []

for x in df['From_To']:
    s = x.split("_")
    new_from.append(s[0])
    new_to.append(s[1])

df['From'] = new_from
df['To'] = new_to
 
tdf = df.drop(columns=['From_To'])
tdf


# In[5]:


#Notice how the capitalism of the city names is all mixed up in this temporary
#DataFrame. Standarise the strings so that only the fisrt letter is uppercase (e.g.
#"lonDon" should becone"London".)


new_from = []
new_to = []

for x in range(len(tdf['From'])):
    new_from.append(tdf['From'][x].capitalize())
    new_to.append(tdf['To'][x].capitalize())

tdf['From'] = new_from
tdf['To'] = new_to

tdf


# In[6]:


df = df.drop(columns=['From_To'])
df['From'] = tdf['From']
df['To'] = tdf['To']
df


# In[7]:


#Delete the From_to column from df and attach the temporary DataFrame from the
#previous questions.


d = {}
for x in range(len(df['RecentDelays'])):
    d[x] = df['RecentDelays'][x]

max_l = 0
for x in d:
    max_l = max(max_l, len(d[x]))

for x in d:
    while len(d[x]) < max_l:
        d[x].append(np.nan)



delays = pd.DataFrame(d).T
delays


# In[8]:


#In the RecentDelays column, the calues have been entered into the DataFrame as a
#list. We would like each first value in its own column, each sedcond value in its own
#column, and so on. If there isn't an Nth value, the value should NaN.

#Expand the series of lists into a DataFrame named delays, rename the columns delay_1
#delay_2 etc.and replace the unwanted RecentDelays columns in df with delays.


df['RecentDelays'] = delays.index
df


# In[ ]:





