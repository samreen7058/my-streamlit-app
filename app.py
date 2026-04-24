import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title(" Student Data App")

df = pd.read_csv("students.csv.csv")   

st.write(df)

column = st.selectbox("Select Column", df.columns)

if st.button("Show Graph"):
    fig, ax = plt.subplots()
    df[column].hist(ax=ax)
    st.pyplot(fig)