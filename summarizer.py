from textblob import TextBlob
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for web applications
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.probability import FreqDist
import os

def text_summarize(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]

    frequency_dist = FreqDist(words)
    max_freq = max(frequency_dist.values())
    sentence_scores = {}

    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in frequency_dist.keys():
                if sentence in sentence_scores:
                    sentence_scores[sentence] += frequency_dist[word] / max_freq
                else:
                    sentence_scores[sentence] = frequency_dist[word] / max_freq

    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]
    summary = TreebankWordDetokenizer().detokenize(summary_sentences)
    return summary

def sentiment_analysis(text):
    analysis = TextBlob(text)
    sentiment = SentimentIntensityAnalyzer()
    sent = sentiment.polarity_scores(text)
    result = ""
    if analysis.sentiment.polarity > 0:
        result = "Positive"
    elif analysis.sentiment.polarity < 0:
        result = "Negative"
    else:
        result = "Neutral"
    result = result + " : " + str(sent)
    return result
         

def word_cloud(text, filename):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    
    # Create figure and plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    ax.set_title("Word Cloud")
    
    # Save the file with original settings
    file = f'static/images/{filename}'
    fig.savefig(file, bbox_inches='tight')
    
    # Clean up to prevent memory leaks
    plt.close(fig)
    plt.clf()
    
    return file

