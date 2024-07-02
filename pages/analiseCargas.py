import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import locale




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
#terminaisSantos = terminais.carregaTerminais()
#movimentacaoGeo = pd.merge(movimentacao, terminaisSantos,on='Terminal', how='left' )
movimentacaoGeo = movimentacao
movimentacaoGeo['Data'] = pd.to_datetime(movimentacaoGeo['Data'])

st.header("2. Análise de Cargas")


tabA, tabB = st.tabs(["Hipótese 3","Hipótese 4"])
with tabA:
    col1, col2 = st.columns([1,3])
    with col1:
        st.subheader("Evolução do Perfil de Carga")
    with col2:            
        mark = """
                <div style="text-align: justify;font-face: tahoma;font-size:12pt;border: 0.5px dashed #666;border-radius:10px; background-color: #eee;box-sizing: border-box;
                padding: 10px;">
                    <b>Hipótese 3: Certos tipos de carga estão crescendo em participação no volume de carga movimentada</b> .
                </div>
                """
        st.markdown(""+mark+"</p>", unsafe_allow_html=True)

    #st.subheader("Visualização: Gráfico de barras empilhadas com a evolução dos volumes movimentados em valor absoluto de toneladas e em %.")

    # Agrupando por PerfilCarga
    grpMov = movimentacaoGeo.assign(
        result1=np.where(movimentacaoGeo['PerfilCarga']=='GRANEL SOLIDO', movimentacaoGeo['Toneladas'], 0),
        result2=np.where(movimentacaoGeo['PerfilCarga']=='CARGA CONTEINERIZADA', movimentacaoGeo['Toneladas'], 0),
        result3=np.where(movimentacaoGeo['PerfilCarga']=='GRANEL LIQUIDO', movimentacaoGeo['Toneladas'], 0),
        result4=np.where(movimentacaoGeo['PerfilCarga']=='CARGA GERAL', movimentacaoGeo['Toneladas'], 0),
    ).groupby('Ano').agg(
        Toneladas=('Toneladas','sum'),
        Toneladas_Granel_Sólido=('result1','sum'),
        Toneladas_Carga_Conteinerizada=('result2','sum'),
        Toneladas_Granel_Líquido=('result3','sum'),
        Toneladas_Carga_Geral=('result4','sum')
        ).reset_index()
    # Adicionando colunas em %
    grpMov['Toneladas_Granel_Sólido_%'] = grpMov['Toneladas_Granel_Sólido'] / grpMov['Toneladas']
    grpMov['Toneladas_Carga_Conteinerizada_%'] = grpMov['Toneladas_Carga_Conteinerizada'] / grpMov['Toneladas']
    grpMov['Toneladas_Granel_Líquido_%'] = grpMov['Toneladas_Granel_Líquido'] / grpMov['Toneladas']
    grpMov['Toneladas_Carga_Geral_%'] = grpMov['Toneladas_Carga_Geral'] / grpMov['Toneladas']
    grpMov.head()

    tab1, tab2 = st.tabs(["Evolução da Carga Movimentada por Perfil de Carga","Evolução da Carga Movimentada por Perfil de Carga em %"])

    with tab1:
        # Gráfico de barras empilhadas em valor absoluto
        fig = px.bar(grpMov, x='Ano', 
                    y=['Toneladas_Granel_Sólido',
                        'Toneladas_Carga_Conteinerizada', 
                        'Toneladas_Granel_Líquido',
                        'Toneladas_Granel_Líquido',
                        'Toneladas_Carga_Geral'])
        fig.update_layout(
            title='Evolução da Carga Movimentada por Perfil de Carga',
            xaxis_tickfont_size=14,
            yaxis=dict(title='Toneladas', titlefont_size=16, tickfont_size=14),
            xaxis=dict(title='Ano', titlefont_size=16, tickfont_size=14),
            width=900,
            height=500)
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        # Gráfico de barras empilhadas em %
        fig = px.bar(grpMov, x='Ano', 
                    y=['Toneladas_Granel_Sólido_%',
                        'Toneladas_Carga_Conteinerizada_%', 
                        'Toneladas_Granel_Líquido_%',
                        'Toneladas_Granel_Líquido_%',
                        'Toneladas_Carga_Geral_%'])
        fig.update_layout(
            title='Evolução da Carga Movimentada por Perfil de Carga em %',
            xaxis_tickfont_size=14,
            yaxis=dict(title='Toneladas', titlefont_size=16, tickfont_size=14),
            xaxis=dict(title='Ano', titlefont_size=16, tickfont_size=14),
            width=900,
            height=500)
        st.plotly_chart(fig, use_container_width=True)

