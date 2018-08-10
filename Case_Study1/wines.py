# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 16:39:03 2018

@author: ONESIH
"""

#%% Imports and Load data

import pandas as pd
import numpy as np

whites_df = pd.read_csv("winequality-white.csv", sep=";")
reds_df = pd.read_csv("winequality-red.csv", sep=";")

print(whites_df.head())

print(reds_df.head())

#%% Reds
print(reds_df.shape)

for i in reds_df.columns:
    print(i)

print(reds_df.info())

# Unique values for quality variable
print(reds_df.quality.value_counts())

print(reds_df.density.mean())

#%% Whites
print(whites_df.shape)

print(whites_df.columns)

print(whites_df.info())

# Unique values fro quality variable
print(whites_df.quality.nunique())
#%%

# Duplicates
print(reds_df.duplicated().sum())

print(whites_df.duplicated().sum())


#%%