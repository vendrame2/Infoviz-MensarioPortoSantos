import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import locale
import seaborn as sns
import matplotlib.pyplot as plt



st.set_page_config(
    page_title="Porto de Santos - Movimentação",
    page_icon="🏂",
    layout="wide"
    )

import menu as menu
menu.menu()
    

st.markdown(f"""
    <style>
    iframe {{
        width: inherit;
    }}
    </style>
    """
    , unsafe_allow_html=True)

#Sources do projeto
from src.utils.data import getMovimentacoesData as movimenta
from src.utils.data import getTerminaisData as terminais

movimentacao = movimenta.carregaMovimentacao()

terminaisSantos = terminais.carregaTerminais()
movimentacaoGeo = pd.merge(movimentacao, terminaisSantos,on='Terminal', how='left' )
movimentacaoGeo['Data'] = pd.to_datetime(movimentacaoGeo['Data'])

#st.write( movimentacao[movimentacao["Ano"]==2023 & movimentacao["Mes"]==1].all()["Toneladas"].sum())

st.header("1. Análise Geral do Volumes")

tabA, tabB = st.tabs(["Hipótese 1","Hipótese 2"])

with tabA:

    col1, col2 = st.columns([1,3])
    with col1:
        st.subheader("Análise Temporal da Movimentação de Cargas")
    with col2:            
        mark = """
                <div style="text-align: justify;font-face: tahoma;font-size:12pt;border: 0.5px dashed #666;border-radius:10px; background-color: #eee;box-sizing: border-box;
                padding: 10px;">
                    <b>Hipótese 1:</b> O crescimento do volume total de carga movimentado oscilou ao longo dos anos e tem tendência de crescimento.
                </div>
                """
        st.markdown(""+mark+"</p>", unsafe_allow_html=True)
        #st.divider()

    tab1, tab2, tab3 = st.tabs(["Evolução da Carga Movimentada","Variação da Carga Movimentada","Comparação PIB, Indústria, Serviços e Agro"])
    with tab1:


            # Agrupando os dados por Data
            grpMov = movimentacaoGeo.groupby(['Ano','Mes','Data']).agg(Toneladas=('Toneladas','sum')).reset_index()
            #st.dataframe(grpMov)
            grpMov['Média Móvel 12 Meses'] = grpMov['Toneladas'].rolling(window=12).mean()
            grpMov['Acumulado_12_Meses'] = grpMov['Toneladas'].rolling(window=12).sum()
            grpMov['Acumulado_12_Meses_Ano_Anterior'] = grpMov['Acumulado_12_Meses'].shift(12)
            grpMov['Toneladas YoY %'] = ((grpMov['Acumulado_12_Meses'] / grpMov['Acumulado_12_Meses_Ano_Anterior']) - 1) * 100
            #display(grpMov)
            st.caption(len(grpMov))
            # Gráfico de linha com a evolução do volume movimentado e a média móvel de 12 meses
            fig = px.line(grpMov, x='Data', y=['Toneladas','Média Móvel 12 Meses'])
            fig.update_layout(
                title='Evolução da Carga (Tons) Movimentadas Mensal e Anualmente',
                xaxis_tickfont_size=14,
                yaxis=dict(title='Toneladas', titlefont_size=16, tickfont_size=14),
                xaxis=dict(title='Ano', titlefont_size=16, tickfont_size=14),
                width=900,
                height=600)
            
            st.plotly_chart(fig, use_container_width=True)
            #st.image(fig)

    with tab2:
        #st.dataframe(grpMov)
        fig = px.bar(grpMov, x='Data', y='Toneladas YoY %', 
                title='Variação da Carga Movimentada vs Ano Anterior (YoY %)')
        fig.update_layout(
        xaxis_title='Ano',
        yaxis_title='Variação vs Ano Anterior (YoY %)',
        width=900,
        height=600)
        grpMov["Color"] = np.where(grpMov["Toneladas YoY %"]<0, 'red', 'green')
        fig.update_traces(marker_color=grpMov["Color"])
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
    
        # Carregando os dados de PIB
        dfPIB = pd.read_excel('./Data/raw/Tab_Compl_CNT_1T24.xls', sheet_name='Acum. em 4 trimestres', header=2)
        # Acertando os rótulos
        new_header = []
        for col1, col2 in zip(dfPIB.iloc[0], dfPIB.columns):
            if pd.isna(col1) or col1=='Total':
                new_header.append(col2)
            else:
                new_header.append(col1)
        dfPIB.columns = new_header
        dfPIB = dfPIB.rename(columns={'Unnamed: 6': 'INDÚSTRIA', 'Unnamed: 14': 'SERVIÇOS'})
        dfPIB.drop(0, axis=0, inplace=True)

        # Converte o trimestre em algarismo romano em data
        de_para = {'.I': '03', '.II': '06', '.III': '09', '.IV': '12'}
        dfPIB['Data'] = [f"{row['Período'][:4]}-{de_para[row['Período'][4:]]}-01" 
                                if row['Período'][4:] in de_para.keys() 
                                else row['Período']                        
                                for _, row in dfPIB.iterrows()]
        dfPIB['Data'] = pd.to_datetime(dfPIB['Data'])



        # Juntando as 2 tabelas
        grpMovTri = pd.merge(grpMov, dfPIB[['Data', 'PIB', 'AGROPECUÁRIA', 'INDÚSTRIA', 'SERVIÇOS']], 
                            how='inner', on='Data')
        grpMovTri = grpMovTri.astype({'AGROPECUÁRIA': float, 'INDÚSTRIA': float, 'SERVIÇOS': float})
        #grpMovTri

        with st.expander("Visão Ano Fechado"):
            # Visão do ano fechado
            fig = px.line(grpMovTri, x='Data', y=['Toneladas YoY %', 'PIB', 'AGROPECUÁRIA', 'INDÚSTRIA', 'SERVIÇOS'], 
                        title='Variação da Carga Movimentada vs Ano Anterior (YoY %) e Indicadores Macroeconômicos')
            fig.update_layout(
                xaxis_title='Ano',
                yaxis_title='Variação vs Ano Anterior (YoY %)',
                width=900,
                height=600)
            st.plotly_chart(fig, use_container_width=True)

        with st.expander("Matriz de Correlação"):

            # Calcular a matriz de correlação
            matriz_corr = grpMovTri[['Toneladas YoY %', 'PIB', 'AGROPECUÁRIA', 'INDÚSTRIA', 'SERVIÇOS']].corr()

            # Criar o heatmap da matriz de correlação
            fig, ax = plt.subplots()
            sns.heatmap(matriz_corr, annot=True, cmap='coolwarm', ax=ax)

            # Exibir o gráfico no Streamlit
            st.pyplot(fig)

        with st.expander("Matriz de Scatterplots"):
            fig = px.scatter_matrix(grpMovTri, dimensions=grpMovTri[['Toneladas YoY %', 'PIB', 'AGROPECUÁRIA', 'INDÚSTRIA', 'SERVIÇOS']],
                            color=grpMovTri['Data'].dt.year,# hover_name='Toneladas',
                            color_continuous_scale="Inferno",
                            title="Matriz de Scatterplots")
            fig.update_traces(diagonal_visible=False)  # Ocultar os gráficos na diagonal, se desejado
            fig.update_layout(
                coloraxis_colorbar=dict(title="Ano"),
                height=900, width=900)   # Ajustar o tamanho do layout
            st.plotly_chart(fig, use_container_width=True)

