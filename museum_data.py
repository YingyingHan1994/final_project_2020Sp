import csv
import json
import re
import pandas as pd

## Collect data and extract info needed for analysis

## 1. Museum dataset
## A) The Metropolitan Museum of Art (MET)
met_raw_headers = ['Object Number', 'Is Highlight', 'Is Public Domain', 'Is Timeline Work', 'Object ID',
           'Department', 'AccessionYear', 'Object Name', 'Title', 'Culture', 'Period', 'Dynasty',
           'Reign', 'Portfolio', 'Artist Role', 'Artist Prefix', 'Artist Display Name', 'Artist Display Bio',
           'Artist Suffix', 'Artist Alpha Sort', 'Artist Nationality', 'Artist Begin Date', 'Artist End Date',
           'Artist Gender', 'Artist ULAN URL', 'Artist Wikidata URL', 'Object Date', 'Object Begin Date',
           'Object End Date', 'Medium', 'Dime Bnsions', 'Credit Line', 'Geography Type', 'City', 'State', 'County',
           'Country', 'Region', 'Subregion', 'Locale', 'Locus', 'Excavation', 'River', 'Classification',
           'Rights and Reproduction', 'Link Resource', 'Object Wikidata URL', 'Metadata Date', 'Repository', 'Tags',
           'Tags AAT URL']

def extract_need_data (file, need_headers: list):
    """
    Given a file storing raw data, extract the records under specified fields for future analysis.
    :param file: This is a file storing raw museum metadata. It can be an online link, a csv file, etc.
    :param need_headers: This is a list, in which stores the fields that are going to be analyzed in the project.
    :return: All records under specified fields will be returned in the format of a dataframe.
    >>> import pandas as pd
    >>> file = "museum.csv"
    >>> header = ["ObjectID", "Title"]
    >>> df = extract_need_data(file, header)
    >>> type(df)
    <class 'pandas.core.frame.DataFrame'>
    """
    need_data = pd.read_csv(file,
                   low_memory= False,
                   index_col= False,
                   usecols=need_headers)
    return need_data

## B) Indianapolis Museum of Art (IMA)
def extract_need_data_from_json (file:json):
    """
    Given a museum raw metadata file downloaded from Indianopolis Museum of Art, this function return a dataframe with
    8 columns. The 8 columns are: "ObjectID", "Title", "ObjectDate", "ObjectBeginDate","ObjectEndDate", "City",
    "State","Country".
    :param file: A museum raw metadata file downloaded from Indianopolis Museum of Art
    :return: A dataframe with 8 columns.
    >>> file = "ima_raw_data.json"
    >>> df = extract_need_data_from_json(file)
    >>> title_list = df["Title"].tolist()
    >>> title_list[0]
    'evening dress'
    """
    f = open(file, "r")
    data = json.load(f)
    all_records = data['data']
    data_for_analysis_list = []
    for each_record in all_records.values():
        object_id = each_record['id']
        title = each_record["title"]
        date_created = each_record["date_created"]
        date_earliest = each_record["date_earliest"]
        date_latest = each_record["date_latest"]
        creation_city = each_record["creation_city"]
        creation_state = each_record["creation_state"]
        creation_country = each_record["creation_country"]
        # collection_area = each_record['collection_area']
        data_for_analysis = [object_id, title, date_created, date_earliest,
                                 date_latest, creation_city, creation_state,
                                 creation_country]
        data_for_analysis_list.append(data_for_analysis)
    data_for_analysis_df = pd.DataFrame(data_for_analysis_list,
                                        columns= ["ObjectID", "Title", "ObjectDate", "ObjectBeginDate",
                                 "ObjectEndDate", "City", "State",
                                 "Country"],
                                        )
    return(data_for_analysis_df)

