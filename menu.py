import streamlit as st
from streamlit_extras.app_logo import add_logo


def readImage(img):
  import base64

  with open(img, "rb") as f:
    return base64.b64encode(f.read()).decode("utf-8")

def unauthenticated_menu():

  st.html("""
    <style>
      [alt=Logo] {
        height: 3rem;
      }
    </style>
          """)


  st.logo("./src/utils/visualization/img/logoColor.png", icon_image="./src/utils/visualization/img/LogoSbranco.png")
  st.sidebar.page_link("app.py", label="Home", icon="🏠")
# 
  st.sidebar.page_link("pages/analiseGeralVolumes.py", label="Análise Geral do Volumes", icon="🏗")
  st.sidebar.page_link("pages/analiseCargas.py", label="Análise de Cargas", icon="🚢")
  st.sidebar.page_link("pages/analiseTerminais.py", label="Análise de Terminais", icon="⚓")
  st.sidebar.page_link("pages/terminais.py", label="Localização dos Terminais", icon="🗺️")

  st.sidebar.page_link("pages/atracacoes.py", label="Plus: Principais Cargas", icon="📊")
  st.sidebar.page_link("pages/visualizacoes.py", label="Plus: Visual. Dimensões Carga", icon="📊")
  
  
  st.sidebar.page_link("pages/about.py", label="Equipe...", icon="🧑🏻‍💻")




# Classes proprias
def menu():
    unauthenticated_menu()
