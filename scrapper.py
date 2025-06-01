import requests
from bs4 import BeautifulSoup
from readability import Document
import streamlit as st

def extract_article(url):
    try:
        # Primary method: newspaper3k
        from newspaper import Article
        article = Article(url)
        article.download()
        article.parse()

        if not article.text.strip():
            raise ValueError("Empty article content from newspaper3k")

        st.info("📰 Article extracted using newspaper3k")
        return article.title, article.text

    except Exception as e:
        st.warning(f"⚠️ newspaper3k failed: {e}")
        try:
            # Fallback method: readability + BeautifulSoup
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=10)
            doc = Document(response.text)
            soup = BeautifulSoup(doc.summary(), 'html.parser')
            clean_text = ' '.join(soup.stripped_strings)

            if not clean_text.strip():
                raise ValueError("Fallback method returned empty content")

            st.warning("🔍 Used fallback method (readability + BeautifulSoup)")
            return doc.title(), clean_text

        except Exception as fallback_error:
            st.error(f"❌ Failed to extract article: {fallback_error}")
            return "Error", "Could not extract article content."
