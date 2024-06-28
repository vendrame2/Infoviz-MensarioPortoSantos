import streamlit as st

st.set_page_config(
    page_title="Port of Santos Container  Visualization",
    page_icon="🏂",
    layout="wide"
    )

import menu as menu
menu.menu()

def plotaRoundedImageLink(img):
    # CSS para adicionar bordas arredondadas
    css = """
        <style>
        .rounded-img {
            border-radius: 50px; /* Ajuste o valor para alterar o raio da borda */
            width: 150px; /* Ajuste o tamanho da imagem conforme necessário */
        }
        </style>
        """
    # HTML para exibir a imagem com a classe CSS
    html = f"""
    <img src="{image_url}" class="rounded-img">
    """
    # Inserir o CSS e HTML no Streamlit
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(html, unsafe_allow_html=True)
    
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Luiz Carlos Vendrame Junior")
    colB, colA = st.columns([1,1])

    with colB:
        st.markdown("**NUSP:** 13807101")
        st.markdown("**No projeto:** Organização do Dataset, prototipagem inicial, Visualizações Geolocalizadas")
        st.divider()

    with colA:
        image_url = "https://media.licdn.com/dms/image/C4E03AQGSOSRR-3E3qg/profile-displayphoto-shrink_200_200/0/1655907840691?e=1724284800&v=beta&t=QEUqRRNnLwdJXfePMEdLz0dMH-vJskass1hZR57gNNU"
        plotaRoundedImageLink(image_url)  

        
    
with col2:
    st.subheader("Denilson Nishida")
    colA, colB = st.columns([1,1])
    with colA:
        image_url = "https://media.licdn.com/dms/image/C5603AQEzZnLb22Evsw/profile-displayphoto-shrink_800_800/0/1516946577071?e=1724284800&v=beta&t=utC4nh9xpQUmPK9jJMptKWnwjyHb-tIzQS0Nl2kMIk0"
        plotaRoundedImageLink(image_url)
    with colB:
        st.markdown("**NUSP:** 3032206")
        st.markdown("**No projeto:** Data storytelling, Insights e visualizações de dados")
        st.divider()
with col3:
    st.subheader("Ricardo Maeshiro")
    colA, colB = st.columns([1,1])
    with colA:
        st.image("https://scontent.fssz1-1.fna.fbcdn.net/v/t39.30808-6/299971205_5347752055272135_8989116202972533895_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=833d8c&_nc_eui2=AeFieZunlitcvr195UVWUaJx9CtRnIS7YhP0K1GchLtiEwCqMONlIPsvDwEwFVSV0tY&_nc_ohc=_D1nmLTwu-cQ7kNvgEtOcYE&_nc_ht=scontent.fssz1-1.fna&oh=00_AYDQliWG8PIeW86LbfWPb-hGaO8MEez-UaYI5_witxmMFA&oe=66813ACE")
        pass
    with colB:
        st.markdown("**NUSP:** 11025395")
        st.markdown("**No projeto:** Data storytelling, Insights para visualizações de dados, Storetelling  do Porto de Santos")
        st.divider()
