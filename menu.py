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
  st.sidebar.page_link("pages/about.py", label="Equipe...", icon="1️⃣")
  st.sidebar.page_link("pages/atracacoes.py", label="Atracações", icon="1️⃣")
  st.sidebar.page_link("pages/portos.py", label="Portos", icon="1️⃣")
  st.sidebar.page_link("pages/terminais.py", label="Terminais", icon="1️⃣")
  st.sidebar.page_link("pages/visualizacoes.py", label="Visualizações EDA", icon="1️⃣")
  #st.sidebar.page_link("pages/projecoesProjeto.py", label="Modelos Preditivos", icon="1️⃣")
  #    st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
  #    st.page_link("http://www.google.com", label="Google", icon="🌎")
      #st.image("./src/utils/visualization/img/logoBranco.png", width=200) 




# Classes proprias
def menu():
    unauthenticated_menu()
