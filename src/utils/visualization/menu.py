import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

# Cria Menu da aplicação


def streamlit_menu(example=1):

    #Linha 1: Texto do Link
    #Linha 2: Icones do Bootstrap: https://icons.getbootstrap.com/#icons
    menu=[["Home", "Atracações","Portos", "Equipe"],
           ["house", "1-circle-fill","portos", "people"]
        ]
    
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=menu[0],  # required
                icons=menu[1],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        with st.container():
            selected = option_menu(
                menu_title=None,  # required
                options=menu[0],  # required
                    icons=menu[1],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                orientation="horizontal",
            )
        return selected

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=menu[0],  # required
                icons=menu[1],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected

    #if selected == "Home":
    #    switch_page("home")
    #if selected == "Atracações":
    #    switch_page("atracacoes")
