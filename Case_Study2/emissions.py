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
import csv
import requests

#%%
"""
Download csv file and write to csv file. Only necessary 1st time to download
file locally.

url_08 = "https://www.epa.gov/sites/production/files/2016-07/08tstcar.csv"
filename = "data_08.csv"

with open(filename, 'wb') as out_file:
    out_file.write(requests.get(url_08).content)
"""

# Read csv file into a dataframe
df_08 = pd.read_csv("data_08.csv")
df_08.head()
#%%
url_18 = "https://www.epa.gov/sites/production/files/2018-06/18tstcar\
-2018-05-30.xlsx"

xl = pd.ExcelFile(url_18, sep="\t")

sheet_name = xl.sheet_names[0]

df_18 = pd.read_excel(url_18, sep="\t", sheet_name=sheet_name)
df_18.head()

# Save locally as csv file for faster read or in case url goes bad.
df_18.to_csv("data_18.csv")

#%%















