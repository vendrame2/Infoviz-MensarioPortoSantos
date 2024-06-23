import geopandas as gpd
import geoplot as glpt
import geoplot.crs as gcrs
import geojson
import pandas as pd

def carregaBercosPDZDataFrame():
    
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
    dfBercosPDZ = df.loc[:,'Cais':]
                         


    return dfPoligono, dfBercosPDZ

def carregaBercosPDZDataFramePuro():
    
    arquivo = "./Data/raw/PDZ_bercos.geojson"
    geo = gpd.read_file(arquivo)
    with open(arquivo, 'r', encoding='utf-8') as file:
        geojson_data = geojson.load(file)

    return  dict(geojson_data)

def converte_GeoJSON_ORIGINAL_SHP_File():
    
    import geopandas as gpd

    gdf = gpd.read_file('./Data/raw/PDZ_bercos.geojson')
    gdf.to_file('./Data/raw/file.shp')

def converte_SHP_File_to_GeoJSON_Lat_Long():

    ##########
    #          Converte arquivo de shapefile para geoSon com latitude e longitude.
    #########
    
    json_file = "./Data/raw/porto.geojson"

    # Read in data
    gdf = gpd.read_file('./Data/raw/file.shp')
    # Reproject to Lat/Long: http://epsg.io/4326
    gdf_4326 = gdf.to_crs(epsg='4326')
    # Write to file
    gdf_4326.to_file(json_file, driver="GeoJSON") 

def carregaDeParaBercosMovimentacaoPDZ():
    return pd.DataFrame(pd.read_csv('./Data/deParaBercoMovimentaBercoPDZ.csv', encoding='utf8', sep=";"))
