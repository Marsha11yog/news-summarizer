# News Article Summarizer 
A GenAI - powered Streamlit web app that summarizes any online news article using Hugging Face's BART model.

## Features 
- Paste any article url
- Extracts full article text using `newspaper3k` and `BeautifulSoup`
- Summarizes the content with `facebook/bart-large-cnn`
- Fallback scraping in case of structured content failures

## Result:
![App Screenshot](summarizer_result/result.PNG)



