import streamlit as st
import pandas as pd

st.set_page_config(page_title="Trend Analyzer", layout="wide")


st.markdown("""
<style>
body {
    background-color: #f0f2f6;
}
h1 {
    color: #2E86C1;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("📈 Trend Analyzer Dashboard")


df = pd.read_csv("students.csv.csv")

st.success("✅ Data Loaded Successfully")


num_cols = df.select_dtypes(include=['int64','float64']).columns

if len(num_cols) > 0:

    col = st.selectbox("Select Metric", num_cols)

    st.subheader("📊 Trend Analysis")
    st.line_chart(df[col])   


    window = st.slider("Select Moving Average Window", 2, 10, 3)
    df["moving_avg"] = df[col].rolling(window).mean()

    st.subheader("📉 Moving Average")
    st.area_chart(df["moving_avg"])   # different color style


    st.subheader("📋 Summary")

    c1, c2, c3 = st.columns(3)
    c1.metric("Average", round(df[col].mean(), 2), delta="Good")
    c2.metric("Highest", df[col].max(), delta="High")
    c3.metric("Lowest", df[col].min(), delta="Low")


    st.markdown("### 🎯 Insights")
    if df[col].mean() > df[col].median():
        st.success("Data is slightly skewed positively 📈")
    else:
        st.warning("Data is slightly skewed negatively 📉")

else:
    st.error("No numeric columns found!")