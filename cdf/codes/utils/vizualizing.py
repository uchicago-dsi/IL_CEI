import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import json
import folium
from geopy.geocoders import Nominatim
from folium import plugins


# cleaned_data = gpd.read_file("C:/Users/user/Downloads/DSI/CEI v2/cleaned_raw.csv")

def plotting(cleaned_data):

    #variable of interest
    cols = ['Population Density (Per Sq. Mile)', 'Total Population','Total Population: Male', 'Total Population: Female','Number of Employees for All Establishments', 
            'Number of All Establishments for All Sectors', 
        'Total Annual Payroll: All Establishments', 'Average Employee Wage: All Establishments', 
        'Number of All Establishments: Construction of Buildings', 'Number of All Establishments: Heavy and Civil Engineering Construction',
        'Number of All Establishments: Paper Manufacturing','All Establishments: Agriculture, Forestry, Fishing and Hunting',
       'Number of Employees for All Establishments: Utilities', 'Number of Employees for All Establishments: Specialty Trade Contractors',
        'Number of Establishments with 1 to 4 Employees: Total for All Sectors']
    for col in cols:
        fig, ax = plt.subplots(figsize=(10, 10))

        cleaned_data.plot(column=col, cmap='YlGnBu', edgecolor='black', linewidth=0.08, ax=ax, legend=True)

        # Customize the plot
        ax.set_title(col)
        ax.axis('off')

        # Display the plot
        plt.show()

        
###################################### MAPPING BEP CERTIFIED BUSINESSES #################################

        