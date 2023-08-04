# CEI_Project
The State of Illinois Commision on Equity and Inclusion (CEI) created the <a href = "https://cei.illinois.gov/business-enterprise-program.html">Business Enterprise Program (BEP)</a> for businesses owned by minorities, women, and persons with disability to foster an inclusive, equitable and competitive business environment that will support underrepresented businesses increase their capacity, grow revenue, and enhance credentials. The state is engaging with private businesses for goods and services through public procurement, and historically, minority-owned businesses are underrepresented in the procurement processes. One of BEP's goal is to provide opportunities for minority-owned businesses to be eligible for public procurement. 

The state’s annual, aggregated aspirational goal is to spend at least 30% of its total non-construction and non professional services dollars with firms certified through BEP. This overall goal is allocated as follows: 
Group | Goal
------------- | -------------
Minority Business Enterprise (MBE)  | 16%
Women Business Enterprise (WBE)  | 10%
Persons with Disability Business Enterprise (PBE) | 4%

The state’s annual, aggregated aspirational goal for construction and professional services contracts is to spend not less than 20% of total dollars with BEP firms. This overall goal is allocated as follows: 
Group | Goal
------------- | -------------
Minority Business Enterprise (MBE)  | 11%
Women Business Enterprise (WBE)  | 7%
Persons with Disability Business Enterprise (PBE) | 2%


In the <a href = "https://cei.illinois.gov/content/dam/soi/en/web/cei/documents/bep-annual-reports/FY22%20Business%20Enterprise%20Program%20Annual%20Report.pdf">2022 Annual Report</a>, BEP set an ambitious goal of $14,130,167,167, which represents a substantial 185% increase from the $4,955,174,823 target in 2021. Although BEP achieved a higher overall dollar amount in 2022, reaching $1,156,587,597 compared to $885,489,466 in 2021, it became evident that attaining 20-30% of the new goal proved to be more challenging. Furthermore, the achievement rate for 2022 was recorded at 8.2%, which is notably lower than the achievement rate of 17.9% in 2021. This significant decline in the achievement percentage further emphasizes the increased difficulty in reaching the specified target during the mentioned year.

 Totals | 2021 | 2022 | remarks
 -|-|-|-
 Dollars Subject to Goal - DSG | $ 4,955,174,823 | $ 14,130,167,167 | ⬆️ +185.2%
 BEP Achievement | $ 885,489,466 |  $ 1,156,587,597
 BEP % Achievement | 17.9% | 8.2% | ⬇️

This project aims to help CEI to:
1. Explore BEP's current contracting with minority owned firms by mapping existing BEP-certified minority owned businesses database through geospatial analysis
2. Increase BEP participation through analyzing IL demographics (general and business-related) through geospatial analysis, to identify where to potentially expand CEI's efforts (eg. stakeholder outreach, professional consultation, capacity building, new partnerships)
3. Monitor goal by providing internal dashboard/tracker that will allow CEI to proactively see their goal achievement in a more frequent manner, and adjust their operational efforts throughout the fiscal year (work in progress)

Community Data Fellows directly collaborate with **Bruce Montgomery (Acting CEI Commissioner)** during Spring and Summer 2023.

## Files in /data/input directory:
1. Directory_BEP.csv: list of certified businesses in the State of Illinois downloaded from <a href = "https://ceibep.diversitysoftware.com/">public online directory</a> on 06/20/2023
2. Directory_BEP_noduplicates.csv: cleaner version of list of certified businesses -no duplicates per address
3. IL_census_data: Census data including population, education, income by census track. Data downloaded from <a href = "https://www.socialexplorer.com/explore-tables"> Social Explorer </a>
4. county_business_patterns_2021: business-related statistics from census bureau. This includes number of establishments, employment, payroll, average wage, by geographic area, NAICS industry, and size of establishment. Data downloaded from <a href = "https://www.socialexplorer.com/explore-tables"> Social Explorer </a>
5. tl_2022_17_tract.shp: Illinois state shape file by census track
6. IL_bounds_county_Py.shp: Illinois state shape file by county
7. Dashboard_Raw_Data.xlsx: multi-fiscal year report including Budget, Exemptions, and Dollars Subject to Goal (DSG) --this is a file shared by CEI

## Files in /data/output directory:
1. certified_businesses_map.html: map of BEP certified businesses as of 06/20/2023
2. 

## Files in /codes directory:
1. Visualization.R: R codes for creating different types static visualizations (e.g. heatmap, faceted line charts, spatial plots); continuously maintained and updated with codes for more plots (**work in progress -to be converted to python**)
2. Geocoding.py: codes for generating geocodes for each business (**work in progress -to be edited**)
3. Mapping.ipynb: codes to map each certified business (**work in progress -to be migrated to main file**)
4. External_data.ipynb: codes for mapping census data (**work in progress -to be migrated to main file**)
5. business_patterns.ipynb: codes for mapping business patterns (**work in progress -to be migrated to main file**)

## Google Drive: (insert link) -**work in progress**
1. 


## How to Run this **work in progress**
1. 
2.
3.
4. 


Repository Structure:
│   Dockerfile
│   README.md
│   requirements.txt
│   
├───codes
│   │   Visualization.R
│   │   
│   └───utils
│           cleaning.py
│           geocoding.py
│           tree_output.txt
│           vizualizing.py
│           __init__.py
│           
├───data
│   ├───cache
│   ├───clean
│   │       certified_businesses_map.html
│   │       cleaned_raw.csv
│   │       combined_df.csv
│   │       geocoded_loc_raw.json
│   │       
│   └───raw
│           directory_certified_businesses.csv
│           IL_BNDY_County_Py.shp
│           IL_business_data.csv
│           IL_census_data.csv
│           test_data_directory.csv
│           
└───notebooks
        bep_demographics_and_business.ipynb
        bep_geocoding.ipynb
        bep_mapping.ipynb

