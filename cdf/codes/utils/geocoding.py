import pandas as pd
import json
from geopy.geocoders import Nominatim
import requests

data = pd.read_csv("..data/raw/directory_certified_businesses.csv") 

#categories = ['VBE', 'VOSB', 'BEPD', 'PBE', 'SWS']
categories = ['MBE', 'WBE', 'WMBE', 'SDVOSB', 'VBE', 'VOSB', 'BEPD', 'PBE', 'SWS']


def slicing_df(data):
    """
    This function reorganize the dataset by category type. The purpose of doing this is for easier geocoding and visualization
    Input: raw pandas df
    Output: dictionary of Category_Type with list of tuples of Addresses and Company Names -- {Category1: [(Address1, Company1), (Address2, Company2)]...}
    """
    dataframes = {} 
    for cat in categories:
        filtered_df = data[data['Certification Type'] == cat] #filter data based on category
        filtered_df = filtered_df[['Address', 'Company Name']] #keep Address and Company Name only
        result_list = [tuple(row) for row in filtered_df.values] #
        dataframes[cat]= result_list
    return dataframes



def extracting_location(data):
    """
    input: list of tuples of (address, company name)
    output: dictionary of Company Names with geocode information 
    """
    geocodes = {}
    sliced = slicing_df(data)
    for cat in categories:
        addresses_name = sliced[cat]
        info = {}
        for address, name in addresses_name:
        # Define the URL for Nominatim API
            url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json&limit=1"
                # Make the request with a timeout of 5 seconds
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                data = response.json()
                if len(data) > 0:
                     data[0]['category'] = cat
                else: 
                     continue
          
                info[name]=data
      
            except requests.exceptions.RequestException as e:
                continue
        geocodes.update(info)
    
    return geocodes




def save_geocodes(data):
    '''
    input: extracted info
    output: json file
    '''
    file_path_raw = "../data/clean/geocoded_loc_raw.json"
    new_data = extracting_location(data)

    try:
        # Step 1: Read existing JSON data from the file (if it exists)
        with open(file_path_raw, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list
        existing_data = {}
        
   
    existing_data_list = list(existing_data.items())
    new_data_list = list(new_data.items())

    #If new data is not in the existing data list, add it
    for company in new_data_list:
        if company not in existing_data_list:
            existing_data_list.append(company)
            
    existing_data_updated = dict(existing_data_list)
    
    # Write the updated data back to the JSON file
    with open(file_path_raw, 'w') as file:
        json.dump(existing_data_updated, file, indent=2)

        
        
        
        
