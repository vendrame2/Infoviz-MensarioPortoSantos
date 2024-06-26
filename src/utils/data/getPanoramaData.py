# Pega dados do site do Porto de Santos via Acesso
# Dados GeoRef
# WordPress: https://www.portodesantos.com.br/conheca-o-porto/panorama/?tipo=areas
# Site Visual: 

import pandas as pd
from urllib.request import urlopen 
import requests, json
from flatten_json import flatten

URL = "https://www.portodesantos.com.br/conheca-o-porto/panorama/?tipo=areas"
URLCores = "https://www.portodesantos.com.br/conheca-o-porto/panorama/?tipo=cores"

def carregaDadosTerminaisPanorama():
    
    # store the response of URL 
    response = urlopen(URL) 

    data_json = json.loads(response.read()) 

    return data_json # Check the JSON Response Content documentation below

def carregaCoresTipoTerminaisPanorama():
    
    # store the response of URL 

    response = urlopen(URLCores) 
    response = json.loads(response.read())
    #print(response)
    dfcorTerminal = pd.DataFrame(columns=("TipoTerminal","Cor"))
    for index, (key, value) in enumerate(response.items()):
        
        new_row = pd.Series({
                    "TipoTerminal": key,
                    "Cor": value
                    })
        dfcorTerminal = append_row(dfcorTerminal, new_row)

    
    return dfcorTerminal

    return df # Check the JSON Response Content documentation below


def append_row(df, row):
    return pd.concat([
                df, 
                pd.DataFrame([row], columns=row.index)]
           ).reset_index(drop=True)

def DictToDatasetPanorama():
    
    dfCor = carregaCoresTipoTerminaisPanorama()

    data_json = carregaDadosTerminaisPanorama()

    dfLocalTerminal = pd.DataFrame(columns=("Terminal","Carga","Notas","Tamanho"))
    for i, terminal in enumerate(data_json):
        
        new_row = pd.Series({
                    "Terminal": terminal["nome"],
                    "Carga": terminal["carga"],
                    "Notas": terminal["notas"],
                    "Tamanho": terminal["tamanho"],
                    "Poligonos": terminal["poligonos"]
                    })
        dfLocalTerminal = append_row(dfLocalTerminal, new_row)
    
    dfLocalTerminal = dfLocalTerminal.merge(dfCor, left_on='Carga',right_on="TipoTerminal", how='left')

    #print(dfLocalTerminal["Terminal"].sort_values())
    #print("")

    return dfLocalTerminal

def  coordToListTerminais(celulaPoligonos):

    
    from shapely.geometry import Polygon
    
    for j, poligono in enumerate(celulaPoligonos):
                    
        _coords = poligono["coordenadas"].splitlines()
        _coords = list(map(lambda x: x.strip(), _coords))
        
        #print(_coords)
        
        lat_point_list = list(map(lambda x: x.split(',')[0], _coords))
        lon_point_list = list(map(lambda x: x.split(',')[1], _coords))
        
        polygon_geom = Polygon(zip(lat_point_list,lon_point_list))
    
    return polygon_geom          


def carregaDeParaTerminaisPanoramaMovimentacao():
    return pd.DataFrame(pd.read_csv('./Data/deParaPanoramaMovimentacao.csv', encoding='utf8', sep=";"))
