import folium.map
import streamlit as st

from streamlit_folium import st_folium
import json
import plotly.graph_objects as go
import pandas as pd
import pprint as pp
import geopandas as gpd
import plotly.express as px
import plotly.graph_objs as go
from urllib.request import urlopen 
import geopandas as gpd
from shapely.geometry import Polygon
from folium import plugins
import folium

#ImportsProjeto
from src.utils.data import getPanoramaData as carregaDadosTerminaisPanorama

st.set_page_config(
    page_title="Port of Santos Container  Visualization",
    page_icon="🏂",
    layout="wide"
    )

import menu as menu
menu.menu()  
    
m = folium.Map([-23.95606873631538, -46.30942691864801], zoom_start=12, width=2000, height=600, position="fixed")
minimap = plugins.MiniMap()
m.add_child(minimap)


coresTipoTerminais = carregaDadosTerminaisPanorama.carregaCoresTipoTerminaisPanorama()
#st.write(coresTipoTerminais)



LocaisTerminais = carregaDadosTerminaisPanorama.DictToDatasetPanorama()

folium.TileLayer(
        tiles="https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
        attr="Google",
        name="Google Maps",
        overlay=False,
        control=True,
        subdomains=["mt0", "mt1", "mt2", "mt3"]).add_to(m)
#"SATELLITE": 
folium.TileLayer(
    tiles="https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
    attr="Google",
    name="Google Satellite",
    overlay=False,
    control=True,
    subdomains=["mt0", "mt1", "mt2", "mt3"]).add_to(m)

#"TERRAIN":
folium.TileLayer(
    tiles="https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}",
    attr="Google",
    name="Google Terrain",
    overlay=False,
    control=True,
    subdomains=["mt0", "mt1", "mt2", "mt3"]).add_to(m)
#"HYBRID":
folium.TileLayer(
    tiles="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    attr="Google",
    name="Google Satellite",
    overlay=False,
    control=True,
    subdomains=["mt0", "mt1", "mt2", "mt3"]).add_to(m)
#"ESRI":
folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Esri",
    name="Esri Satellite",
    overlay=False,
    control=True,
    subdomains=["mt0", "mt1", "mt2", "mt3"]).add_to(m)


#st.dataframe(LocaisTerminais["Terminal"])
def create_geojson_object(coordinates):
    geojson_object = {
        "type": "FeatureCollection",
        "features": []
    }

    for polygon_coords in coordinates:
        polygon_feature = {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [polygon_coords]
            },
            "properties": {}
        }
        geojson_object["features"].append(polygon_feature)

    return geojson_object


def convert_coords(poligonos):
    paths = []
    for elem in poligonos:
        coords = elem['coordenadas'].splitlines()
        path = []
        for ele2 in coords:
            ele2 = ele2.strip()
            if ele2:
                lat_lng = ele2.split(',')
                path.append([float(lat_lng[0]), float(lat_lng[1])]) #dados do panorama estão invertidos
        paths.append(path)
    return paths


tipos_carga = LocaisTerminais['Carga'].unique()
feature_groups = {tipo: folium.FeatureGroup(name=tipo) for tipo in tipos_carga}

for tipo in tipos_carga:
    for _, terminal in LocaisTerminais[LocaisTerminais['Carga'] == tipo].iterrows():


            html = "<div style='font-face:tahoma;font-size:10pt'><b> "+ terminal["Terminal"] +"</b></div><br>"
            html = html + "<div style='font-face:tahoma;font-size:9pt'><b>Coordenadas:"+terminal["Cor"]+" </b> s" + "<br>"
            html = html + "<b>R$: </b>" + "xx" + "</div>"

            iframe = folium.IFrame(html)
            popup = folium.Popup(iframe,
                                min_width=150,
                                max_width=150)
                
            
            #print("Adicionado" + terminal["Terminal"] +"à  layer" + tipo )
            folium.GeoJson(
                           
                           #carregaDadosTerminaisPanorama.coordToListTerminais(terminal["Poligonos"] ), 
                           create_geojson_object(convert_coords(terminal["Poligonos"])),
                           #process_geometry_column(terminal['Poligonos']),
                           name=terminal["Terminal"] , 
                           tooltip=terminal["Terminal"] , 
                           style_function=lambda feature, tipo=tipo: {
                                'weight': 0.1,
                                'fillOpacity': 0.6,
                    'fillColor': 'green' if tipo == 'Granel Sólido Vegetal' 
                            else 'blue'  if tipo == 'Carga Geral' 
                            else 'red'  if tipo=='Fertilizantes'
                            else 'yellow' if tipo =='Granel Líquido'
                            else 'pink' if tipo == 'Celulose'
                            else 'purple' if tipo == 'Sucos Cítricos'
                            else 'ligthgreen' if tipo == 'Passageiros'
                            else 'dark blue' if tipo == 'Carga Geral/Veículos'
                            else 'grey' if tipo == 'Carga Geral/Base Offshore'
                            else 'white',
                    'color': 'black',
                    'weight': 0.1,
                },  
                           popup=popup).add_to(feature_groups[tipo])
            
#"ROADMAP": 

for fg in feature_groups.values():
    m.add_child(fg)
folium.LayerControl(position='topright', collapsed=False, autoZIndex=True).add_to(m)

st_folium(m, width=1000, height=600)
#st.dataframe(LocaisTerminais)