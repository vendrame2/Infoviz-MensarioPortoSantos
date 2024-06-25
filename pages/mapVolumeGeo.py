import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

import locale
import pydeck as pdk
import streamlit.components.v1 as components

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#Sources do projeto
from src.utils.data import getMovimentacoesData as movimenta
from src.utils.data import getTerminaisData as terminais


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
movimentacaoGeo = movimentacaoGeo.drop(columns=movimentacaoGeo.columns[[ 
                                                                        movimentacaoGeo.columns.get_loc('Tamanho'),
                                                                        movimentacaoGeo.columns.get_loc('TerminalUni'),
                                                                        movimentacaoGeo.columns.get_loc('Local'),
                                                                        movimentacaoGeo.columns.get_loc('Tipo')
                                                                        ]])


st.markdown(f"""
    <style>
    iframe {{
        width: inherit;
    }}
    </style>
    """
    , unsafe_allow_html=True)

col1, col2 = st.columns([1, 6])
with col1:
    st.subheader("Ano")
    Ano = st.selectbox('Selecione o Ano', movimentacaoGeo["Ano"].unique())
    st.subheader("Perfil Carga")
    TipoCarga = st.multiselect('Selecione o Ano', movimentacaoGeo["PerfilCarga"].unique())


with col2:

    

    if Ano:
        
        movimentacaoGeo = movimentacaoGeo[((movimentacaoGeo["PerfilCarga"].isin(TipoCarga)) & 
                                            (movimentacaoGeo["Ano"] == Ano))].groupby(
                                            ["Ano", "TerminalAjustado", "Latitude", "Longitude", "PerfilCarga"]
                                            ).agg({'Toneladas':"sum"}).sort_values(by=["TerminalAjustado"], ascending=True).reset_index()

    # HTML e JavaScript para o Mapbox e Deck.gl
    legend_html = '''
        <div style="position: absolute; top: 30px; right: 50px; z-index: 1000; background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 1px solid #ccc; border-radius: 5px; font-family: Arial, sans-serif; font-size: small;">
            <div style="margin-bottom: 5px;">
                <svg width="20" height="20">
                    <circle cx="10" cy="10" r="8" stroke="white" stroke-width="2" fill="red" />
                </svg>
                <span style="margin-left: 5px; font-weight: bold;">Carga Geral</span>
            </div>
            <div style="margin-bottom: 5px;">
                <svg width="20" height="20">
                    <circle cx="10" cy="10" r="8" stroke="white" stroke-width="2" fill="green" />
                </svg>
                <span style="margin-left: 5px; font-weight: bold;">Granel Sólido</span>
            </div>
            <div style="margin-bottom: 5px;">
                <svg width="20" height="20">
                    <circle cx="10" cy="10" r="8" stroke="white" stroke-width="2" fill="blue" />
                </svg>
                <span style="margin-left: 5px; font-weight: bold;">Granel Líquido</span>
            </div>
            <div style="margin-bottom: 5px;">
                <svg width="20" height="20">
                    <circle cx="10" cy="10" r="8" stroke="white" stroke-width="2" fill="yellow" />
                </svg>
                <span style="margin-left: 5px; font-weight: bold;">Conteiners</span>
            </div>
        </div>
        '''
    st.markdown(legend_html, unsafe_allow_html=True)
    
    
    
    movimentacaoGeo["MTons"] = (movimentacaoGeo["Toneladas"]/1000000).round(2)
    movimentacaoGeo = movimentacaoGeo.pivot_table(
        index=['TerminalAjustado', 'Ano', 'Latitude', 'Longitude'],
        columns='PerfilCarga',
        values='MTons',
        aggfunc='sum'
    ).reset_index()
    movimentacaoGeo = movimentacaoGeo.fillna(0)

    #st.dataframe(movimentacaoGeo)
    #print("Carga Geral" in TipoCarga)
    if 'CARGA GERAL' not in movimentacaoGeo.columns: movimentacaoGeo['CARGA GERAL'] = 0
    if 'GRANEL SOLIDO' not in movimentacaoGeo.columns: movimentacaoGeo['GRANEL SOLIDO'] = 0
    if 'GRANEL LIQUIDO' not in movimentacaoGeo.columns: movimentacaoGeo['GRANEL LIQUIDO'] = 0
    if 'CARGA CONTEINERIZADA' not in movimentacaoGeo.columns: movimentacaoGeo['CARGA CONTEINERIZADA'] = 0


        # Calculando o total de toneladas
    #movimentacaoGeo["MTons"] = (movimentacaoGeo[["CARGA GERAL", "GRANEL SOLIDO", "GRANEL LIQUIDO", "CARGA CONTEINERIZADA"]].sum(axis=1) / 1000000).round(2)


    # Dados da autoridade portuária
    authority_location = {
        'name': 'Autoridade Portuária',
        'lat': -23.95606873631538, 
        'lon': -46.30942691864801,
        'logo': 'https://www.portodesantos.com.br/en/wp-content/uploads/2019/11/logo_santos_port_authority-1024x559.png'  # Substitua pelo URL do logotipo da autoridade portuária
    }

    # Configuração dos dados para Pydeck
    data = []
    for i, row in movimentacaoGeo.iterrows():
        data.append({
            'name': row['TerminalAjustado'],
            'lat': row['Latitude'],
            'lon': row['Longitude'],
            'carga1': row['CARGA GERAL'],
            'carga2': row['GRANEL SOLIDO'],
            'carga3': row['GRANEL LIQUIDO'],
            'carga4': row['CARGA CONTEINERIZADA'],
            'elevation': 27
        })

    # Lista de cores para cada seção da barra empilhada
    colors = {
        'carga1': [255, 0, 0],   # Vermelho para CARGA GERAL
        'carga2': [0, 255, 0],   # Verde para GRANEL SOLIDO
        'carga3': [0, 0, 255],   # Azul para GRANEL LIQUIDO
        'carga4': [255, 255, 0]  # Amarelo para CARGA CONTEINERIZADA
    }

    # Criando a visualização Pydeck com barras empilhadas
    view_state = pdk.ViewState(
        latitude=-23.96,
        longitude=-46.32,
        zoom=12,
        pitch=50
    )

    layers = []
    for section in ['carga1', 'carga2', 'carga3', 'carga4']:
        layers.append(
            pdk.Layer(
                'ColumnLayer',
                data=data,
                get_position='[lon, lat]',
                get_fill_color=f'[{colors[section][0]}, {colors[section][1]}, {colors[section][2]}]',  # Cor da seção específica
                get_elevation=f'{section} * 20',  # Altura da seção específica
                elevation_scale=10,
                radius=50,
                pickable=True,
                extruded=True,
                auto_highlight=True
            )
        )
     # Tooltip para a autoridade portuária com logotipo
    authority_tooltip = {
        "html": "<img src='{logo}' style='width:50px;height:50px;'/><br /><b>{name}</b>",
        "style": {
            "backgroundColor": "steelblue",
            
        }
    }
    #layers.append(
    #    pdk.Layer(
    #        'ScatterplotLayer',
    #        data=[authority_location],
    #        get_position='[lon, lat]',
    #        get_fill_color='[255, 255, 255]',  # Cor branca para o ponto
    #        get_radius=100,
    #        pickable=True,
    #        tooltip=True,
    #        getTooltip= authority_tooltip
    #    )
    #)
    tooltip = {
                "html": "<b>{name}</b><br />Carga Geral: {carga1} M Tons. <br />Granel Sólido: {carga2} M Tons. <br />Granel Líquido: {carga3} M Tons. <br />Carga Conteinerizada: {carga4} M Tons. ",
                "style": {
                        "backgroundColor": "#666",
                        "color": "#CCC"
                    }
                }
   
    # Renderizando o mapa com Pydeck e Streamlit
    st.pydeck_chart(pdk.Deck(
        height=800,
        map_style='mapbox://styles/mapbox/satellite-streets-v11',
        layers=layers,
        initial_view_state=view_state,
        tooltip=tooltip
    ))
    



    


   