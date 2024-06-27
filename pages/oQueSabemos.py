import pandas as pd
import numpy as np
import streamlit as st

import locale


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

st.set_page_config(
    page_title="Porto de Santos - Movimentação",
    page_icon="🏂",
    layout="wide"
    )

import menu as menu
menu.menu()


from streamlit_elements import elements, mui, html, sync

IMAGES = [
    "https://1spa.sharepoint.com/sites/SEGTI/_layouts/15/embed.aspx?UniqueId=862500a4-6239-4545-89a2-d2e84d03b97a",
    "https://1spa.sharepoint.com/sites/SEGTI/_layouts/15/embed.aspx?UniqueId=3a46bf94-b9f8-4003-9d18-fcfb4415c3fe",
    "https://1spa.sharepoint.com/sites/SEGTI/_layouts/15/embed.aspx?UniqueId=dfd62a2c-a324-4b1c-8a0e-a60b086432f6",
]




from streamlit_carousel import carousel

test_items = [
    dict(
        title="Slide 1",
        text="A tree in the savannah",
        img="./src/utils/visualization/img/Slide3.JPG",
        link="https://discuss.streamlit.io/t/new-component-react-bootstrap-carousel/46819"
    ),
    dict(
        title="Slide 2",
        text="A wooden bridge in a forest in Autumn",
        img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
        link="https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel"
    ),
    dict(
        title="Slide 3",
        text="A distant mountain chain preceded by a sea",
        img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
        link="https://github.com/thomasbs17/streamlit-contributions/tree/master"
    ),
]

carousel(items=test_items, width=0.5)