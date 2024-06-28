import pandas as pd
import numpy as np
import streamlit as st

import locale




st.set_page_config(
    page_title="Porto de Santos - Movimentação",
    page_icon="🏂",
    layout="wide"
    )

import menu as menu
menu.menu()


import streamlit.components.v1 as components
linkGoogleDocs = "https://docs.google.com/presentation/d/1sGeNsiFTRcyuDm83pa0SfNzort-rDcRMGtjt5QCyyGY"

linkPPTlocal = "./src/utils/visualization/img/ApresentacaoMECAI.pptx"


from PIL import Image
import os
camImages = "./src/utils/visualization/img/"
# Lista das imagens (nomes dos arquivos)
image_files = ["Slide3.JPG", "Slide5.JPG", "Slide6.JPG","Mensario1.png"]
image_folder = "./src/utils/visualization/img/"

# Função para carregar a imagem atual
def load_image(index):
    image_path = os.path.join(image_folder, image_files[index])
    return Image.open(image_path)

# Estado para manter o índice da imagem atual
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
col1, col3,col2 = st.columns([2,9, 2])
with col1:
    # Botão para avançar para o próximo slide
    if st.button("Anterior"):
        st.session_state.current_index -= 1
        if st.session_state.current_index == -1:
            st.session_state.current_index = len(image_files)-1
with col3:
    pass
with col2:
# Botão para avançar para o próximo slide
    if st.button("Próximo"):
        st.session_state.current_index += 1
        if st.session_state.current_index >= len(image_files):
            st.session_state.current_index = 0

# Carregar a imagem atual
current_image = load_image(st.session_state.current_index)

# Mostrar a imagem
st.image(current_image, width=800)

# Mostrar a legenda da imagem
#st.caption(f"Slide {st.session_state.current_index + 1} de {len(image_files)}")