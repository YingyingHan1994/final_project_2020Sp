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

## A short statement about what is being used from this dataset.
In this file, we will extract the geographic data from fields 
"geographic type", "city", "state", "county", "country", "region", "subregion", "locale", "locus", "artisist nationality".
(We might need to screen the geographic information via "geographic type" and then extract the country information. If latitude/longitude numbers
are offered, we can run some libaray and get the continent, state, country, or even city information).

We will extract object date information from fields 
"period", "artist begin date", "artist end date", "Object date", "Object begin date", "Object end date".

(To be confirmed) In all, there are ??? records in this file. 

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
