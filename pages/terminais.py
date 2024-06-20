import folium.map
import streamlit as st

from streamlit_folium import st_folium

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
    
m = folium.Map([-23.95606873631538, -46.30942691864801], zoom_start=12, width=1000, height=500)
minimap = plugins.MiniMap()
m.add_child(minimap)





#folium.TileLayer(
#                tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
#                attr = 'Esri',
#                name = 'Esri Satellite', 
#                overlay = True,
#                control = True,
#                subdomains=["mt0", "mt1", "mt2", "mt3"]).add_to(m)
#folium.TileLayer("https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}", 
#                 attr="google", 
#                 name="Google Maps", 
#                 overlay=True, 
#                 control=True, 
#                 subdomains=["mt0", "mt1", "mt2", "mt3"]).add_to(m)


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




for i, terminal in enumerate(LocaisTerminais):
            
            html = "<div style='font-face:tahoma;font-size:10pt'><b> "+ str(terminal[0][0]) +"</b></div><br>"
            html = html + "<div style='font-face:tahoma;font-size:9pt'><b>Coordenadas: </b> s" + "<br>"
            html = html + "<b>R$: </b>" + "xx" + "</div>"

            iframe = folium.IFrame(html)
            popup = folium.Popup(iframe,
                                min_width=150,
                                max_width=150)
                

            style =  {'fillColor': 'blue', #cor de preenchimento
                            'color': 'red',#cor da linha de contorno
                            'weight': 0.1, #espessura da linha
                        }
            folium.GeoJson(carregaDadosTerminaisPanorama.coordToListTerminais(terminal[0][1]), name=terminal[0][0], tooltip=terminal[0][0], style_function=lambda x:style, popup=popup).add_to(m)
#"ROADMAP": 

folium.LayerControl(position='topright', collapsed=False, autoZIndex=True).add_to(m)

st_data = st_folium(m, width=1000, height=500)