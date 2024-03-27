# Importing relevant libraries
import numpy as np
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# Loading the spaCy model
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('spacytextblob')

# Loading the dataset 
data = pd.read_csv("E:\Coding\Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv") 

# Preprocessing the text data
def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

data['clean_text'] = data['reviews.text'].apply(preprocess_text)

# Removing rows with missing values
clean_data = data.dropna(subset=['clean_text'])

# Analyzing sentiment with spaCy
def spacy_polarity(text):
    doc = nlp(text)
    polarity_value = doc._.polarity
    return polarity_value

# Analyzing sentiment for each review
clean_data['sentiment_score'] = clean_data['clean_text'].apply(spacy_polarity)

# Counting sentiment categories
positive_count = (clean_data['sentiment_score'] > 0).sum()
negative_count = (clean_data['sentiment_score'] < 0).sum()
neutral_count = (clean_data['sentiment_score'] == 0).sum()
total = len(clean_data)

positive_perc = (positive_count / total) * 100
negative_perc = (negative_count / total) * 100
neutral_perc = (neutral_count / total) * 100

print(f"Positive percentage: {positive_perc:.2f}%")
print(f"Negative percentage: {negative_perc:.2f}%")
print(f"Neutral percentage: {neutral_perc:.2f}%")

# Selecting a random sample of reviews for testing
sample_reviews = clean_data.sample(n=5)['clean_text']

# Analyzing sentiment for the sample reviews
for review in sample_reviews:
    polarity_score = spacy_polarity(review)
    if polarity_score > 0:
        sentiment = 'positive'
    elif polarity_score < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    print(f"Review: {review}")
    print(f"Sentiment: {sentiment}")
    print("--------------")
