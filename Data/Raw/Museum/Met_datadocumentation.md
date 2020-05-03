# The Metropolitan Museum of Art  Data Documentation
The data is available from https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv.
It is too huge that I am unable to download it.

## Describe the authorship, attribution, and/or the provenance of the file.  
The data was created by staffs in The Metropolitan Museum of Art.

## Provide all attribution available to you about the file.  Even if you’ve made the file yourself, provide attribution about the content and the source you gathered it from. I expect you to go beyond the minimum legal requirements for this.
#### https://github.com/american-art/ima/blob/master/LICENSE

## Describe the semantic contents of the file.
#### CCO (https://github.com/metmuseum/openaccess/blob/master/LICENSE)

## A short plain language statement about what the data file contains, this should be very much along the lines of a domain description.
File "MetObjects.csv" includes basic descriptive information of museum objects in MET, including geographic information, created date
information, object title, etc.

There are 51 fileds.
['Object Number', 'Is Highlight', 'Is Public Domain', 'Is Timeline Work', 'Object ID', 'Department', 'AccessionYear', 'Object Name', 'Title', 'Culture', 'Period', 'Dynasty', 'Reign', 'Portfolio', 'Artist Role', 'Artist Prefix', 'Artist Display Name', 'Artist Display Bio', 'Artist Suffix', 'Artist Alpha Sort', 'Artist Nationality', 'Artist Begin Date', 'Artist End Date', 'Artist Gender', 'Artist ULAN URL', 'Artist Wikidata URL', 'Object Date', 'Object Begin Date', 'Object End Date', 'Medium', 'Dimensions', 'Credit Line', 'Geography Type', 'City', 'State', 'County', 'Country', 'Region', 'Subregion', 'Locale', 'Locus', 'Excavation', 'River', 'Classification', 'Rights and Reproduction', 'Link Resource', 'Object Wikidata URL', 'Metadata Date', 'Repository', 'Tags', 'Tags AAT URL']


## A short statement about what is being used from this dataset.
In this file, we will extract the geographic data from fields 
"geographic type", "city", "state", "county", "country", "region", "subregion", "locale", "locus", "artisist nationality".

We will extract object date information from fields 
"period", "artist begin date", "artist end date", "Object date", "Object begin date", "Object end date".

In all, there are 474439 records in this file. 

## Relevant dates of the data collection.
Published in 2020.

## Describe the collection process.
Download from https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv

## Description of the data structure

### What data format is this file stored in?
One csv file.

## What are the records/entities within this data file? What do they represent? 
Each record represents information an object. 

### Describe the dimensions of the data.  How many records are there? How many properties about each record are there?
474439 records in this file. Each record, there are 51 properties in it. I suppose 17 fields might be helpful for analysis.
I wrote a short program named "metdata_extract_important_field.py" and the important field imformation has been saved in 
"mets_important_field.csv"

## How we might going to analyze the file?
### In terms of geographic data
We might need to screen the geographic information via "geographic type" and then extract the country information. If latitude/longitude numbers are offered, we can run some libaray and get the continent, state, country, or even city information.

### In terms of date information
we will use "Object Date" field. If it is missing, we can consider "Object Begin Date", "Object End Date". If all missing, we can consider "Artist Begin Date" and "Artist End Date".

## Reason for missing values and the relevant missing values or codes

## Number of known missing values within this column

## What are all the unique values and their meaning? (if you have categorical data).  Don’t do this if there are more than like 10 or 20.

