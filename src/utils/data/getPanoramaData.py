# Pega dados do site do Porto de Santos via Acesso
# Dados GeoRef
# WordPress: https://www.portodesantos.com.br/conheca-o-porto/panorama/?tipo=areas
# Site Visual: 

import pandas as pd
from urllib.request import urlopen 
import requests, json
from flatten_json import flatten

URL = "https://www.portodesantos.com.br/conheca-o-porto/panorama/?tipo=areas"

def carregaDadosTerminaisPanorama():
    
    # store the response of URL 
    response = urlopen(URL) 

    data_json = json.loads(response.read()) 

    return data_json # Check the JSON Response Content documentation below

def DictToDatasetPanorama():
    
    data_json = carregaDadosTerminaisPanorama()

    dfLocalTerminal = []
    for i, terminal in enumerate(data_json):
        
        new_row = [[terminal["nome"], terminal["poligonos"]]]
        dfLocalTerminal.append(new_row)


    return dfLocalTerminal    

def  coordToListTerminais(celulaPoligonos):
    
    from shapely.geometry import Polygon
    
    for j, poligono in enumerate(celulaPoligonos):
                    
        _coords = poligono["coordenadas"].splitlines()
        _coords = list(map(lambda x: x.strip(), _coords))
        
        
        lat_point_list = list(map(lambda x: x.split(',')[0], _coords))
        lon_point_list = list(map(lambda x: x.split(',')[1], _coords))
        
        polygon_geom = Polygon(zip(lat_point_list,lon_point_list))
    
    return polygon_geom           