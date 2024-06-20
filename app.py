import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import time
import locale
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Port of Santos Container  Visualization",
    page_icon="🏂",
    layout="wide"
    )


import menu as menu
menu.menu()

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')






titulo = 'Modelos de Previsão de demanda para Comodities de Granel Sólido Vegetal para o Porto de Santos, Brasil'
st.markdown("<h1 style='text-align: center;'>"+titulo+"</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
   
   st.image("./src/utils/visualization/img/porto-santos.jpg")

with col2:
   
    para0 = '''
            Este estudo propõe uma análise comparativa de métodos econométricos para previsão de volumes de 
            carga em um porto de exportação de commodities agrícolas, especificamente soja, milho e açúcar. 
            A previsão precisa do volume de carga é de extrema importância para a eficiência das operações 
            portuárias, a alocação adequada de recursos logísticos e a tomada de decisões estratégicas.
            '''
    para1 = '''
            O estudo compreende uma seleção de métodos econométricos, incluindo modelos de séries temporais,
            modelos de regressão e técnicas de aprendizado de máquina aplicadas ao contexto econômico. A
            base de dados utilizada abrange um período significativo de observações históricas dos volumes de
            carga das commodities em questão. Cada método é implementado e avaliado considerando métricas
            de desempenho como erro médio absoluto, erro quadrático médio, erro percentual médio absoluto e
            arctangente do erro percentual médio absoluto.
            '''
    para2 = '''
            Os resultados da análise comparativa oferecem insights sobre a eficácia relativa de cada método
            na previsão dos volumes de carga. Além disso, considerações sobre a estabilidade e robustez dos
            modelos diante de diferentes cenários econômicos são abordadas. A análise também explora a
            capacidade dos modelos de capturar sazonalidades, tendências e possíveis eventos disruptivos que
            possam afetar os volumes de carga.
            '''
    st.markdown("<p style='text-align: justify;'>"+para0+"</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>"+para1+"</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>"+para2+"</p>", unsafe_allow_html=True)