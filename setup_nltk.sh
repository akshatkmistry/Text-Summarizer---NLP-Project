#!/bin/bash
echo "Installing NLTK data..."
python -c "
import nltk
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

print('Downloading punkt_tab...')
nltk.download('punkt_tab', quiet=True)
print('Downloading punkt...')
nltk.download('punkt', quiet=True)
print('Downloading stopwords...')
nltk.download('stopwords', quiet=True)
print('Downloading vader_lexicon...')
nltk.download('vader_lexicon', quiet=True)
print('NLTK data download complete!')
"
echo "NLTK data installation completed!"