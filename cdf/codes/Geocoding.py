import pandas as pd
import json
import folium
from geopy.geocoders import Nominatim
import requests
import time
import matplotlib.pyplot as plt
from folium import plugins

#Part 1: Geocoding and Mapping BEP Certified Businesses


url = 'https://github.com/uchicago-dsi/IL_CEI/tree/Angelica_Sun_main_update/cdf/data/input/Directory_BEP.csv'
df = pd.read_csv(url)


#Check stats

category_counts = df['Certification Type'].value_counts()
category_counts = category_counts.sort_values(ascending=True)
ax=category_counts.plot(kind='barh')

plt.xlabel('Count')
plt.ylabel('Certification Type')
plt.title('Certification Type Count')

for i, v in enumerate(category_counts):
    ax.text(v + 0.2, i, str(v), color='black', va='center')
    
plt.show()



def extracting_location (addresses_name):
    """
    input: address list
    output: geocodes of the addresses
    """
    info={}
    for address, name in addresses_name:
        # Define the URL for Nominatim API
        url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json&limit=1"
            # Make the request with a timeout of 5 seconds
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            info[name]=data
        except requests.exceptions.RequestException as e:
            continue
    print ("total info:", len(info))
    return info


#optional -- Since nominatim can only extract a few geocodes per request, slice the dataframe into smaller datasets. Exploring other geocoders is also an option
#suggested to breakdown per certification type


def slicing_df(df):
    """
    """
    categories = ['MBE', 'WBE', 'WMBE', 'SDVOSB', 'VBE', 'VOSB', 'BEPD', 'PBE', 'SWS']
    dataframes = {}  # Dictionary to store the dataframes
    for cat in categories:
        cat_data = df.loc[df['Certification Type'] == cat]  # Filter data based on the category
        print(cat, len(cat_data))
        dataframes[cat] = cat_data  # Store the dataframe in the dictionary

    # Access the individual dataframes
    MBE_data = dataframes['MBE']
    WBE_data = dataframes['WBE']
    WMBE_data = dataframes['WMBE']
    SDVOSB_data = dataframes['SDVOSB']
    VBE_data = dataframes['VBE']
    VOSB_data = dataframes['VOSB']
    BEPD_data = dataframes['BEPD']
    PBE_data = dataframes['PBE']
    SWS_data = dataframes['SWS']



def converting_to_json(sliced_file):
    """
    this is to save files with geocodes to json
    input: sliced df (for nominatim)
    output: json file (no return), only saving in the file path
    """

    extract=sliced_file
    file_path = "/path_to_file.json"
    #udpate this file path

    # Open the file in write mode and save the dictionary as JSON
    with open(file_path, 'w') as json_file:
        json.dump(extracting_location(extract), json_file)

        
#optional -- Combine Json files for categories sliced and geocoded multiple times (due to geocoding limitation per run)


        
        

        
