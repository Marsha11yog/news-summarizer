# News Article Summarizer 
A GenAI - powered Streamlit web app that summarizes any online news article using Hugging Face's BART model.

## Features 
- Paste any article url
- Extracts full article text using `newspaper3k` and `BeautifulSoup`
- Summarizes the content with `facebook/bart-large-cnn`
- Fallback scraping in case of structured content failures

## Tools
- Python
- Streamlit
- Hugging Face Transformers
- newspaper3k
- BeautifulSoup
- Readability-lxml

## Result:

![result](https://github.com/user-attachments/assets/5a613a31-3c6b-4139-abb0-f5f3223a6e84)


## Future Improvements

- Support summarizing multiple articles (10–15) at once, either from a list of URLs or daily newspaper pages
- Build a "Daily Digest" feature that summarizes all articles from a newspaper homepage and presents them categorically
- Allow file uploads (e.g., PDFs or DOCs) to summarize offline content
- Integrate Retrieval-Augmented Generation (RAG) to:
  - Provide summaries with contextual background pulled from trusted sources
  - Answer user questions about the article using embedded content
- Add options to export summary as PDF or email it
