import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import time



st.set_page_config(
    page_title="Port of Santos Container  Visualization",
    page_icon="🏂",
    layout="wide"
    )

import menu as menu
menu.menu()

    
"""

portos = pd.DataFrame(pd.read_csv('./0_Stagging/00_Portos.csv', encoding='utf8', sep=";"))
portos = portos[portos.Latitude != "#CALC!"]
portos = portos[portos.Longitude != "#CALC!"]

portos.drop(columns={"Porto_ORI"}, axis=1,  inplace=True)

#impa Virgulas da Latitude
portos["Latitude"]=portos["Latitude"].str.replace(",","" )
portos["Longitude"]=portos["Longitude"].str.replace(",","")

#transforma em números reais
portos["Latitude"]=portos["Latitude"].astype(float)
portos["Longitude"]=portos["Longitude"].astype(float)


portos = portos.sort_values(['Trigrama'])
#st.dataframe(portos)


portsExcluir = ["TTLAB","CABAY","DOHAI","VEPSU","USMOR","DOSDQ","AROYO","LCCDS","CANEP","CRCAL","USADK","NARSAK","VICRO","CAMON","BRARE","CAGAE","CASJB","CRCAL","AWAUA","AROES","ARIBO","CRCAL","CANEP",
                "ARIB0","VEPSU","AROES","CASJB","SRSMA","CALCV",
                "VEJSE","ARCVI","VELCV","USPOT","VEPCA","PEPIO","BRIOA","COTLU","BRSAL","GFSLM","BRIGI","ARINW","BRARA","ARLIM","CABAS","NAZZZ","SO003","EGDAM","EGAIS","NALUD","MAZZZ",
                "REPDG","NGBRT","MAEUN","CGNKO","MATNG","ZAPRY","CGBTB","LRROX","STTMS","BRAMW","BRSLZ","BROUT","CABEC","BRBAR","BR205","USCHA","YESAL","CNDJK","TRERE","MYPRA","CNDAA",
                "INDHA","KRSEL","KRINC","KRYOS", "AEDAS","TRISK","SAYNB","TWKHH","KRTGA","KRPUS","INKAT","ROCND","NLIJM","RUPRI","DELAG","NOKAR","RUTAM","ITRAM","RUKRR","DEMAM","BEZEL",
                "NOFRK","ITSPA","ESBIO","UAMPW","UAYUZ","SEROR","SEARN","RULED","AD888","DESTA","FISVL","NOKMY","UAICK","GBPRU","RUPWE","RUIKS","RU888","RULAZ","RULES","RUSOG","RUNEV",
                "RUZAR","CNDEF","TRLMA","BHSIT","TRIST","IRASA","CLARI","BR252","GLJNS"]
    
#st.write(portos["Trigrama"].size)

portos = portos[ ~ portos["Trigrama"].isin(portsExcluir)]

#st.write(portos["Trigrama"].size)


continent_list = list(portos["continent"].unique())[::-1]
selected_continent = st.selectbox('Selecione o Continente', continent_list, index=len(continent_list)-1)


with st.container():
    st.write("Portos Encontrados")

    
    colAfrica, colAmerica, colAsia, colOceania, colEurope = st.columns(5)

    with colAfrica:
        st.metric(label="África", value=portos[portos.continent == "Africa"]["CODE"].size)


    with colAmerica:
        st.metric(label="Américas", value=portos[portos.continent == "Americas"]["CODE"].size)


    with colAsia:
        st.metric(label="Ásia", value=portos[portos.continent == "Asia"]["CODE"].size)

    
    with colOceania:
        st.metric(label="Oceania", value=portos[portos.continent == "Oceania"]["CODE"].size)

    with colEurope:
        st.metric(label="Europa", value=portos[portos.continent == "Europe"]["CODE"].size)




fig2 = px.scatter_mapbox(portos[portos.continent == selected_continent], 
                        lat="Latitude", 
                        lon="Longitude", 
                        hover_name="Porto", 
                        hover_data=["Pais","Trigrama","Porto","Latitude","Longitude"],
                        #color="Listed",
                        #color_continuous_scale=color_scale,
                        #size="Listed",
                        zoom=2, 
                        height=500,
                        width=1920)

fig2.update_layout(mapbox_style="open-street-map")
fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig2, use_container_width=True)
"""
    