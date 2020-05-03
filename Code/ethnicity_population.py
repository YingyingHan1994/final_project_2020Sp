"""
IS590PR: Final Project
Written by: Xinyu Huang

This part will extract American Ethnicity population data from cvs dataset derived from data.census.gov

Currently contains two dataset:
    Asian Alone Ethnicity in U.S.
    First Ancestry in U.S

                     Ethnicity Population
0                        Total   17574550
1                 Asian Indian    3852293
2                  Bangladeshi     169835
...

                  Ethnicity Population
0                    German   33133923
1            German Russian      17790
2                     Greek    1020770
3                  Guyanese     196705
...

Source:  U.S. Census Bureau, 2014-2018 American Community Survey 5-Year Estimates
"""

import pandas as pd
import re


def join_ACS_meta_data(filepath_data, filepath_metadata):
    '''
    Combine the U.S. ethnicity metadata downloaded from U.S. Census Bureau into one pandas DataFrame
    :param filepath_data: the path of the 'data_with_overlays'.csv file
    :param filepath_metadata: the path of the 'metadata'.csv file
    :return: a pandas DataFrame, columns={'Ethnicity', 'Population'}, recommend to use regular expression to
                match the ethnicity because of some annotations inside the cell
    '''
    ACS_data = pd.read_csv(filepath_data, index_col='GEO_ID').T
    ACS_metadata = pd.read_csv(filepath_metadata, index_col='GEO_ID')

    merged_data = pd.merge(ACS_data, ACS_metadata)

    # drop the blank column
    for i in merged_data.columns:
        if merged_data[i].count() == 0:
            merged_data.drop(labels=i, axis=1, inplace=True)

    # cleaning the table
    merged_data = merged_data[merged_data["id"].str.contains('Estimate')]  # discard rows of margin error
    re_expression = re.compile('Estimate!!(.+)')
    merged_data['id'] = merged_data['id'].str.replace(re_expression, r'\1')
    re_expression = re.compile('Total!!(.+)')
    merged_data['id'] = merged_data['id'].str.replace(re_expression, r'\1')
    merged_data.columns = ['Ethnicity', 'Population']
    merged_data.reset_index(drop=True, inplace=True)
    print(merged_data)

    return merged_data


if __name__ == '__main__':
    file_data1 = '../Data/Ethnicity/ethnicity_asian_alone/ACSDT5Y2018.B02015_data_with_overlays_2020-05-01T221237.csv'
    file_metadata1 = '../Data/Ethnicity/ethnicity_asian_alone/ACSDT5Y2018.B02015_metadata_2020-05-01T221237.csv'
    join_ACS_meta_data(file_data1, file_metadata1)

    file_data2 = '../Data/Ethnicity/ethnicity_first_ancestry/ACSDT5Y2013.B04001_data_with_overlays_2020-05-01T222006.csv'
    file_metadata2 = '../Data/Ethnicity/ethnicity_first_ancestry/ACSDT5Y2013.B04001_metadata_2020-05-01T222006.csv'
    join_ACS_meta_data(file_data2, file_metadata2)

