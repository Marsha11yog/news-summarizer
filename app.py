import streamlit as st
from scrapper import extract_article
from summarise import summarize_text

st.set_page_config(page_title="News Article Summarizer", layout="centered")
st.title("📰 News Article Summarizer")

url = st.text_input("📎 Paste the article URL below:")

if st.button("Summarize"):
    if url.strip() == "":
        st.warning("⚠️ Please enter a valid URL.")
    else:
        with st.spinner("🔍 Extracting and summarizing the article..."):
            title, text = extract_article(url)
            summary = summarize_text(text)
        
        if "Error" not in summary:
            st.subheader(f"🗞 Title: {title}")
            st.markdown(f"**✍️ Summary:**\n\n{summary}")
        else:
            st.error("❌ Could not generate summary. Please try another article.")
