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
The result is shown in Image 1 titled "States1".  
![Image of Yaktocat](https://github.com/YingyingHan1994/final_project_2020Sp/blob/master/images/states_distribution.png)

## (2) How many artifacts are from countries outside USA? What are those countries?  
The result is shown in Image 2 titled "Count".
![Image of Yaktocat](https://github.com/YingyingHan1994/final_project_2020Sp/blob/master/images/country_distribution.png)

## (3) Is there a correlation between the number of artifacts with one ethnicity and the population of that ethnicity in & outside USA? 
![Image of Yaktocat](https://github.com/YingyingHan1994/final_project_2020Sp/blob/master/images/correlation_with_population.png)
![Image of Yaktocat](https://github.com/YingyingHan1994/final_project_2020Sp/blob/master/images/correlation_with_ethnicity.png)

## (4) What is the distribution of artifacts over time?  
a. How many objects were created before year zero, in year zero, and after year zero?
      The result is shown in Image 5.
      ![Image of Yaktocat](https://github.com/YingyingHan1994/final_project_2020Sp/blob/master/images/year_zero_distribution.png)
      We found that 415316 object were created after year Zero and year value range from year 1 to year 2020.  
      There are a huge amount of objects were created after Year Zero (# 415316), however, the year values cover from year 1 to year 2020 only.  
      1253 objects were created in year zero.  
      
b. What is the year distribution of objects created before year zero?
      The result is shown in Image 6.
      ![Image of Yaktocat](https://github.com/YingyingHan1994/final_project_2020Sp/blob/master/images/bc_distribution.png)  
      We found most of the objected before year zero were created between 2500 BC to year zero.  
      
c. What is the century distribution of objects created after year zero?
      The result is shown in Image 7 and Image 8.
      ![Image of Yaktocat](https://github.com/YingyingHan1994/final_project_2020Sp/blob/master/images/century_distribution.png)
      ![Image of Yaktocat](https://github.com/YingyingHan1994/final_project_2020Sp/blob/master/images/century_pie.png)
      
   We found over half of the objects after year zero were created after 19 century.  
      
d. How many objects are created after (including) 19th century? and what is the year distribution?
      The result is shown in Image 8 and Image 9.
      ![Image of Yaktocat](https://github.com/YingyingHan1994/final_project_2020Sp/blob/master/images/after19century_distribution_halfcentury.png)
      
      We found most of the objects created after 19 century were created between 1850 to 1950.  
      If we distribute the year value by every 25 years, the result is as follows:  
      
![Image of Yaktocat](https://github.com/YingyingHan1994/final_project_2020Sp/blob/master/images/after19century_distribution_25years.png)
      
e. In terms of those objects created in Egypt, how many of them were created before year zero?
      ![Image of Yaktocat](https://github.com/YingyingHan1994/final_project_2020Sp/blob/master/images/egypt_object_year_distribution.png)
      ![Image of Yaktocat](https://github.com/YingyingHan1994/final_project_2020Sp/blob/master/images/egypt_pie.png)
      
      We found 82% of the objects originated from Egypt were created before year zero. It might because Egypt is an ancient counrty. So, we did the year distribution analysis to the objects from China too.
      
f. In terms of those objects created in China, how many of them were created before year zero?
      ![Image of Yaktocat](https://github.com/YingyingHan1994/final_project_2020Sp/blob/master/images/chinese_pie.png)
      
      99% of the objects from China were created after year zero. Thus, "being an ancient country" does not explain why most of the objects from Egypt were created before year zero. Further discussion is needed in the future. 
     
