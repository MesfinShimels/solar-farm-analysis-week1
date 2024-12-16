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


# data_analysis.py
import pandas as pd
from talib import SMA, RSI, MACD

def calculate_technical_indicators(df):
    """
    Calculates the following technical indicators:
    - Simple Moving Averages (SMA) for 10, 20, and 50 days
    - Relative Strength Index (RSI) for 14 days
    - MACD (Moving Average Convergence Divergence)
    
    Parameters:
    df (pd.DataFrame): The input DataFrame containing stock price data with a 'Close' column.
    
    Returns:
    pd.DataFrame: The DataFrame with calculated technical indicators added as new columns.
    """
    
    # Calculate Simple Moving Averages
    df["SMA_10"] = SMA(df["Close"], timeperiod=10)  # 10-day Simple Moving Average
    df["SMA_20"] = SMA(df["Close"], timeperiod=20)  # 20-day Simple Moving Average
    df["SMA_50"] = SMA(df["Close"], timeperiod=50)  # 50-day Simple Moving Average

    # Calculate Relative Strength Index
    df["RSI"] = RSI(df["Close"], timeperiod=14)  # 14-day Relative Strength Index

    # Calculate MACD and MACD Signal
    macd, macd_signal, macd_hist = MACD(df["Close"], fastperiod=12, slowperiod=26, signalperiod=9)
    df["MACD"] = macd
    df["MACD_signal"] = macd_signal
    df["MACD_hist"] = macd_hist

    return df
