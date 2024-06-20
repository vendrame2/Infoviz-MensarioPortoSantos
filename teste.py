import pandas as pd
import geopandas as gpd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import geojson

geojsonFile = "./Data/raw/porto.geojson"

gdf = gpd.read_file(geojsonFile, encoding='utf-8')

with open(geojsonFile, 'r', encoding='utf-8') as file:
    geojson_data = geojson.load(file)

gdf = gpd.GeoDataFrame.from_file(geojsonFile)
print(gdf)

gdf.explore()
#import folium
#m = folium.Map(location=[-23.95606873631538, -46.30942691864801], zoom_start=12)
'''
for _, r in gdf.iterrows():
    # Without simplifying the representation of each borough,
    # the map might not be displayed
    propriedade = r["Id. Berço"]
    vetor = r["geometry"]
    #print(vetor)

    sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    #print()
    #print("data", geo_j)
    #print()
    geo_j = folium.GeoJson(data=vetor, style_function=lambda x: {"fillColor": "orange"})
    folium.Popup(r["Calado"]).add_to(geo_j)
    geo_j.add_to(m)
'''