with tabB:
    col1, col2 = st.columns([1,3])
    with col1:
        st.subheader("Evolução do Perfil de Carga")
    with col2:            
        mark = """
                <div style="text-align: justify;font-face: tahoma;font-size:12pt;border: 0.5px dashed #666;border-radius:10px; background-color: #eee;box-sizing: border-box;
                padding: 10px;">
                    <b>Hipótese 4:</b> Fluxo de cargas conforme tipo de instalação, sentido da carga, navegação, perfil e carga.
                </div>
                """
        st.markdown(""+mark+"</p>", unsafe_allow_html=True)
    
    # Visualização: Coordenadas Paralelas com o fluxo conforme as variáveis.

    grpMov = movimentacaoGeo.query('Ano==2022').groupby(['TipoInstalacao', 'PerfilCarga', 'TipoOperacao', 
    'Navegacao', 'SentidoCarga', 'Carga']).agg(
    Qtd=('Data','count'), Toneladas=('Toneladas','sum'), 
    TEUs=('TEUs','sum'), Unidades=('Unidades','sum')
    ).reset_index().sort_values(by=['TipoInstalacao', 'PerfilCarga', 'TipoOperacao', 
    'Navegacao', 'SentidoCarga', 'Carga'])
    #grpMov

    # Filtrando os dados de 2022 e agrupando os dados pelas variáveis categóricas
    grpMov = movimentacaoGeo.query('Ano==2005').groupby(['TipoInstalacao', 'PerfilCarga', 'TipoOperacao', 
        'Navegacao', 'SentidoCarga', 'Carga']).agg(
        Qtd=('Data','count'), Toneladas=('Toneladas','sum'), 
        TEUs=('TEUs','sum'), Unidades=('Unidades','sum')
        ).reset_index().sort_values(by=['TipoInstalacao', 'PerfilCarga', 'TipoOperacao', 
        'Navegacao', 'SentidoCarga', 'Carga'])
    #grpMov

    # Para resolver um problema de versão do pandas e plotly
    pd.DataFrame.iteritems = pd.DataFrame.items

    tab1, tab2, tab3, tab4 = st.tabs(["Fluxo Carga 2005","Fluxo Carga 2022","Fluxo Carga 2022 V2", "Volume Movimentado por Carga vs Terminal 2022"])
    with tab1:
        

        # Gráfico de coordenadas paralelas
        fig = px.parallel_categories(grpMov, 
            dimensions=['TipoInstalacao', 'Navegacao', 'SentidoCarga', 'PerfilCarga', 'Carga'],
            labels={'TipoInstalacao': 'Tipo Instalacao',
                'Navegacao': 'Navegacao',
                'SentidoCarga': 'Sentido Carga',
                'PerfilCarga': 'Perfil Carga',
                'Toneladas': 'Toneladas'},
            #color='Toneladas',
            #color_continuous_scale=px.colors.sequential.Viridis
            )
        fig.update_layout(
            title='Fluxo da Carga Movimentada 2005',
            xaxis_tickfont_size=14,
                margin=dict(r=170, l=120),
            coloraxis_colorbar=dict(
                #title="Toneladas",
                x=1.2  # Move a barra de cores mais para a direita
            ),
            width=1000,
            height=600)
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        # Filtrando os dados de 2022 e agrupando os dados pelas variáveis categóricas
        grpMov = movimentacaoGeo.query('Ano==2022').groupby(['TipoInstalacao', 'PerfilCarga', 'TipoOperacao', 
            'Navegacao', 'SentidoCarga', 'Carga']).agg(
            Qtd=('Data','count'), Toneladas=('Toneladas','sum'), 
            TEUs=('TEUs','sum'), Unidades=('Unidades','sum')
            ).reset_index().sort_values(by=['TipoInstalacao', 'PerfilCarga', 'TipoOperacao', 
            'Navegacao', 'SentidoCarga', 'Carga'])
        #grpMov

        # Para resolver um problema de versão do pandas e plotly
        pd.DataFrame.iteritems = pd.DataFrame.items

        # Gráfico de coordenadas paralelas
        fig = px.parallel_categories(grpMov, 
            dimensions=['TipoInstalacao', 'Navegacao', 'SentidoCarga', 'PerfilCarga', 'Carga'],
            labels={'TipoInstalacao': 'Tipo Instalacao',
                'Navegacao': 'Navegacao',
                'SentidoCarga': 'Sentido Carga',
                'PerfilCarga': 'Perfil Carga',
                'Toneladas': 'Toneladas'},
            #color='Toneladas',
            #color_continuous_scale=px.colors.sequential.Viridis
            )
        fig.update_layout(
            title='Fluxo da Carga Movimentada 2022',
            xaxis_tickfont_size=14,
                margin=dict(r=170, l=120),
            coloraxis_colorbar=dict(
                #title="Toneladas",
                x=1.2  # Move a barra de cores mais para a direita
            ),
            width=1000,
            height=600)
        st.plotly_chart(fig, use_container_width=True)
    with tab3:
        import plotly.graph_objects as go

        # Lista das top 10 cargas
        listTop10 = movimentacaoGeo.query('Ano==2022').groupby(['Carga']).agg(Toneladas=('Toneladas','sum')).reset_index().nlargest(10, 'Toneladas')['Carga'].tolist()

        # Filtrando os dados de 2022 e agrupando os dados pelas variáveis categóricas
        grpMov = movimentacaoGeo.query('Ano==2022' and 'Carga in @listTop10').groupby(['TipoInstalacao', 'PerfilCarga', 'TipoOperacao', 
            'Navegacao', 'SentidoCarga', 'TerminalAjustado', 'Carga']).agg(
            Qtd=('Data','count'), Toneladas=('Toneladas','sum')
            ).reset_index()
        #grpMov

        df = grpMov

        # Preparar dados para o gráfico de Sankey
        def prepare_sankey_data(df, cat_cols, value_col):
            nodes = []
            for col in cat_cols:
                nodes.extend(list(df[col].unique()))
            nodes = list(pd.Series(nodes).unique())
            
            node_indices = {node: i for i, node in enumerate(nodes)}
            
            sources = []
            targets = []
            values = []

            for i in range(len(cat_cols) - 1):
                source_col = cat_cols[i]
                target_col = cat_cols[i + 1]
                
                grouped_df = df.groupby([source_col, target_col])[value_col].sum().reset_index()
                
                for _, row in grouped_df.iterrows():
                    sources.append(node_indices[row[source_col]])
                    targets.append(node_indices[row[target_col]])
                    values.append(row[value_col])

            return nodes, sources, targets, values

        cat_cols = ['TipoInstalacao', 'Navegacao', 'SentidoCarga', 'PerfilCarga', 'Carga']
        value_col = 'Toneladas'

        nodes, sources, targets, values = prepare_sankey_data(df, cat_cols, value_col)

        # Criar o gráfico de Sankey
        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=nodes
            ),
            link=dict(
                source=sources,
                target=targets,
                value=values
            ))])

        fig.update_layout(title_text="Fluxo de Cargas 2022", font_size=14)
        st.plotly_chart(fig, use_container_width=True)
    with tab4:
        # Agrupando os dados de um ano fechado
        grpTerminalCarga = movimentacaoGeo.query('Ano==2022').groupby(['TerminalAjustado','Carga']).agg(Toneladas=('Toneladas','sum'),).reset_index()
        df = grpTerminalCarga.nlargest(30, 'Toneladas')

        # Pivotar os dados para criar uma tabela de terminais vs cargas
        pivot_df = df.pivot_table(values='Toneladas', index='Carga', columns='TerminalAjustado', aggfunc='sum', fill_value=0)

        # Criar o heatmap
        fig = px.imshow(pivot_df, 
                        labels=dict(x="Terminal", y="Carga", color="Toneladas"),
                        x=pivot_df.columns,
                        y=pivot_df.index,
                        color_continuous_scale='Viridis')

        fig.update_layout(title='Volume Movimentado por Carga vs Terminais',
            width=1000, height=700)
        fig.update_xaxes(tickangle=90)
        st.plotly_chart(fig, use_container_width=True)

