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
# def sentiment_analysis(data, column='headline'):
#     """Perform sentiment analysis using TextBlob."""
#     data['sentiment'] = data[column].apply(lambda x: TextBlob(x).sentiment.polarity)
#     return data

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






import pandas as pd

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








# working
# import pandas as pd

# def prepare_data(news_df, stock_df):
#     """
#     Prepares and aligns news and stock price data by date.

#     This function ensures consistent data types for merging, calculates daily stock returns,
#     and aligns sentiment scores with stock data.

#     Args:
#     - news_df: DataFrame containing news data with 'date' and 'Sentiment' columns.
#     - stock_df: DataFrame containing stock price data with 'Date' and 'Close' columns.

#     Returns:
#     - merged_df: Merged DataFrame with daily stock returns and sentiment scores.
#     """
#     # Ensure 'date' column in news_df is parsed as datetime and timezone is removed
#     print(f"Original 'date' dtype in news_df: {news_df['date'].dtype}")  # Debug
#     news_df['date'] = pd.to_datetime(news_df['date'], errors='coerce')
#     news_df['date'] = news_df['date'].dt.tz_localize(None)  # Remove timezone
#     print(f"Updated 'date' dtype in news_df: {news_df['date'].dtype}")  # Debug

#     # Ensure 'Date' column in stock_df is parsed as datetime
#     print(f"Original 'Date' dtype in stock_df: {stock_df['Date'].dtype}")  # Debug
#     stock_df['Date'] = pd.to_datetime(stock_df['Date'], errors='coerce')
#     print(f"Updated 'Date' dtype in stock_df: {stock_df['Date'].dtype}")  # Debug

#     # Drop rows with invalid dates (NaT) after conversion
#     news_df = news_df.dropna(subset=['date'])
#     stock_df = stock_df.dropna(subset=['Date'])

#     # Check the first few rows for debugging
#     print("First 5 rows of news_df after date conversion:")
#     print(news_df[['date', 'Sentiment']].head())
#     print("First 5 rows of stock_df after date conversion:")
#     print(stock_df[['Date', 'Close']].head())

#     # Merge the two DataFrames on date columns
#     # Ensure there are no mismatched data types
#     print("Merging stock_df and news_df...")
#     try:
#         merged_df = pd.merge(
#             stock_df, 
#             news_df[['date', 'Sentiment']], 
#             how='left', 
#             left_on='Date', 
#             right_on='date'
#         )
#         print("Merge successful!")
#     except Exception as e:
#         print(f"Merge failed: {e}")
#         return None

#     # Calculate daily stock returns
#     merged_df['Stock_Return'] = merged_df['Close'].pct_change() * 100
#     print("Daily stock returns calculated.")

#     # Debug: Check the merged DataFrame structure
#     print("First 5 rows of merged_df:")
#     print(merged_df.head())

#     return merged_df








# def prepare_data(news_df, stock_df):
#     """
#     Prepares and aligns news and stock price data by date.
    
#     Args:
#     - news_df: DataFrame containing news data with 'date' and 'headline' columns.
#     - stock_df: DataFrame containing stock price data with 'Date' and 'Close' columns.
    
#     Returns:
#     - news_df: Processed news DataFrame with sentiment scores.
#     - stock_df: Processed stock DataFrame with daily returns.
#     """
#     # Ensure the 'date' column in both DataFrames is in datetime format
#     news_df['date'] = pd.to_datetime(news_df['date'])
#     stock_df['Date'] = pd.to_datetime(stock_df['Date'])
    
#     # Align stock and news data by date (use left join to preserve all stock data)
#     merged_df = pd.merge(stock_df, news_df, how='left', left_on='Date', right_on='date')
    
#     # Calculate daily returns for stock price
#     merged_df['Stock_Return'] = merged_df['Close'].pct_change() * 100
    
#     return merged_df

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

from textblob import TextBlob

# def sentiment_analysis(news_df):
#     """
#     Analyzes sentiment of news headlines and adds a 'Sentiment' column.
    
#     Args:
#     - news_df (DataFrame): DataFrame containing a 'headline' column.
    
#     Returns:
#     - DataFrame: Updated DataFrame with a 'Sentiment' column.
#     """
#     try:
#         news_df['Sentiment'] = news_df['headline'].apply(
#             lambda x: TextBlob(x).sentiment.polarity if isinstance(x, str) else 0
#         )
#         print("Sentiment analysis complete. First 5 rows with sentiment:")
#         print(news_df[['headline', 'Sentiment']].head(20))
#         return news_df
#     except KeyError as e:
#         raise KeyError(f"Missing required column in news_df: {e}")
#     except Exception as e:
#         print(f"Error during sentiment analysis: {e}")
#         raise





# from textblob import TextBlob

# def sentiment_analysis(news_df):
#     """
#     Performs sentiment analysis on the 'headline' column using TextBlob.
    
#     Args:
#     - news_df: DataFrame containing news data with a 'headline' column.
    
#     Returns:
#     - news_df: DataFrame with sentiment scores (polarity) for each headline.
#     """
#     news_df['Sentiment'] = news_df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
#     return news_df


from scipy.stats import pearsonr

# def calculate_correlation(merged_df):
#     """
#     Calculates the Pearson correlation between sentiment scores and stock returns.
    
#     Args:
#     - merged_df: DataFrame containing 'Sentiment' and 'Stock_Return' columns.
    
#     Returns:
#     - float: Pearson correlation coefficient.
#     """
#     sentiment_series = merged_df['Sentiment'].dropna()
#     stock_return_series = merged_df['Stock_Return'].dropna()
    
#     correlation, _ = pearsonr(sentiment_series, stock_return_series)
#     return correlation







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











# working
# def calculate_correlation(merged_df):
#     """
#     Calculates the correlation between sentiment and stock returns.
    
#     Args:
#     - merged_df: Merged DataFrame containing 'Sentiment' and 'Stock_Return' columns.
    
#     Returns:
#     - correlation: Correlation value between sentiment and stock returns.
#     """
#     if 'Sentiment' not in merged_df.columns or 'Stock_Return' not in merged_df.columns:
#         raise KeyError("The 'Sentiment' or 'Stock_Return' column is missing in the DataFrame.")
    
#     # Drop rows with NaN values in relevant columns
#     clean_df = merged_df.dropna(subset=['Sentiment', 'Stock_Return'])
    
#     # Calculate correlation
#     correlation = clean_df['Sentiment'].corr(clean_df['Stock_Return'])
#     return correlation
