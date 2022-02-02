import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

st.title('TESTE')
st.subheader('Tabela')
casos = ('http://dadosabertos.c3sl.ufpr.br/curitiba/CasosCovid19/2022-01-19_Casos_Covid_19_-_Base_de_Dados.csv')
df_casos = pd.read_csv(casos, encoding='latin1', delimiter=';')
#casos_por_bairro = df_casos.groupby("BAIRRO")[['CLASSIFICAÇÃO FINAL']].count().reset_index()
#df_casos.head(n=10)

st.header(f'Mapa de casos por bairro')
m = folium.Map (location = [-25.5,-49.3], tiles = 'Stamen Terrain',zoom_start = 11)
m
folium.LayerControl().add_to(m)
folium_static(m)
#DATA_URL = pd.read_csv(DATA_URL_, sep=';', encoding='latin-1')
