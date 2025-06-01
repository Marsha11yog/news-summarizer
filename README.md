# News Article Summarizer 
A GenAI - powered Streamlit web app that summarizes any online news article using Hugging Face's BART model.

## Features 
- Paste any article url
- Extracts full article text using `newspaper3k` and `BeautifulSoup`
- Summarizes the content with `facebook/bart-large-cnn`
- Fallback scraping in case of structured content failures

## Result:
![screenshot](summarizer_result/result.png)

## 🚀 Run It Locally

```bash
pip install -r requirements.txt
streamlit run app.py
