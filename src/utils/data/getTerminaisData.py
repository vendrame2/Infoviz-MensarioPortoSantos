import pandas as pd
import numpy as np



def carregaTerminais():

    terminaisSantos = pd.DataFrame(pd.read_csv('./Data/raw/TerminaisSantos.csv', encoding='utf8', sep=";"))

    terminaisSantos = terminaisSantos[terminaisSantos.Terminal != ""]

    #portos.drop(columns={"Porto_ORI"}, axis=1,  inplace=True)
    #limpa Virgulas da Latitude
    terminaisSantos["Latitude"]=terminaisSantos["Latitude"].replace(",","" )
    terminaisSantos["Longitude"]=terminaisSantos["Longitude"].replace(",","")

    #transforma em números reais
    terminaisSantos["Latitude"]=terminaisSantos["Latitude"].astype(float)
    terminaisSantos["Longitude"]=terminaisSantos["Longitude"].astype(float)

    return terminaisSantos