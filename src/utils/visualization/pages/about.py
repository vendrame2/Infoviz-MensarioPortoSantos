import streamlit as st
from streamlit_option_menu import option_menu

import plotly.graph_objects as go

import pandas as pd

import pprint as pp

#ImportsProjeto
from src.utils.data import getBercosData as bercos


def app():

    
    dfPoligono, dfBercosPDZ = bercos.convertbercosPDZDataFrame()

    st.dataframe(dfPoligono)
    st.dataframe(dfBercosPDZ)

    """
    # Geographic Map
    fig = go.Figure(
        glpt.polyplot(
            geo
        )
    )
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=6.6,
        mapbox_center={"lat": 46.8, "lon": 8.2},
        width=800,
        height=600,
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig)
    #fig.write_image("fig1.png")

    """








    st.subheader('Pondering is a website created for users to')
    st.subheader('share their valuable thoughts with the world.')
    st.markdown('Created by: [Ashwani Siwach](https://github.com/Ashwani132003)')
    st.markdown('Contact via mail: [siwachsahab1@gmail.com]')
    