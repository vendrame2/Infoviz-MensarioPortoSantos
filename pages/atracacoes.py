import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import time
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

"""
Datasets
https://www.kaggle.com/datasets/mexwell/world-port-index
https://www.kaggle.com/datasets/rajkumarpandey02/world-wide-port-index-data
https://www.kaggle.com/datasets/sanjeetsinghnaik/ship-ports

REFs
Aula professora - https://www.youtube.com/watch?v=X5Ug5C3LfOo
https://www.youtube.com/playlist?list=PLTYhWEH3DGrQXAJc-BldYfnroDWzbfwtd

CODES
PLot lat Log in python - https://stackoverflow.com/questions/53233228/plot-latitude-longitude-from-csv-in-python-3-6
Geopandas - https://towardsdatascience.com/the-easiest-way-to-plot-data-from-pandas-on-a-world-map-1a62962a27f3
Map Flights - https://coderzcolumn.com/tutorials/data-science/how-to-create-connection-map-chart-in-python-jupyter-notebook-plotly-and-geopandas
https://tech.marksblogg.com/popular-airline-passenger-routes-2023.html
https://towardsdatascience.com/geopandas-101-plot-any-data-with-a-latitude-and-longitude-on-a-map-98e01944b972
https://towardsdatascience.com/using-python-to-create-a-world-map-from-a-list-of-country-names-cd7480d03b10
https://www.reddit.com/r/dataisbeautiful/comments/rkx7ww/opensource_airline_route_maps_from_1999_and_2018/?rdt=43412


Pendências: Localização de alguns portos
https://unece.org/trade/cefact/UNLOCODE-Download >> Base de download da POrt API
https://port-api.com/docs


***
**python cluster points with less than x meters
***
https://geoffboeing.com/2014/08/clustering-to-reduce-spatial-data-set-size/
https://stackoverflow.com/questions/53075481/how-do-i-cluster-a-list-of-geographic-points-by-distance
https://gis.stackexchange.com/questions/437344/python-geopandas-if-distance-between-each-point-and-its-neighbors-is-less-th
https://stackoverflow.com/questions/19375675/simple-way-of-fusing-a-few-close-points
https://kazumatsuda.medium.com/spatial-clustering-fa2ea5d035a3
https://kazumatsuda.medium.com/aggregating-information-of-two-overlaying-geodataframes-using-geopandas-with-code-example-dcee1df74e0e

https://sites.google.com/icmc.usp.br/apneto/teaching/mai5017-2024

"""


movimentacao = pd.DataFrame(pd.read_csv('./0_Stagging/combined_file.csv', encoding='utf8', sep=","))

movimentacao['Data'] = pd.to_datetime(movimentacao['Ano'].astype(str) + 
                                        movimentacao['Mes'].astype(str), format='%Y%m')
movimentacao['Data'] = movimentacao['Data'].dt.date
#st.dataframe(movimentacao)

#st.write(movimentacao["Carga"].unique())
#st.write(movimentacao["PerfilCarga"].unique())


movimentacao['Carga'].replace('PRODUTOS DA INDÚSTRIA QUÍMICA', 'PRODUTOS QUÍMICOS', inplace=True)
movimentacao['Terminal'].replace('  ', ' ', inplace=True)
movimentacao['TipoInstalacao'].replace('', 'PORTO ORGANIZADO', inplace=True)
movimentacao['TipoInstalacao'].replace(' ', 'PORTO ORGANIZADO', inplace=True)
#movimentacao['TipoInstalacao'].replace(None, 'PORTO ORGANIZADO', inplace=True)

#Agrupamento por Terminal
movimentacao['TerminalAjustado'] = movimentacao['Terminal']
movimentacao['TerminalAjustado'].replace('VOPAK (ILHA)', 'VOPAK', inplace=True)
movimentacao['TerminalAjustado'].replace('VOPAK (ALAMOA)', 'VOPAK', inplace=True)

movimentacao['TerminalAjustado'].replace('CITROSUCO (SER. PASSAGEM)','CITROSUCO', inplace=True)
movimentacao['TerminalAjustado'].replace('CUTRALE SABOO', 'CUTRALE', inplace=True)
movimentacao['TerminalAjustado'].replace('CUTRALE - TPO', 'CUTRALE',inplace=True)

movimentacao['TerminalAjustado'].replace('AGEO LESTE', 'AGEO', inplace=True)
movimentacao['TerminalAjustado'].replace('AGEO NORTE - COPAPE','AGEO',  inplace=True)

