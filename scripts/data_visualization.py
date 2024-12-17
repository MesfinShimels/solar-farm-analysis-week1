import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
# Function to plot publication trends over time
def plot_publication_trends(publication_counts):
    """
    Plot trends in publication frequency.
    
    Args:
    - publication_counts: A pandas Series with dates as the index and article counts as values.
    """
    plt.figure(figsize=(10, 6))
    publication_counts.plot(kind='line', color='b', lw=2)
    plt.title('Publication Frequency Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles')
    plt.grid(True)
    plt.show()


# Example of calling the functions with a sample dataset
if __name__ == "__main__":
    import pandas as pd

    # Sample data loading (replace this with actual data loading)
    # publication_counts and sentiment_data should be loaded from your analysis pipeline
    publication_counts = pd.Series([5, 7, 10, 12, 9], 
                                   index=pd.date_range('2024-01-01', periods=5, freq='D'))
    sentiment_data = pd.DataFrame({
        'headline': ['Headline 1', 'Headline 2', 'Headline 3', 'Headline 4', 'Headline 5'],
        'sentiment': [0.1, -0.2, 0.0, 0.3, -0.1]
    })
    
    # Call the functions
    plot_publication_trends(publication_counts)
    plot_sentiment_distribution(sentiment_data)






def plot_close_price_with_moving_averages(df, file_name):
    """
    Plots the Close Price with Moving Averages (SMA 10, SMA 20).
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], label="Close Price", color='blue')
    plt.plot(df.index, df['SMA_10'], label="SMA 10", linestyle='--', color='red')
    plt.plot(df.index, df['SMA_20'], label="SMA 20", linestyle='--', color='green')
    plt.title(f"{file_name} - Close Price with Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()



def plot_rsi(df, file_name):
    """
    Plots the Relative Strength Index (RSI) indicator.
    """
    plt.figure(figsize=(12, 4))
    plt.plot(df.index, df['RSI'], color='purple', label='RSI')
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.title(f"{file_name} - Relative Strength Index (RSI)")
    plt.legend()
    plt.show()

def plot_macd(df, file_name):
    """
    Plots the MACD indicator, Signal line, and Histogram.
    """
    plt.figure(figsize=(12, 5))
    plt.plot(df.index, df['MACD'], label='MACD', color='orange')
    plt.plot(df.index, df['MACD_signal'], label='MACD Signal', linestyle='--', color='blue')
    plt.bar(df.index, df['MACD_hist'], label='MACD Histogram', color='gray')
    plt.title(f"{file_name} - MACD")
    plt.legend()
    plt.show()









def plot_sentiment_vs_stock(merged_df):
    """
    Plots the relationship between sentiment and stock returns.
    
    Args:
    - merged_df (DataFrame): Merged DataFrame containing 'Sentiment' and 'Stock_Return'.
    """
    plt.figure(figsize=(15,15))
    plt.scatter(merged_df['Sentiment'], merged_df['Stock_Return'], alpha=0.5)
    plt.title("Sentiment vs Stock Returns")
    plt.xlabel("Sentiment")
    plt.ylabel("Stock Return (%)")
    plt.show()



# Plot sentiment distribution function
def plot_sentiment_distribution(news_df):
    """
    Plots a histogram of sentiment scores for the given DataFrame.
    
    Args:
    - news_df (DataFrame): DataFrame containing a 'Sentiment' column.
    """
    try:
        if 'Sentiment' not in news_df.columns or news_df.empty:
            print("No sentiment data available to plot.")
            return

        # Plot histogram of sentiment scores
        plt.figure(figsize=(10, 6))
        plt.hist(news_df['Sentiment'], bins=20, color='skyblue', edgecolor='black')
        plt.title("Sentiment Distribution", fontsize=16)
        plt.xlabel("Sentiment Score", fontsize=14)
        plt.ylabel("Frequency", fontsize=14)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
        print("Sentiment distribution plot displayed.")
    except Exception as e:
        print(f"Error plotting sentiment distribution: {e}")
        raise