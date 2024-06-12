import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import time
import locale
import seaborn as sns
import matplotlib.pyplot as plt

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')



st.set_page_config(
    page_title="Port of Santos Container  Visualization",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")






#streamlit run app.py





st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/portos.py", label="Page 1", icon="1️⃣")
#st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
#st.page_link("http://www.google.com", label="Google", icon="🌎")



# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )


df = pd.DataFrame(pd.read_csv('./Data/combined_file.csv', encoding='utf8', sep=","))

# Título e Introdução
st.title('Análise das Operações Portuárias')
st.write('Este dashboard apresenta uma análise detalhada das operações portuárias baseadas em um conjunto de dados contendo informações de cargas movimentadas ao longo dos anos.')

# Análise Temporal
st.header('Análise Temporal')
fig1 = px.line(df, x='Mes', y='Toneladas', color='Ano', title='Volume de Carga ao Longo do Tempo')
st.plotly_chart(fig1)
st.write('Observamos tendências sazonais significativas, com picos de atividade em determinados meses. Isso pode ser devido a ...')

# Distribuição de Cargas por Berço e Terminal
st.header('Distribuição de Cargas por Berço e Terminal')
fig2 = px.bar(df, x='Terminal', y='Toneladas', color='Berco', title='Volume de Carga por Terminal e Berço')
st.plotly_chart(fig2)
st.write('Os terminais mais utilizados são ..., indicando a necessidade de ...')

# Perfil da Carga e Tipo de Operação
st.header('Perfil da Carga e Tipo de Operação')
fig3 = px.scatter(df, x='PerfilCarga', y='Toneladas', color='TipoOperacao', size='Toneladas', title='Distribuição das Cargas por Perfil e Tipo de Operação')
st.plotly_chart(fig3)
st.write('Podemos ver que operações de ... são predominantes para cargas do tipo ..., sugerindo que ...')

# Fluxo de Navegação e Sentido da Carga
##st.header('Fluxo de Navegação e Sentido da Carga')
#fig4 = px.sankey(df, node=dict(label=['Navegação', 'SentidoCarga']), link=dict(source=[...], target=[...], value=[...]))
#st.plotly_chart(fig4)
#st.write('O fluxo de cargas entre navegação de cabotagem e longo curso mostra que ...')

# Tipo de Instalação e Volume de Carga
st.header('Tipo de Instalação e Volume de Carga')
fig5 = px.pie(df, names='TipoInstalacao', values='Toneladas', title='Volume de Carga por Tipo de Instalação')
st.plotly_chart(fig5)
st.write('As instalações mais utilizadas são ..., o que sugere que ...')

# Mapa Geográfico de Cargas Movimentadas
st.header('Mapa Geográfico de Cargas Movimentadas')
#fig6 = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', size='Toneladas', color='Terminal', mapbox_style='open-street-map', title='Distribuição Geográfica das Operações Portuárias')
#st.plotly_chart(fig6)
st.write('A distribuição geográfica das operações revela que ...')

# Análise de Correlações entre Variáveis
st.header('Análise de Correlações entre Variáveis')
corr = df.corr()
fig7, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig7)
st.write('A matriz de correlação indica que há uma forte relação entre ...')

# Conclusão
st.header('Conclusão')
st.write('Com base na análise acima, identificamos que ..., o que nos leva a concluir que ...')
