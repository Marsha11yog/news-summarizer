from transformers import pipeline
import streamlit as st

# Cache the summarization pipeline so it's loaded only once @st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

def summarize_text(text):
    if not text or not text.strip():
        st.warning("⚠️ No content provided for summarization.")
        return "No content to summarize."

    try:
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        st.error(f"❌ Summarization failed: {e}")
        return "Error: Could not summarize the content."
