import streamlit as st
import pandas as pd

st.title("馬券戦略アプリ 🏇")

uploaded_file = st.file_uploader("TARGET JV CSVファイルをアップロード", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("データプレビュー", df.head())