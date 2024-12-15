import pandas as pd
from textblob import TextBlob
from collections import Counter
import re

# Descriptive Statistics
def calculate_text_lengths(data, column='headline'):
    """Calculate the lengths of textual data."""
    data['text_length'] = data[column].apply(len)
    return data.describe()

def articles_per_publisher(data, column='publisher'):
    """Count the number of articles per publisher."""
    return data[column].value_counts()

def publication_trends(data, column='date'):
    """Analyze publication trends over time."""
    data['date'] = pd.to_datetime(data[column])
    return data.groupby(data['date'].dt.date).size()

# Text Analysis
def sentiment_analysis(data, column='headline'):
    """Perform sentiment analysis using TextBlob."""
    data['sentiment'] = data[column].apply(lambda x: TextBlob(x).sentiment.polarity)
    return data

def extract_keywords(data, column='headline', n=10):
    """Extract common keywords from the text."""
    all_text = ' '.join(data[column].dropna())
    words = re.findall(r'\b\w+\b', all_text.lower())
    return Counter(words).most_common(n)
