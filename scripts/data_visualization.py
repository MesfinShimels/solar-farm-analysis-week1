import matplotlib.pyplot as plt
import seaborn as sns

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

# Function to plot sentiment distribution
def plot_sentiment_distribution(data, column='sentiment'):
    """
    Plot the distribution of sentiment scores.
    
    Args:
    - data: A pandas DataFrame containing the sentiment data.
    - column: The column name containing sentiment scores.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], bins=30, kde=True, color='orange')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
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




# import matplotlib.pyplot as plt

# def plot_time_series(data, x_col, y_col, title="Time Series Plot"):
#     """Plots a time series."""
#     plt.figure(figsize=(10, 6))
#     plt.plot(data[x_col], data[y_col])
#     plt.title(title)
#     plt.xlabel(x_col)
#     plt.ylabel(y_col)
#     plt.grid()
#     plt.show()

# def plot_histogram(data, column, title="Histogram"):
#     """Plots a histogram for a specific column."""
#     plt.figure(figsize=(8, 5))
#     data[column].hist(bins=30)
#     plt.title(title)
#     plt.xlabel(column)
#     plt.ylabel("Frequency")
#     plt.show()