movimentacao['TerminalAjustado'].replace('GRANEL QUIMICA (ALAMOA)', 'GRANEL QUIMICA',inplace=True)
movimentacao['TerminalAjustado'].replace('GRANEL QUIMICA (ILHA)', 'GRANEL QUIMICA',  inplace=True)

movimentacao['TerminalAjustado'].replace('LIBRA 33', 'LIBRA',  inplace=True)
movimentacao['TerminalAjustado'].replace('LIBRA 35', 'LIBRA',  inplace=True)
movimentacao['TerminalAjustado'].replace('LIBRA 37', 'LIBRA',  inplace=True)

movimentacao['TerminalAjustado'].replace('RODRIMAR - ARM VIII', 'RODRIMAR',  inplace=True)

movimentacao['TerminalAjustado'].replace('SANTOS BRASIL - ', 'SANTOS BRASIL', inplace=True)
movimentacao['TerminalAjustado'].replace('SANTOS BRASIL (SSZ35.2 Saboó)', 'SANTOS BRASIL', inplace=True)

movimentacao['TerminalAjustado'].replace('USIMINAS - TPF', 'USIMINAS',  inplace=True)



#Incluindo Geolocalização dos pontos


# PLot no mapa de santos

terminaisSantos = pd.DataFrame(pd.read_csv('./0_Stagging/TerminaisSantos.csv', encoding='utf8', sep=";"))

terminaisSantos = terminaisSantos[terminaisSantos.Terminal != ""]

#portos.drop(columns={"Porto_ORI"}, axis=1,  inplace=True)
#limpa Virgulas da Latitude
terminaisSantos["Latitude"]=terminaisSantos["Latitude"].replace(",","" )
terminaisSantos["Longitude"]=terminaisSantos["Longitude"].replace(",","")

#transforma em números reais
terminaisSantos["Latitude"]=terminaisSantos["Latitude"].astype(float)
terminaisSantos["Longitude"]=terminaisSantos["Longitude"].astype(float)

movimentacaoGeo = pd.merge(movimentacao, terminaisSantos,on='Terminal', how='left' )
#ClientePedido = pd.merge(Clientes,pedidos[['Total','Pedidos']],on='Cliente', how='left')
#st.dataframe(movimentacaoGeo)
                           









col1, col2, col3 = st.columns(3)

with col1:
    st.header("Perfl da Carga")
    perfilCarga_list = list(movimentacao["PerfilCarga"].unique())[::-1]
    selected_perfilCarga = st.multiselect('Selecione o Tipo da Carga', perfilCarga_list,default="CARGA CONTEINERIZADA") 

with col2:
    st.header("Tipo de Instalação")
    tipoInst_list = list(movimentacao["TipoInstalacao"].unique())[::-1]
    selected_tipoInst = st.multiselect('Selecione o Tipo da Instalacao', tipoInst_list,default="PORTO ORGANIZADO") 

with col3:
    st.header("Agrupamento")
    selected_group = st.selectbox('Selecione o Tipo de Agrupamento', ["Terminal","Carga"])
    if selected_group == "Terminal": 
        selected_group = "TerminalAjustado" 
    else:
       selected_group = "Carga" 
       



movimentoQ = movimentacaoGeo[((movimentacaoGeo["PerfilCarga"].isin(selected_perfilCarga)) & 
                              (movimentacaoGeo["TipoInstalacao"].isin(selected_tipoInst)))].groupby(
                                                                                        [selected_group,"Data","Latitude","Longitude"]
                                                                                        ).agg({'Toneladas':sum}).sort_values(by=["Data",selected_group], ascending=True).reset_index()

#st.dataframe(movimentoQ)

fig = px.bar(movimentoQ, x="Data", y="Toneladas", color=selected_group)

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)



################### MAPA

fig2 = px.scatter_mapbox(movimentoQ,
                        animation_frame = 'Data', animation_group = selected_group, 
                        lat="Latitude", 
                        lon="Longitude", 
                        hover_name=selected_group, 
                        hover_data=[selected_group, "Toneladas"],
                        color_continuous_scale=px.colors.cyclical.IceFire,
                        size="Toneladas",
                        size_max=70, 
                        title = 'XXXXX em Terminais Portuários',
                        zoom=12, 
                        height=600,
                        width=1920)

fig2.update_layout(mapbox_style="open-street-map")
fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig2, use_container_width=True)
