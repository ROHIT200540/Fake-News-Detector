import streamlit as st

st.title("Fake News Detector for Students")

news = st.text_area("Enter the news article")

if st.button("Check"):
    st.success("Prediction: Fake / Real")
