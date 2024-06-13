import geopandas as gpd
import geoplot as glpt
import geoplot.crs as gcrs
import geojson
import pandas as pd

def convertbercosPDZDataFrame():
    
    arquivo = "./Data/raw/PDZ_bercos.geojson"
    geo = gpd.read_file(arquivo)
    with open(arquivo, 'r', encoding='utf-8') as file:
        geojson_data = geojson.load(file)

    df =  pd.json_normalize(dict(geojson_data)["features"])

    df.rename(columns={'type': 'Tipo', 
                            'geometry.type': 'TipoPoligono', 
                            'geometry.coordinates': 'Coordenadas', 
                            'properties.Id. Cais': 'Cais', 
                            'properties.Id. Berço': 'Berco', 
                            'properties.C. Const.': 'Descricao', 
                            'properties.Comp.': 'Comprimento', 
                            'properties.Profund.': 'Profundidade', 
                            'properties.Calado': 'Calado', 
                            'properties.Per.Carga': 'Carga', 
                            }, inplace=True)
    dfPoligono = df.loc[:,'Tipo':'Berco']
    dfBercosPDZ = df.loc[:,'Berco':]
    return dfPoligono, dfBercosPDZ