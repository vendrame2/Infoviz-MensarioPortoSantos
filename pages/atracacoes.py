import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import time
import locale


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#Sources do projeto
from src.utils.data import getMovimentacoesData as movimenta
from src.utils.data import getTerminaisData as terminais
from src.utils.data import getBercosData as bercos
from src.utils.data import getPanoramaData as carregaDadosTerminaisPanorama

st.set_page_config(
    page_title="Port of Santos Container  Visualization",
    page_icon="🏂",
    layout="wide"
    )

import menu as menu
menu.menu()
    
#Movimentação
movimentacao = movimenta.carregaMovimentacao()



terminaisSantos = terminais.carregaTerminais()

movimentacaoGeo = pd.merge(movimentacao, terminaisSantos,on='Terminal', how='left' )
#def colunasMovimentaGeo():
    #   Colunas
    #   Ano
    #   Mes
    #   Berco
    #   TipoInstalacao
    #   Terminal           
    #   PerfilCarga  
    #   TipoOperacao    
    #   Navegacao      
    #   SentidoCarga  ...    
    #   Unidades        
    #   Data
    #   TerminalAjustado   
    #   Latitude  
    #   Longitude    
    #   Local         
    #   Tipo  
    #   Tamanho 
    #   TerminalUni
   #print(movimentacaoGeo)


deParaBercos = bercos.carregaDeParaBercosMovimentacaoPDZ()
#st.dataframe(deParaBercos)

#Identificação dos berços
dfPoligono, dfBercosPDZ = bercos.carregaBercosPDZDataFrame()
#def colunasdfBercosPDZ():
    #Carrega Berços
    #st.write(dfBercosPDZ["Berco"].unique())
    #   Colunas
    #       Cais (Região)*
    #       Berco
    #       Descricao
    #       Comprimento*
    #       Profundidade* 
    #       Calado*
    #       Carga (Tipo)*
    #print(dfBercosPDZ)

deParaBercosDadosPDZ = pd.merge(deParaBercos, dfBercosPDZ,left_on="BercoPDZ", right_on="Berco", how='outer' )
st.dataframe(deParaBercosDadosPDZ)
     

#Identificação dos terminais (Página do Panorama do Porto de Santos)
LocaisTerminais = carregaDadosTerminaisPanorama.DictToDatasetPanorama()
#LocaisTerminais = pd.json_normalize(LocaisTerminais[0][0])
st.dataframe(LocaisTerminais)

col1, col2, col3, col4 = st.columns(4)

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
with col4:
    qtd = st.slider("Quantidade de TOPs", 3, 6, 1)
 


movimentacaoGeo['DataN'] = pd.to_datetime(movimentacaoGeo['Data'], format='%d%b%Y.%f')

movimentacaoGeo["mesAno"] = pd.to_datetime(movimentacaoGeo['Data'], format='%b/%Y.%f')


movimentoQ = movimentacaoGeo[((movimentacaoGeo["PerfilCarga"].isin(selected_perfilCarga)) & 
                            (movimentacaoGeo["TipoInstalacao"].isin(selected_tipoInst)))].groupby(
                                                                                        [selected_group,'mesAno',"Latitude","Longitude"]
                                                                                        ).agg({'Toneladas':"sum"}).sort_values(by=["mesAno",selected_group], ascending=True).reset_index()
print(movimentoQ.dtypes)

#st.dataframe(movimentoQ)

fig = px.bar(movimentoQ, x="mesAno", y="Toneladas", color=selected_group)

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
                        animation_frame = 'mesAno', animation_group = selected_group, 
                        lat="Latitude", 
                        lon="Longitude", 
                        hover_name=selected_group, 
                        hover_data=[selected_group, "Toneladas"],
                        color_continuous_scale=px.colors.cyclical.Edge,
                        size="Toneladas",
                        size_max=70, 
                        title = 'XXXXX em Terminais Portuários',
                        zoom=12, 
                        height=600,
                        width=1920)

fig2.update_layout(mapbox_style="open-street-map")
fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig2, use_container_width=True)



_top = movimentoQ.nlargest(qtd, 'Toneladas')
fig_bar = px.bar(_top,
                 x='Toneladas',
                 y='TerminalAjustado',
                 orientation='h',
                 color='Toneladas',
                 color_continuous_scale="YlOrRd",
                 title="TOP {qd} {selected_group}",
                 animation_frame = 'mesAno', 
                 animation_group = selected_group, 
                 )
fig_bar.update_layout(yaxis={'categoryorder': 'total ascending'})
st.plotly_chart(fig_bar, use_container_width=True)





