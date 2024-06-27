import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import locale
import pydeck as pdk

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

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

st.header("3. Análise dos Terminais")

col1, col2 = st.columns([1,3])
with col1:
    #st.subheader("Análise de Sazonalidade")
    pass
with col2:            
    mark = """
            <div style="text-align: justify;font-face: tahoma;font-size:12pt;border: 0.5px dashed #666;border-radius:10px; background-color: #eee;box-sizing: border-box;
            padding: 10px;">
                <b>Hipótese 5:</b>Alguns terminais movimentam um volume maior de carga e perfis diferentes..
            </div>
            """
    st.markdown(""+mark+"</p>", unsafe_allow_html=True)
    #st.divider()



# Agrupamento por Terminal com métricas novas
grpTerminal = movimentacaoGeo.query('Ano==2022').groupby('TerminalAjustado').agg(
    Toneladas=('Toneladas','sum'), Toneladas_Média=('Toneladas','mean'),
    TEUs=('TEUs','sum'), TEUs_Média=('TEUs','mean'), 
    Unidades=('Unidades','sum'), Unidades_Média=('Unidades','mean'),
    Qtd_PerfilCarga_Distinta=('PerfilCarga','nunique'),
    Qtd_Carga_Distinta=('Carga','nunique'),
    Qtd_Berço=('Berco','nunique')).reset_index().sort_values(by=['Toneladas'], ascending=False)

tab1, tab2, tab3, tab4 = st.tabs(["Qtde Terminais por Volume Movimentado"," Unidades vs Toneladas com Qtd Carga","Fluxo de Carga Movimentada por Terminal","Visão Geolocalizada - Perfil Carga / Ano"])
with tab1:

    import plotly.graph_objs as go
    from plotly.subplots import make_subplots

    # Selecionando os features numéricos
    features_numericos = grpTerminal.select_dtypes(include='number').columns

    # Definir o número de linhas e colunas para os subplots
    num_rows = len(features_numericos) // 2 + len(features_numericos) % 2
    num_cols = 2

    # Criar subplot
    fig = make_subplots(rows=num_rows, cols=num_cols)

    # Loop nas variáveis numéricas
    for i, var in enumerate(features_numericos):
        # Gráfico de histograma
        histogram = go.Histogram(x=grpTerminal[var], nbinsx=50, name=var)
        
        # Adicionar gráfico ao subplot
        row = i // num_cols + 1
        col = i % num_cols + 1
        fig.add_trace(histogram, row=row, col=col)
        
        fig.update_xaxes(title_text=var, row=row, col=col)
        fig.update_yaxes(title_text='Qtd Terminais', row=row, col=col)
        
    fig.update_layout(title_text="Histogramas | Quantidade de Terminais por Volume Movimentado",
                    height=num_rows * 300, width=num_cols * 450)
    st.plotly_chart(fig, use_container_width=True)
with tab2:
        # Gráfico de dispersão
    fig = px.scatter(grpTerminal, x='Unidades', y='Toneladas', size='Qtd_Carga_Distinta',
        color='TEUs',hover_name='TerminalAjustado',
        title='Gráfico de Dispersão: Unidades vs Toneladas com Qtd Carga como Tamanho dos Pontos',
        size_max=50  # Define o tamanho máximo dos círculos
    )
    fig.update_layout(
        #xaxis_title='Número de Unidades',
        #yaxis_title='Número de TEUs',
        title_x=0.5,  # Centraliza o título
        width=800,
        height=600
    )
    st.plotly_chart(fig, use_container_width=True)
with tab3:
    import plotly.graph_objects as go

    # Lista das top 10 cargas
    listTop10 = movimentacaoGeo.query('Ano==2022').groupby(['TerminalAjustado']).agg(Toneladas=('Toneladas','sum')).reset_index().nlargest(10, 'Toneladas')['TerminalAjustado'].tolist()

    # Filtrando os dados de 2022 e agrupando os dados pelas variáveis categóricas
    grpMov = movimentacaoGeo.query('Ano==2022' and 'TerminalAjustado in @listTop10').groupby(['TipoInstalacao', 'PerfilCarga', 'TipoOperacao', 
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

    cat_cols = ['TipoInstalacao', 'Navegacao', 'SentidoCarga', 'PerfilCarga', 'TerminalAjustado']
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

    fig.update_layout(title_text="Fluxo de Cargas por Terminal 2022", font_size=14)
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    

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
        


