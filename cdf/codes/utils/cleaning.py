import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def rename_cens(census):
    census.rename(columns={"County Name": "Qualifying Name"}, inplace=True)
    census['Qualifying Name'] = census['Qualifying Name'].str.lower()
    census.iloc[:, 1:] = census.iloc[:, 1:].replace(',', '', regex=True)
    return census


def rename_bus(business):
    business.rename(columns={'County': 'CO_FIPS'}, inplace=True)
    business['Qualifying Name'] = business['Qualifying Name'].str.lower()
    business.iloc[:, 1:] = business.iloc[:, 1:].replace(',', '', regex=True)
    return business
    
    
def merge_census_business(census, business):
    combined_df = pd.merge(rename_cens(census), rename_bus(business), on="Qualifying Name", how="outer")

    # Convert all data in the DataFrame into numbers
    for col in combined_df.columns[1:]:
        combined_df[col] = pd.to_numeric(combined_df[col], errors='coerce')
    combined_df.to_csv("../data/clean/combined_df.csv", index=False)
    return combined_df



def merge_geo(census, business, bounds):
    merged_df = merge_census_business(census,business).merge(bounds, on="CO_FIPS", how='outer')
    merged_gdf = gpd.GeoDataFrame(merged_df, geometry=merged_df.geometry)
    merged_gdf.to_csv("../data/clean/cleaned_raw.csv")
    return merged_gdf
