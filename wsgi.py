"""
WSGI entry point for production deployment
"""
import os
import nltk
from app import app

# Download NLTK data on startup (for production deployment)
def download_nltk_data():
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
        nltk.data.find('vader_lexicon')
    except LookupError:
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('vader_lexicon')

# Ensure NLTK data is available
download_nltk_data()

if __name__ == "__main__":
    app.run()