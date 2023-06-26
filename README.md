# CEI_Project
(work in progress)

## Files in /data repository:
1. Directory_2023-06-20_241.csv: list of certified businesses in the State of Illinois downloaded from <a href = "https://ceibep.diversitysoftware.com/">public online directory</a> on 06/20/2023
2. Directory_2023-06-20_241_nodupl.csv: cleaner version of list of certified businesses -no duplicates per address
3. Dashboard_Raw_Data.xlsx: multi-fiscal year report including Budget, Exemptions, and Dollars Subject to Goal (DSG)

## Files in /codes repository
1. Visualization.R: R codes for creating different types static visualizations (e.g. heatmap, faceted line charts, spatial plots); continuously maintained and updated with codes for more plots.
2. nominatim_extractor.ipynb: codes for generating geocodes for each business
3. combining_jsons.ipynb: used to combine different sets of geocodes (broken down per certification type)
4. Mapping.ipynb: codes to map each certified business


Joseph Jaiyeola 