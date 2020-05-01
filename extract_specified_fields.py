import csv
import json
import pandas as pd


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
    # >>> file = "https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv"
    # >>> header = ["Object ID", "Country"]
    # >>> df = extract_need_data(file, header)
    # >>> df.iloc[0][0]
    # "1"
    # >>> type(df)
    <class 'pandas.core.frame.DataFrame'>
    """
    need_data = pd.read_csv(file,
                   names = met_raw_headers,
                   header = None,
                   low_memory= False,
                   index_col= False,
                   usecols=need_headers)
    return need_data


# Extract data from The Metropolitan Museum of Art (met) raw dataset for further analysis
met_raw_data_source = "https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv"
# These are the headers we want to use in our analysis
useful_headers_met = ['Object ID','Title','Culture', 'Period','Artist Begin Date', 'Artist End Date','Object Date',
                  'Object Begin Date', 'Object End Date', 'Geography Type', 'City', 'State', 'Country']
met_data_for_analysis_df = extract_need_data(met_raw_data_source,useful_headers_met)


# Extract the data from Indianapolis Museum of Art (IMA) raw metadata for future analysis
def extract_need_data_from_json (file:json):
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
        nationalities = each_record['nationalities']
        collection_area = each_record['collection_area']
        data_for_analysis = [object_id, title, date_created, date_earliest,
                                 date_latest, creation_city, creation_state,
                                 creation_country, nationalities, collection_area]
        data_for_analysis_list.append(data_for_analysis)
    data_for_analysis_df = pd.DataFrame(data_for_analysis_list)
    return(data_for_analysis_df)

ima_data_for_analysis_df= extract_need_data_from_json ("ima_raw_data.json")
print(ima_data_for_analysis_df)


