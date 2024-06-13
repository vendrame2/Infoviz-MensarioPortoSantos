

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
from streamlit_option_menu import option_menu

# Classes proprias
from  src.utils.visualization import menu

#import das Pages
from src.utils.visualization.pages  import about, atracacoes, home, portos


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#streamlit run app.py

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            #"title": title,
            "function": func
        })

    def run():
        
        # 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
        EXAMPLE_NO = 2
        app = menu.streamlit_menu(example=EXAMPLE_NO)

        if app == "Home":
            home.app()
        if app == 'Atracações':
            atracacoes.app()    
        if app == 'Portos':
            portos.app()    
        if app == 'Equipe':
            about.app()    

             
          
             
    run()            
