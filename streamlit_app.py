from os import F_LOCK, path
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config( layout='wide')
def get_data(path):
    data = pd.read_csv(path)
    return data

path = 'kc_house_data.csv'
data = get_data(path)

# Data Frames

df05 = data[(data['bedrooms'] >= 0 ) & (data['price'] > 1000)]


# ====== Filtros ======

min_Price_built = int (df05['bedrooms'].min() )
max_Price_built = int (df05['bedrooms'].max()-22)
st.sidebar.subheader(' Selecione o Número de Quartos')
f_price_built =  st.sidebar.slider('Quartos', min_Price_built,max_Price_built, max_Price_built)

# Ano de Construção
min_yaer_built = int( data['yr_built'].min())
max_year_built = int(data['yr_built'].max())
st.sidebar.subheader(' Selecione o ano de construção')
f_year_built =  st.sidebar.slider('yaer built', min_yaer_built,max_year_built, min_yaer_built)

# Gráfico com plotly

# st.write (' *** Preço por número de quartos ***')
st.header(' Variação do preço e número de quartos')
df05 = data.loc[data['bedrooms' ] <= f_price_built]
df05 = df05[['bedrooms', 'price']].groupby ('bedrooms').mean().reset_index()
fig = px.line (df05, x = 'bedrooms', y = 'price')
st.plotly_chart( fig , use_container_width=True) 
#
#Gráfico2
#
st.header(' Variação do preço por ano de construção')
## st.write (' *** Preço por ano de construção ***')
df = data.loc[data['yr_built' ] < f_year_built]
df = df[['yr_built', 'price']].groupby ('yr_built').mean().reset_index()
fig = px.line (df, x = 'yr_built', y = 'price')
st.plotly_chart( fig , use_container_width=True) 







