# Indianapolis Museum of Art Data Documentation

## Describe the authorship, attribution, and/or the provenance of the file.  
The data was created by staffs in Indianapolis Museum of Art.

## Provide all attribution available to you about the file.  Even if you’ve made the file yourself, provide attribution about the content and the source you gathered it from. I expect you to go beyond the minimum legal requirements for this.
#### https://github.com/american-art/ima/blob/master/LICENSE

## Describe the semantic contents of the file.
#### There are three files in this dataset: IMA-Objects-Creation-Location-data.csv, IMA-Objects-data.csv, aac-objects.json. These three files
include basic descriptive metadata of IMA objects, for example, title, created date, created geographic location, etc. 

## A short plain language statement about what the data file contains, this should be very much along the lines of a domain description.
#### File "IMA-Objects-Creation-Location-data.csv" includes geographic location information of objects. 
In IMA-Objects-Creation-Location-data.csv file, there are five fields: object ID, country, state, district, and city. 
In all, there are 11348 records in this file. 

#### File "IMA-Objects-data.csv" includes descriptive information of object.
There are 27 fields in this file: ID, ACCESSION_NUMBER,PREVIOUS_ACCESSION_NUMBER, DATE_ACCESSION, LINK, RECORD_TYPE, OBJECT_TYPES,
TITLE, DATE_CREATED, DATE_EARLIEST, DATE_LATEST, DESCRIPTION, CREDIT_LINE, MEDIUM_SUPPORT,MEDIUMS, SUPPORTS. TECHNIQUE,
COLLECTION_AREA, Collection_ID, Collection_Name, ACTORS, CONVERTED_DIMENSIONS, NUMBER_OF_PARTS, PART_NUMBER, RIGHTS, 
RECORD_UPDATED, IMAGEURL.
In all, there are 11095 records in this file. 

#### (We probably only need to analyze this file) File "aac-objects.json"
There are 53 fields in this file, including id, type, title, date_created, date_earlist, date_latest, creation period, creation_city, creation_state, 
creation_country, creation_district, culture, nationalities, etc. 

## A short statement about what is being used from this dataset.
We probably only need to analyze the file "aac-objects.json". In this file, we will extract the geographic data from fields 
"creation_city", "creation_state", "creation_country", "creation_district". We will extract object date information from fields 
"date_created", "date_earlist", "date_latest".
In all, there are 11157 records in this file. 

## Relevant dates of the data collection.
Published in 2017.

## Describe the collection process.
Download from https://github.com/american-art/ima/tree/master/aac-objects

## Description of the data structure

### What data format is this file stored in?
two csv files and one json file (we probabaly would analyze this json file only). 

## What are the records/entities within this data file? What do they represent? 
Each record represents information an object. 

### Describe the dimensions of the data.  How many records are there? How many properties about each record are there?
11157 records in this file. Each record, there are 27 properties in it. 

## How we might going to analyze the file?
### In terms of geographic data
we will finally want country, state, continent information. 
However, in this dataset, there is no continent information as well as most state information might be missing (need further verification).
Thus, we need a programming library which can find out the continent information based on the ingested country information. 
If city information exist, how do we get state information from city name and country name?

### In terms of date information
we will use "date_created" information first. If this field is missing, we wil use "date_earlist" field.
If both fields are missing, we will use "date_latest" field. 

## Reason for missing values and the relevant missing values or codes

## Number of known missing values within this column

## What are all the unique values and their meaning? (if you have categorical data).  Don’t do this if there are more than like 10 or 20.

## Need feedback from Jenna and Xinyu on "How we might going to analyze the file?" part.
