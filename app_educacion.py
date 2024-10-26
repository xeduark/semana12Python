import streamlit as st
import pandas as pd
import altair as alt

# Cargar el archivo CSV (si se carga uno)
uploaded_file = st.file_uploader("Cargar archivo 'educacion.csv'", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    # Cargar el archivo CSV por defecto si no se carga uno
    df = pd.read_csv("educacion.csv")

# Interfaz de usuario con Streamlit
st.title("Análisis de Datos de Educación en Colombia")
st.dataframe(df) 

# Filtros
st.sidebar.header("Filtros")

# Filtro por nivel educativo
nivel_educativo = st.sidebar.multiselect("Nivel educativo", df["Nivel educativo"].unique())

# Filtro por carrera
carrera = st.sidebar.multiselect("Carrera", df["Carrera"].unique())

# Filtro por institución
institucion = st.sidebar.multiselect("Institución", df["Institución"].unique())

# Filtrar el DataFrame
df_filtrado = df.copy()
if nivel_educativo:
    df_filtrado = df_filtrado[df_filtrado["Nivel educativo"].isin(nivel_educativo)]
if carrera:
    df_filtrado = df_filtrado[df_filtrado["Carrera"].isin(carrera)]
if institucion:
    df_filtrado = df_filtrado[df_filtrado["Institución"].isin(institucion)]

# Mostrar DataFrame filtrado
st.dataframe(df_filtrado)

# Estadísticas Descriptivas
st.subheader("Estadísticas Descriptivas")
st.write(df_filtrado.describe())

# Visualizaciones
st.subheader("Conteo de Estudiantes por Nivel Educativo")
st.bar_chart(df_filtrado["Nivel educativo"].value_counts())

# Histograma de edades
st.subheader("Distribución de la Edad")
histograma = alt.Chart(df_filtrado).mark_bar().encode(
    alt.X("Edad", bin=True),
    alt.Y("count()")
)
st.altair_chart(histograma)