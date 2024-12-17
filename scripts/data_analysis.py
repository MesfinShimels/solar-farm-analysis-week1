import pandas as pd
from textblob import TextBlob
from collections import Counter
import re
from talib import SMA, RSI, MACD
from scipy.stats import pearsonr

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



def extract_keywords(data, column='headline', n=10):
    """Extract common keywords from the text."""
    all_text = ' '.join(data[column].dropna())
    words = re.findall(r'\b\w+\b', all_text.lower())
    return Counter(words).most_common(n)


# data_analysis.py



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





def prepare_data(news_df, stock_df):
    """
    Prepares and aligns news and stock price data by date.
    
    Args:
    - news_df (DataFrame): News data with 'date' and 'Sentiment' columns.
    - stock_df (DataFrame): Stock price data with 'Date' and 'Close' columns.
    
    Returns:
    - DataFrame: Merged DataFrame with daily returns and sentiment scores.
    """
    try:
        # Standardize the 'date' columns to ISO 8601 format
        news_df['date'] = pd.to_datetime(news_df['date'], errors='coerce', format='%Y-%m-%d').dt.date
        stock_df['Date'] = pd.to_datetime(stock_df['Date'], errors='coerce', format='%Y-%m-%d').dt.date

        # Remove rows with invalid dates (optional)
        news_df = news_df.dropna(subset=['date'])
        stock_df = stock_df.dropna(subset=['Date'])

        # Merge DataFrames on the standardized date
        print("Merging stock and news data...")
        merged_df = pd.merge(stock_df, news_df[['date', 'Sentiment']], how='left', left_on='Date', right_on='date')

        # Calculate daily returns for stock prices
        merged_df['Stock_Return'] = merged_df['Close'].pct_change() * 100
        print("Merge complete. First 5 rows:")
        print(merged_df.head())

        return merged_df

    except Exception as e:
        print(f"Error preparing data: {e}")
        return None



def sentiment_analysis(news_df):
    """
    Analyzes sentiment of news headlines and adds a 'Sentiment' column.
    
    Args:
    - news_df: DataFrame containing news data with a 'headline' column.
    
    Returns:
    - news_df: DataFrame with an added 'Sentiment' column.
    """
    try:
        # Perform basic sentiment analysis
        news_df['Sentiment'] = news_df['headline'].apply(
            lambda x: 1 if 'positive' in x.lower() else -1 if 'negative' in x.lower() else 0
        )
    except KeyError as e:
        raise KeyError(f"Missing required column in news_df: {e}")
    
    # Debug: Check the first few rows
    print("First 5 rows of news_df with Sentiment:")
    print(news_df[['headline', 'Sentiment']].head())
    
    return news_df




def calculate_correlation(merged_df):
    """
    Calculates the correlation between sentiment and stock returns.
    
    Args:
    - merged_df (DataFrame): Merged DataFrame containing 'Sentiment' and 'Stock_Return'.
    
    Returns:
    - float: Correlation value.
    """
    correlation = merged_df[['Sentiment', 'Stock_Return']].corr().iloc[0, 1]
    return correlation











