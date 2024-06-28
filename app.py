#import pandas as pd
#import numpy as np
import streamlit as st
#import plotly.express as px
#import time
import locale
#import seaborn as sns
#import matplotlib.pyplot as plt



st.set_page_config(
    page_title="Port of Santos Container  Visualization",
    page_icon="🏂",
    layout="wide"
    )


import menu as menu
menu.menu()

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')






titulo = 'Estudo: As Transformações do Porto de Santos nos últimos 10 anos'
st.markdown("<h1 style='text-align: center;'>"+titulo+"</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
   
   st.image("./src/utils/visualization/img/porto-santos.jpg")

with col2:
   
    para0 = '''
            O Porto de Santos, localizado no estado de São Paulo, é o maior e mais importante complexo portuário da América Latina, 
            essencial para o comércio exterior brasileiro. Responsável por uma parcela significativa das importações e exportações do país, 
            o porto destaca-se pela sua infraestrutura avançada e capacidade de movimentação de diversas cargas. Entre os principais tipos de 
            cargas movimentadas estão contêineres, granéis sólidos (como soja e milho), granéis líquidos (como combustíveis e produtos químicos) 
            e carga geral (incluindo veículos e maquinários).
            '''
    st.markdown("<p style='text-align: justify;'>"+para0+"</p>", unsafe_allow_html=True)
