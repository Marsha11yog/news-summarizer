print ("Hello World!")
import streamlit as st
from scrapper import extract_article
from summarise import summarize_text

st.title("News Article Summarizer")

url = st.text_input("Paste the article URL below:")

if st.button("Summarize"):
    title, text = extract_article(url)
    summary = summarize_text(text)
    st.subheader(f"Title: {title}")
    st.markdown(summary)


