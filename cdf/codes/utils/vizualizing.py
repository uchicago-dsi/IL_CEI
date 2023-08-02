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


def selecting_keys(data):
    '''
    input: extracted geocdes -json file
    output: folium map
    '''
    file_path_raw = data
    # Step 1: Read existing JSON data from the file (if it exists)
    with open(file_path_raw, 'r') as json_file:
        data = json.load(json_file)

    data_list = list(data.items())
    
    
    color = {'MBE': 'green', 
         'WBE': 'blue', 
         'WMBE': 'yellow', 
         'SDVOSB':'orange', 
         'VBE': 'black', 
         'VOSB': 'pink', 
         'BEPD': 'cadetblue',
         'PBE': 'gray',
         'SWS': 'darkred'}
    
    
    names = []
    lats = []
    lons = []
    cats = []
    colors = []
    for i, val in enumerate(data_list):
        names.append(data_list[i][0])
        lats.append(data_list[i][1][0]['lat'])
        lons.append(data_list[i][1][0]['lon'])
        cats.append(data_list[i][1][0]['category'])
        colors.append(color[data_list[i][1][0]['category']])
    
    zipped_data = zip(lats, lons, names, colors, cats)
    return zipped_data



def mapping(data):
  
    zipped_list = selecting_keys(data)
    lats, lons, names, colors, cats = zip(*zipped_list)
    lats = list(lats)
    lons = list(lons)
    names = list(names)
    colors = list(colors)
    cats = list(cats)
    
    
    map_center = [lats[0], lons[0]]
    my_map= folium.Map(location=map_center, zoom_start=10)
    
    
    # Define the boundaries of Illinois
    illinois_boundary = folium.GeoJson(
         data=open('illinois-counties.geojson').read(),
         style_function=lambda x: {'fillColor': '#ffcccc', 'color': '#000000', 'weight': 1},
     )

    # Add the Illinois boundary to the map
    illinois_boundary.add_to(my_map)


    for lat, lon, names, colors, cats in zip(lats, lons, names, colors, cats):
    #      folium.Marker([lat, lon], popup=names, icon=folium.Icon(color=colors), icon_size=(20, 20)).add_to(my_map)
        folium.CircleMarker([lat, lon], radius=4, popup=[names, cats], color=colors, fill=True, fill_color=colors).add_to(my_map)

    # Create a dictionary of colors and their respective labels
    # color_labels = {color: names for color, label in zip(colors, names)}

    # Create the legend
    legend_html = '''
         <div style="position: fixed;
                     bottom: 10px; left: 10px; width: 100px; height: 270px;
                     border:2px solid grey; z-index:9999; font-size:14px;
                     background-color:white; opacity:1.0;">

             <p style="margin: 5px;">Legend</p>
             <p style="margin: 5px;"><span style='background:green;'>&nbsp;&nbsp;&nbsp;&nbsp;</span>MBE</p>
             <p style="margin: 5px;"><span style='background:blue;'>&nbsp;&nbsp;&nbsp;&nbsp;</span>WBE</p>
             <p style="margin: 5px;"><span style='background:yellow;'>&nbsp;&nbsp;&nbsp;&nbsp;</span>WMBE</p>
             <p style="margin: 5px;"><span style='background:orange;'>&nbsp;&nbsp;&nbsp;&nbsp;</span>SDVOSB</p>
             <p style="margin: 5px;"><span style='background:black;'>&nbsp;&nbsp;&nbsp;&nbsp;</span>VBE</p>
             <p style="margin: 5px;"><span style='background:pink;'>&nbsp;&nbsp;&nbsp;&nbsp;</span>VOSB</p>
             <p style="margin: 5px;"><span style='background:cadetblue;'>&nbsp;&nbsp;&nbsp;&nbsp;</span>BEPD</p>
             <p style="margin: 5px;"><span style='background:gray;'>&nbsp;&nbsp;&nbsp;&nbsp;</span>PBE</p>
             <p style="margin: 5px;"><span style='background:darkred;'>&nbsp;&nbsp;&nbsp;&nbsp;</span>SWS</p>

         </div>
    '''

    my_map.get_root().html.add_child(folium.Element(legend_html))

    return my_map