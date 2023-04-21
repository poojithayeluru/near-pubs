import streamlit as st
import pandas as pd
import plotly.express as px
st.title("Searching nearby pubs")
st.image("img.jpg")
df=pd.read_csv("pub.csv")
st.dataframe(df)

st.header(f"The no of columns present in data frame: {df.shape[1]}")
st.header(f"The no of rows present in dataframe: {df.shape[0]}")
df=df.drop(["Unnamed: 0"],axis=1)
st.header("Statistics about the data set:")
st.table(df.describe())

col1,col2=st.columns(2)
fig1=px.box(df["latitude"])
col1.plotly_chart(fig1,use_container_width=True)

fig1=px.box(df["longitude"])
col2.plotly_chart(fig1,use_container_width=True)

st.write("The above columns consists of outliers")
st.header("After treating outliers")

d=pd.read_csv("cleanpub.csv")
col1,col2=st.columns(2)
fig1=px.box(d["latitude"])
col1.plotly_chart(fig1,use_container_width=True)

fig1=px.box(d["longitude"])
col2.plotly_chart(fig1,use_container_width=True)
