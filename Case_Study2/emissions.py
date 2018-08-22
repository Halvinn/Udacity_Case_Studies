# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 12:15:11 2018

@author: ONESIH
"""

"""
The data for emissions was available on the EPA's website in the form of xlsx 
and csv files. I downloaded the data directly from the website.
"""
#%% Download and Load Data
import pandas as pd
import numpy as np
import urllib4

#%%
url_08 = "https://www.epa.gov/sites/production/files/2016-07/08tstcar.csv"
socket = urllib.urlopen(url_08)
ex = pd.ExcelFile(socket)

print(ex.sheet_names)

#%%
url_18 = "https://www.epa.gov/sites/production/files/2018-06/18tstcar\
-2018-05-30.xlsx"


df_08 = pd.read_excel(url_08)
df_18 = pd.read_csv(url_18)

print(df_08.head())

#%%