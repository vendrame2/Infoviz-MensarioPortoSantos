import streamlit as st

st.set_page_config(
    page_title="Port of Santos Container  Visualization",
    page_icon="🏂",
    layout="wide"
    )

import menu as menu
menu.menu()

camImg = "./src/utils/visualization/img/equipe/"   
    
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Luiz Vendrame")

    st.image(camImg+"vendrame.jpg", width=200)
    st.divider()
    st.markdown("**NUSP:** 13807101")
    st.markdown("**No projeto:** Organização do Dataset, prototipagem inicial, Visualizações Geolocalizadas")
    

 
with col2:
    st.subheader("Denilson Nishida")
    st.image(camImg+"denilson.jpg", width=200)
    st.divider()
    st.markdown("**NUSP:** 3032206")
    st.markdown("**No projeto:** Data storytelling, Insights de negócio e visualizações de dados")
    
with col3:
    st.subheader("Ricardo Maeshiro")
    st.image(camImg+"maeshiro.jpg", width=200)

    st.divider()
    st.markdown("**NUSP:** 11025395")
    st.markdown("**No projeto:** Data storytelling para o Porto de Santos, Insights para visualizações de dados, Revisão de informações geolocalizadas")
    
