import pandas as pd
import json
from geopy.geocoders import Nominatim
import requests


#Part 1. Cleaning: Keeping Addresses and Names only

df = pd.read_csv("../data/input/Directory_BEP.csv")

categories = ['VBE', 'VOSB', 'BEPD', 'PBE', 'SWS']
#categories = ['MBE', 'WBE', 'WMBE', 'SDVOSB', 'VBE', 'VOSB', 'BEPD', 'PBE', 'SWS']

def slicing_df(df):
    """
    This function reorganize the dataset by category type. The purpose of doing this is for easier geocoding and visualization
    Input: raw pandas df
    Output: Dictionary of Category_Type with list of tuples of Addresses and Company Names -- {Category1: [(Address1, Company1), (Address2, Company2)]...}
    """
    dataframes = {} 
    for cat in categories:
        filtered_df = df[df['Certification Type'] == cat] #filter data based on category
        filtered_df = filtered_df[['Address', 'Company Name']] #keep Address and Company Name only
        result_list = [tuple(row) for row in filtered_df.values] #
        dataframes[cat]= result_list
    return dataframes



#Part 2: Geocoding 

def extracting_location (addresses_name):
    """
    input: list of address and names
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


#Part 3: Mapping
        

        