with tabB:
    col1, col2 = st.columns([1,3])
    with col1:
        st.subheader("Análise de Sazonalidade")
    with col2:            
        mark = """
                <div style="text-align: justify;font-face: tahoma;font-size:12pt;border: 0.5px dashed #666;border-radius:10px; background-color: #eee;box-sizing: border-box;
                padding: 10px;">
                    <b>Hipótese 2:</b> Os volumes variam conforme os meses e pode ter mudado ao longo do tempo.
                </div>
                """
        st.markdown(""+mark+"</p>", unsafe_allow_html=True)
        #st.divider()
    
    st.subheader("Gráfico de área por mês comparando os últimos anos, incluindo o período impactado pela pandemia")

    # Filtrando os dados dos últimos anos e agrupando por ano, mês e perfil de carga
    grpMov = movimentacaoGeo.query('(Ano>=2018 & Ano<=2022)').groupby(['Ano', 'Mes', 'PerfilCarga']).agg(
        Toneladas=('Toneladas','sum'), 
        TEUs=('TEUs','sum'), Unidades=('Unidades','sum')
        ).reset_index()

    # Plotando o gráfico de áreas usando Plotly Express
    fig = px.area(grpMov, x='Mes', y='Toneladas', color='PerfilCarga', facet_col='Ano',
                labels={'Mes': 'Mês', 'Toneladas': 'Toneladas', 'PerfilCarga': 'Perfil Carga'},
                title='Volume de Carga Movimentada por Mês e Tipo de Carga')

    fig.update_layout(
        xaxis_tickfont_size=14,
        yaxis=dict(title='Toneladas', titlefont_size=16, tickfont_size=14),
        width=1200,
        height=500)

    # Atualizando os rótulos do eixo x com os nomes dos meses
    fig.update_xaxes(tickvals=np.arange(1, 13), ticktext=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
                                                        'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])

    st.plotly_chart(fig, use_container_width=True)