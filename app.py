import pandas as pd
import streamlit as st 
import plotly.express as px 
from PIL import Image

st.set_page_config(page_title='Dataset')
st.header('MLB gamelogs')
st.subheader('Dataset')

### --- DATASET
dataset = st.file_uploader("Suba el dataset que desea analizar")
if dataset:
    df = pd.read_csv(dataset, low_memory = False)
    st.dataframe(df)
else:
    st.markdown("Suba un archivo adecuado para el analisis")

graph_v_runs = st.checkbox("Gráfica de porcentaje de carreras anotadas cuando son equipos visitantes")
if graph_v_runs:
    pie_chart_v_runs = px.pie(df,
                    title = 'Carreras equipos visitantes',
                    values = 'v_score',
                    names = 'v_name')
    st.plotly_chart(pie_chart_v_runs)

graph_h_runs = st.checkbox("Gráfica de porcentaje de carreras anotadas cuando son equipos locales")
if graph_h_runs:
    pie_chart_h_runs = px.pie(df,
                    title = 'Carreras equipos locales',
                    values = 'h_score',
                    names = 'h_name')
    st.plotly_chart(pie_chart_h_runs)

graph_v_hits = st.checkbox("Gráfica de porcentajes de hits por partido cuando son equipos visitantes")
if graph_v_hits:
    pie_chart_v_hits = px.pie(df,
                    title = 'Hits de visitantes',
                    values = 'v_hits',
                    names = 'v_name')
    st.plotly_chart(pie_chart_v_hits)

graph_h_hits = st.checkbox("Gráfica de porcentajes de hits por partido cuando son equipos locales")
if graph_h_hits:
    pie_chart_h_hits = px.pie(df,
                    title = 'Hits de locales',
                    values = 'h_hits',
                    names = 'h_name')
    st.plotly_chart(pie_chart_h_hits)

graph_v_league = st.checkbox("Grafica de porcentaje de victoria de equipos visitantes en partidos interliga")
if graph_v_league:
    pie_chart_v_league = px.pie(df,
                    title = 'Carreras liga visitante',
                    values = 'v_score',
                    names = 'v_league')
    st.plotly_chart(pie_chart_v_league)

graph_h_league = st.checkbox("Grafica de porcentaje de victoria de equipos locales en partidos interliga")
if graph_h_league:
    pie_chart_h_league = px.pie(df,
                    title = 'Carreras liga local',
                    values = 'h_score',
                    names = 'h_league')
    st.plotly_chart(pie_chart_h_league)

