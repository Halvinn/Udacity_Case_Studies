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

#%% Combine the dataframes

# Add color column to both dataframes
color_white = np.repeat("white", len(whites_df))
color_red = np.repeat("red", len(reds_df))

reds_df["color"] = color_red
whites_df["color"] = color_white

print(reds_df.head(2))

# Concatenate the dataframes into one frame
wines_df = pd.concat([reds_df, whites_df], ignore_index=True)

print(wines_df.sample(5))

# Save to csv
wines_df.to_csv("winequality_mixed.csv", index=True)

#%%






