## C) Merge data from two files into one data frame
def merge_met_ima(filename1, filename2):
    """
    Merge data from two csv file (MET & IMA) with different structures
    into one data frame

    :param filename1: a csv file
    :param filename2: a csv file
    :return: a pandas data frame
    """
    met_headers = ['ObjectID', 'Title', 'ObjectDate', 'ObjectBeginDate', 'ObjectEndDate', 'City',
                   'State', 'Country 1', 'Country 2', 'Country 3', 'Country 4' ,'Country 5']
    ima_headers = ['ObjectID', 'Title', 'ObjectDate', 'ObjectBeginDate', 'ObjectEndDate', 'City',
                   'State 1', 'State 2', 'State 3', 'Country 1' ,'Country 2']
    new_headers = ['ObjectID', 'Title', 'ObjectDate', 'ObjectBeginDate', 'ObjectEndDate', 'City',
                   'State 1', 'State 2', 'State 3', 'Country 1' ,'Country 2', 'Country 3', 'Country 4' ,'Country 5']

    met_data_for_analysis_df = pd.read_csv(filename1, usecols=met_headers, index_col=False)
    ima_data_for_analysis_df = pd.read_csv(filename2, usecols=ima_headers, index_col=False)

    # Align structure of two data frame for concatenation
    met_data_for_analysis_df.rename(columns = {'State':'State 1'}, inplace = True)
    met_data_for_analysis_df["State 2"] = ""
    met_data_for_analysis_df["State 3"] = ""
    met_data_for_analysis_df = met_data_for_analysis_df.reindex(columns=new_headers)

    ima_data_for_analysis_df["Country 3"] = ""
    ima_data_for_analysis_df["Country 4"] = ""
    ima_data_for_analysis_df["Country 5"] = ""
    ima_data_for_analysis_df = ima_data_for_analysis_df.reindex(columns=new_headers)

    # Concatenate into one data frame.
    frames = [met_data_for_analysis_df, ima_data_for_analysis_df]
    met_ima_df = pd.concat(frames)

    return met_ima_df

## 2. World Bank Dataset
def read_worldbank_data(filename1, filename2):
    """
    This function is to read in data from two World Bank datasets
    and merge into one data frame

    :param filename1: first csv file
    :param filename2: second csv file
    :return: a pandas data frame

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
    df_join = df_join.drop(df_join[df_join.CountryName == 'Not classified'].index)
    df_join['Income'] = df_join['Income'].str.replace('income', '')

    return df_join

## 3. Ethinicity Dataset
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

## 4.  Main Function
if __name__ == '__main__':

    # 1. Museum datasets
    # 1-1. Extract data from  the Metropolitan Museum of Art (met) dataset
    met_raw_data_source = "https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv"
    # These are the headers we want to use in our analysis
    useful_headers_met = ['Object ID','Title','Object Date','Object Begin Date', 'Object End Date', 'City', 'State', 'Country']
    met_data_for_analysis_df = extract_need_data(met_raw_data_source,useful_headers_met)
    met_data_for_analysis_df = met_data_for_analysis_df.rename(columns={'Object ID': "ObjectID", "Object Date": "ObjectDate",
                                             'Object Begin Date':"ObjectBeginDate",
                                             'Object End Date': "ObjectEndDate"})

    # print(met_data_for_analysis_df.shape)
    # met_data_for_analysis_df.to_csv("met_data_for_analysis.csv")

    # 1-2. Extract the data from Indianapolis Museum of Art (IMA) metadata
    ima_data_for_analysis_df= extract_need_data_from_json ("ima_raw_data.json")
    print(ima_data_for_analysis_df.shape)
    # ima_data_for_analysis_df.to_csv("ima_data_for_analysis.csv")

    # 1-3. Clean data of two files with OpenRefine tool
    fil1 = "met_data_for_analysis-clean.csv"
    file2 = "ima_data_for_analysis-clean.csv"

    # 1-4. Concatenate two dataframes into one data frame.
    merged_df = merge_met_ima(file1, file2)
    # merged_df.to_csv("museum.csv")

    # 2. Extract data from World Bank Dataset
    filename1 = "World_Bank_Data.csv"
    filename2 = "World_Bank_Metadata.csv"
    df = read_worldbank_data(filename1, filename2)
    # print(df.head())
    # Export data frame to csv file
    # df_join.to_csv('WorldBank_merged.csv', index=False, header=True)

    # 3. Extract data from ethnicity data sets
    file_data1 = '../Data/Ethnicity/ethnicity_asian_alone/ACSDT5Y2018.B02015_data_with_overlays_2020-05-01T221237.csv'
    file_metadata1 = '../Data/Ethnicity/ethnicity_asian_alone/ACSDT5Y2018.B02015_metadata_2020-05-01T221237.csv'
    join_ACS_meta_data(file_data1, file_metadata1)

    file_data2 = '../Data/Ethnicity/ethnicity_first_ancestry/ACSDT5Y2013.B04001_data_with_overlays_2020-05-01T222006.csv'
    file_metadata2 = '../Data/Ethnicity/ethnicity_first_ancestry/ACSDT5Y2013.B04001_metadata_2020-05-01T222006.csv'
    acs_df = join_ACS_meta_data(file_data2, file_metadata2)
    # acs_df.to_csv('ethnicity.csv', index=False, header=True)
