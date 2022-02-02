# Instalando as Bibliotecas
#conda install streamlit
# pip install pyngrok
# pip install streamlit-folium
# pip install geopandas

#% % writefile covid.py
import streamlit as st
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import pandas as pd
import plotly.express as px

import matplotlib.pyplot as plt
import io
import requests
import openpyxl

# PAGE_CONFIG = {"page_title":"Casos de COVID-19 em Curitiba - PR","layout":"centered"}
# st.set_page_config(**PAGE_CONFIG)

st.set_page_config(layout="wide")

header = st.container()
user_input = st.container()
output_graphs = st.container()
author_credits = st.container()

with header:
    st.title("Casos de COVID-19 em Curitiba - PR")
    st.subheader("Secretaria de Saúde de Curitiba")
    menu = ["Home", "Mapa"]
    choice = st.sidebar.selectbox('Menu', menu)
    if choice == 'Home':
        st.subheader("Março de 2020 até Outubro de 2021")
    elif choice == 'Mapa':
        st.subheader("Visualizar Mapa")

    bairros = '/content/drive/My Drive/Desenvolvimento Geoespacial/bairros_novo.geojson'
    df_bairros = gpd.read_file(bairros)
    #casos = '/content/drive/My Drive/Desenvolvimento Geoespacial/2021-10-13_Casos_Covid_19_-_Base_de_Dados.csv'
    casos = ('http://dadosabertos.c3sl.ufpr.br/curitiba/CasosCovid19/2022-01-19_Casos_Covid_19_-_Base_de_Dados.csv')
    df_casos = pd.read_csv(casos, encoding='latin1', delimiter=';')
    casos_por_bairro = df_casos.groupby("BAIRRO")[['CLASSIFICAÇÃO FINAL']].count().reset_index()

    # with st.echo():
st.header(f'Mapa de casos por bairro')
m = folium.Map(location=[-25.5, -49.3], tiles='Stamen Terrain', zoom_start=11)
bins = list(casos_por_bairro['CLASSIFICAÇÃO FINAL'].quantile([0, 0.25, 0.5, 0.75, 1]))
folium.Choropleth(
    geo_data=df_bairros,
    name='Casos por bairro',
    data=casos_por_bairro,
    columns=['BAIRRO', 'CLASSIFICAÇÃO FINAL'],
    key_on='feature.properties.BAIRRO',
    fill_color='Reds',
    legend_name='Casos por bairro',
    bins=bins
).add_to(m)

folium.LayerControl().add_to(m)
folium_static(m)


def main():
    with user_input:
        table_days = st.sidebar.slider('Escolha a quantidade de dias que você quer ver na tabela. ', min_value=3,
                                       max_value=15, value=5, step=1)

    with output_graphs:
        st.header(f'Resumo dos últimos {table_days} casos de COVID-19.')
        st.markdown(""" Essa tabela apresenta a data, classificação, idade, sexo, bairro e status dos casos.""")

        # st.write(df_county.iloc[-table_days:,-4:])
        a = df_casos.iloc[-table_days:, -8:]
        my_table = st.table(a)

        # Total Cases Graph
        st.header(f'Total de casos para Curitiba.')
        total_cases_chart = df_casos['ENCERRAMENTO'].value_counts()
        st.bar_chart(total_cases_chart)
        st.markdown(
            """**OBS:** Você pode passar o mouse sobre a barra para ver a quantidade exata de casos e usar o mouse para aumentar ou diminuir o tamanho do gráfico.""")

        st.header(f'Total de casos por bairro.')
        total_cases_bairro = df_casos['BAIRRO'].value_counts()
        st.bar_chart(total_cases_bairro)

    with author_credits:
        # st.header(f'Créditos')
        st.markdown("""
    **Obrigada por utilizar minha aplicação!** 

    Os dados utilizado foram disponibilizados pela [Prefeitura Municipal de Curitiba](https://www.curitiba.pr.gov.br/dadosabertos/busca/?pagina=2).
    Essa aplicação usa a biblioteca Streamlit.    
    """)


if __name__ == '__main__':
    main()
