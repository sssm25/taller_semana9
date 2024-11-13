import plotly.express as px 
import streamlit as st


def cargar_datos():
    df = px.data.tips()
    st.markdown('''
                
### los datos sean cargado con éxito. :rocket:
                ''')