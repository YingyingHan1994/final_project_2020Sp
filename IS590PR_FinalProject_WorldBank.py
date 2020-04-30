"""
IS590PR: Final Project
Written by: Jenna Kim

This file is to create a function to read in data
from World Bank Dataset
and create a data frame with extracted info

"""
import pandas as pd

############################# SKIP THIS PART ####################################
# Read in data into data frame
data_df = pd.read_csv("World_Bank_Data.csv", usecols=['Country Name', 'Country Code', '2018'], index_col=False)
meta_df = pd.read_csv("World_Bank_Metadata.csv", usecols=['Country Code', 'Region', 'IncomeGroup'], index_col=False)

# Change column names
data_df.columns = ['CountryName', 'CountryCode', 'Population']
meta_df.columns = ['CountryCode', 'Region', 'Income']

# Explore data
# print(data_df.head())
# print(data_df.shape) # how many rows?: (264,3)

# print(meta_df.head())
# print(meta_df.shape) # how many rows?: (263,3)
# Join two data frames

df_join = pd.merge(data_df, meta_df, on='CountryCode', how='left')

# print(df_join.shape)  # (264, 5)
# print(df_join.head())

# How many rows with NaN value?
# print(df_join.isnull().sum(axis=0))

# Clean data
# remove rows with country names not classified
df_join = df_join.drop(df_join[df_join.CountryName == 'Not classified'].index)
# remove 'income' from Income column
df_join['Income'] = df_join['Income'].str.replace('income', '')
# print(df_join.shape)   # (236, 5)

# Statistics
# row counts by income, country name, and population
grp = df_join.groupby(['Income', 'CountryName', 'Population'])
# print(grp.size())
# print(grp.count())

# Export data frame to csv file
df_join.to_csv('WorldBank_merged.csv', index=False, header=True)

###################################################
#### USE BELOW FUNCTION
###################################################

def read_worldbank_data(filename1, filename2):
    """
    This function is to read in data from two World Bank datasets
    and merge into one data frame

    :param filename1: first csv file
    :param filename2: second csv file
    :return: data frame
    """
    # Read in data into data frame
    data_df = pd.read_csv(filename1, usecols=['Country Name', 'Country Code', '2018'], index_col=False)
    meta_df = pd.read_csv(filename2, usecols=['Country Code', 'Region', 'IncomeGroup'], index_col=False)

    # Change column names
    data_df.columns = ['CountryName', 'CountryCode', 'Population']
    meta_df.columns = ['CountryCode', 'Region', 'Income']

    # Join two data frames
    df_join = pd.merge(data_df, meta_df, on='CountryCode', how='left')

    # Clean data
    # remove rows with country names not classified
    df_join = df_join.drop(df_join[df_join.CountryName == 'Not classified'].index)
    # remove 'income' from Income column
    df_join['Income'] = df_join['Income'].str.replace('income', '')

    # Export data frame to csv file
    # df_join.to_csv('WorldBank_merged.csv', index=False, header=True)

    return df_join


## Test if the function works
if __name__ == '__main__':
    filename1 = "World_Bank_Data.csv"
    filename2 = "World_Bank_Metadata.csv"

    df = read_worldbank_data(filename1, filename2)
    print(df.head())