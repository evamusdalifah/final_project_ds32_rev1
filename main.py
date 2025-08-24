import streamlit as st

st.set_page_config(page_title="Portfolio",
                   layout="wide", page_icon=":rocket:")
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman",
                        ["About", "Maternal Health Prediction"])

if page == 'About' :
    import about
    about.about()
elif page == 'Maternal Health Prediction' : 
    import project_1
    project_1.projectsatu()