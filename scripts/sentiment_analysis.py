from textblob import TextBlob

def sentiment_analysis(news_df, stock_ticker):
    """
    Filters news data for a specific stock and performs sentiment analysis on headlines.
    
    Args:
    - news_df (DataFrame): DataFrame containing 'headline' and 'stock' columns.
    - stock_ticker (str): Stock ticker symbol to filter news data (e.g., 'AAPL').
    
    Returns:
    - DataFrame: Filtered and updated DataFrame with a 'Sentiment' column.
    """
    try:
        # Filter news_df for the given stock_ticker
        filtered_df = news_df[news_df['stock'] == stock_ticker].copy()
        if filtered_df.empty:
            print(f"No data found for stock ticker: {stock_ticker}")
            return filtered_df

        # Perform sentiment analysis on the 'headline' column
        filtered_df['Sentiment'] = filtered_df['headline'].apply(
            lambda x: TextBlob(x).sentiment.polarity if isinstance(x, str) else 0
        )

        print(f"Sentiment analysis complete for stock: {stock_ticker}")
        print(filtered_df[['headline', 'Sentiment']].head(10))
        
        return filtered_df

    except KeyError as e:
        raise KeyError(f"Missing required column in news_df: {e}")
    except Exception as e:
        print(f"Error during sentiment analysis: {e}")
        raise
