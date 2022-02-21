import streamlit as st
import pandas as pd
import requests
import json
from PIL import Image
# API # https://unstats.un.org/SDGAPI/swagger/#!/Indicator/V1SdgIndicatorListGet

import geopandas
import geopandas as gpd
from streamlit_folium import folium_static
#import fiona
import io

icon = Image.open("SDG Wheel_PRINT_Transparent.png")
st.set_page_config(layout='wide', page_title='Objetivos de Desenvolvimento Sustentável', page_icon=icon)

#Declaring streamlit containers
header = st.container()
user_input = st.container()
output_graphs = st.container()
author_credits = st.container()

#bairros = 'bairros_novo.geojson'
#df_bairros = gpd.read_file(bairros)

url = "https://unstats.un.org/SDGAPI/v1/sdg/Indicator/List"
df = pd.read_json(url)
print(df)

#casos = '2022-01-19_Casos_Covid_19_-_Base_de_Dados.csv'
#df_casos = pd.read_csv(casos, encoding='latin1', delimiter=';')

with user_input:
    table_days = st.sidebar.slider('Escolha a quantidade de indicadores ODS que você quer ver na tabela. ', min_value=3,
                                   max_value=17, value=4, step=1)

with output_graphs:
    st.header(f'Resumo dos {table_days} ODS escolhidos.')
    st.markdown(""" Essa tabela apresenta uma lista dos indicadores ODS atualmente publicados.""")

    # st.write(df_county.iloc[-table_days:,-4:])
    a = df.iloc[-table_days:, -10:]
    my_table = st.table(a)
#casos_por_bairro = df_casos.groupby("BAIRRO")[['CLASSIFICAÇÃO FINAL']].count().reset_index()
# Row number (Zero): This is to give the App title:

with header:
    titl, imga = st.columns((4, 1))
    imga.image('E_SDG_logo_UN_emblem_square_trans_WEB.png')
    titl.title('Objetivos de Desenvolvimento Sustentável da ONU')
    #st.subheader("An open source application, free-to-reuse for managing and publishing data and maps related to the Sustainable Development Goals (SDGs).")
    st.write('***Uma aplicação open-source, reprodutível, para gerenciar e publicar dados e mapas relacionados aos Objetivos de Desenvolvimento Sustentpavel (ODS).')


sidebar_selection = st.sidebar.radio(
    'Selecione o ODS:',
    ['Erradicação da pobreza', 'Fome Zero e Agricultura Sustentável', 'Saúde e Bem-Estar'],)

if sidebar_selection == 'Erradicação da pobreza':
    st.markdown('## Erradicar a pobreza em todas as formas e em todos os lugares')

elif sidebar_selection == 'Fome Zero e Agricultura Sustentável':
    st.markdown('## Erradicar a fome, alcançar a segurança alimentar, melhorar a nutrição e promover a agricultura sustentável')

elif sidebar_selection == 'Saúde e Bem-Estar':
    st.markdown('## Garantir o acesso à saúde de qualidade e promover o bem-estar para todos, em todas as idades')



# Row number (1): This is to give the App Introduction: we'll have 5 Columns:
# null1_1, row1_2, null1_2, row1_3, null1_3 = st.beta_columns((0.23, 5, 0.3, 5, 0.17))

# Let's upload the painted Ladies image:
# image = Image.open("house_5.JPG")
# let's specify which column, fix its width and let's give this image a caption:
# row1_2.image(Image.open("house_8.JPG"), use_column_width=True, caption='San Francisco - The Painted Ladies')

# Row number (2): in this row we'll have 6 columns:
# null2_1, row2_1, row2_2, row2_3 , row2_4, row2_5= st.beta_columns((0.1, 2.8,0.1, 0.8, 0.8, 0.1))

with author_credits:
    # st.header(f'Créditos')
    st.write("""
    **Obrigada por utilizar minha aplicação!** 

    Os dados utilizado foram disponibilizados pela [Prefeitura Municipal de Curitiba](https://www.curitiba.pr.gov.br/dadosabertos/busca/?pagina=2).
    Essa aplicação usa a biblioteca Streamlit.    
    """)