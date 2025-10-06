"""
WSGI entry point for production deployment
"""
import os
import nltk
import ssl
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Handle SSL certificate issues for NLTK downloads
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download NLTK data on startup (for production deployment)
def download_nltk_data():
    nltk_resources = [
        'punkt_tab',      # Updated tokenizer
        'punkt',          # Fallback for older versions
        'stopwords',      # Stopwords corpus
        'vader_lexicon'   # Sentiment analysis lexicon
    ]
    
    for resource in nltk_resources:
        try:
            # Try to find the resource first
            if resource == 'punkt_tab':
                nltk.data.find('tokenizers/punkt_tab')
            elif resource == 'punkt':
                nltk.data.find('tokenizers/punkt')
            elif resource == 'stopwords':
                nltk.data.find('corpora/stopwords')
            elif resource == 'vader_lexicon':
                nltk.data.find('vader_lexicon')
            logger.info(f"NLTK resource '{resource}' already available")
        except LookupError:
            try:
                logger.info(f"Downloading NLTK resource: {resource}")
                nltk.download(resource, quiet=True)
                logger.info(f"Successfully downloaded: {resource}")
            except Exception as e:
                logger.error(f"Failed to download {resource}: {str(e)}")

# Ensure NLTK data is available
try:
    download_nltk_data()
    logger.info("NLTK data setup completed")
except Exception as e:
    logger.error(f"Error setting up NLTK data: {str(e)}")

from app import app

if __name__ == "__main__":
    app.run()