import streamlit as st
import pandas as pd

df = pd.read_csv("deputados_2022.csv")

st.title('Analise dos deputados por partido')
partido = st.text_input('coloque aqui a sigla do partido')

if partido:
  filtrado = df[df['partido'].str.upper() == partido.upper()]
  st.dataframe(filtrado)

estado = st.text_input('coloque aqui a sigla do estado')

if estado:
  filtrado = df[df['partido'].str.upper() == partido.upper()]
  st.dataframe(filtrado)

nome_civil = st.text_input('coloque aqui o nome do deputado')

if nome_civil:
  filtrado = df[df['partido'].st.upper() == partido.upper()]
  st.dataframe(filtrado)
