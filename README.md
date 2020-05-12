# Project Name: Where did the exotic artefacts come from in art museums in USA?
# Team members:
Yingying Han  
Xinyu Huang  
Jenna Kim
# Research questions and hypothesis:
(1) What is the distribution of museum artifacts that originate from USA?  
(2) How many artifacts are from countries outside USA? What are those countries?  
(3) Is there a correlation between the number of artifacts with one ethnicity and the population of that ethnicity in & outside USA?  
(4) What is the distribution of artifacts over time?  
# Raw Data:
(1) Museum datasets:
The project has analyzed museum metadata from the Metropolitan Museum of Art (MET) and Indianapolis Museum of Art (IMA). Both the museums have make their metadata open access on the Github.  
Metropolitan Museum of Art (MET): https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv  
Indianapolis Museum of Art (IMA): https://github.com/american-art/ima/blob/master/aac-objects/aac-objects.json  

(2) The worldwide population dataset is downloaded from world bank at https://data.worldbank.org/indicator/sp.pop.totl.  

(3) The American ethnicity dataset is downloaded from U.S. Census Bureau website at https://data.census.gov.  

# Data pre-processing and cleaning
(1) Museum datasets
Please find the code in "museum_data.py": The first two functions in this script extract fields related to geographic location and object date from two raw museum metadata sets. The results are in "met_data_for_analysis.zip" and "ima_data_for_analysis.csv" in Data/Processed folder.

Since geographic location data and date data has many quality issues, such as inconsistency, inaccuracy, the team members used OpenRefine to clean the data. The clean datasets are in "ima_data_for_analysis-clean.csv" and "met_data_for_analysis-clean.csv" in Data/Processed folder.

Please find the code in "museum_data.py". The third function merges two clean datasets ("ima_data_for_analysis-clean.csv" and "met_data_for_analysis-clean.csv")to one for future analysis. The merged dataset names "museum.csv".

(2) Population dataset
Please find the code in "museum_data.py": The fourth function in this script extracts out the population data in 2018 for future analysis. The final population dataset names "world_bank.csv".

(3) American ethnicity dataset
Please find the code in "museum_data.py": The fifth function in this script clean the ethnicity dataset by dropping the blank columns and discarding rows of margin error. The clean ethnicity data names "ethnicity.csv".

# Data analysis
Please find the codes in "IS590PRSP20_Final_Proejct.ipynb". The analysis are conducted from two aspects: 
(1)Distribution of artifacts by geographical information
(2)Distribution of artifacts by time

# Conclusion
## (1) What is the distribution of museum artifacts that originate from USA?
The result is shown in Image 1. 

## (2) How many artifacts are from countries outside USA? What are those countries?  
The result is shown in Image 2.

## (3) Is there a correlation between the number of artifacts with one ethnicity and the population of that ethnicity in & outside USA? 
The results are shown in Image 3 and Image 4.

## (4) What is the distribution of artifacts over time?  
      a. How many objects were created before year zero, in year zero, and after year zero?
      The result is shown in Image 5.
      
      b. What is the year distribution of objects created before year zero?
      The result is shown in Image 6.
      
      c. What is the century distribution of objects created after year zero?
      The result is shown in Image 7.
      
      d. 
      
      
     
