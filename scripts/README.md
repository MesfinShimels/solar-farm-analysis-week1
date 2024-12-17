Scripts Directory
The scripts directory contains Python modules that implement various functionalities for the Stock Market Analyzer project. Each module is dedicated to a specific task, ensuring modularity and ease of maintenance.
Modules and Functions
1. data_loader.py
This module includes functions for loading datasets.
•	load_dataset(file_path)
Loads a single dataset from the given file path.
Parameters:
o	file_path (str): Path to the dataset.
Returns:
o	A Pandas DataFrame with the loaded data.
•	load_all_data(directory)
Loads all datasets from a specified directory.
Parameters:
o	directory (str): Directory containing datasets.
Returns:
o	A dictionary with file names as keys and their corresponding DataFrames as values.

2. data_analysis.py
This module focuses on analyzing the datasets for patterns and insights.
•	sentiment_analysis(news_df)
Performs sentiment analysis on the news DataFrame.
Parameters:
o	news_df (DataFrame): DataFrame containing news headlines.
Returns:
o	DataFrame with sentiment scores.
•	prepare_data(news_df, stock_df)
Prepares news and stock data for analysis by aligning dates and performing necessary preprocessing.
Parameters:
o	news_df (DataFrame): News data.
o	stock_df (DataFrame): Stock data.
Returns:
o	Two aligned DataFrames.
•	calculate_technical_indicators(df)
Computes technical indicators such as moving averages, RSI, and MACD for a stock DataFrame.
Parameters:
o	df (DataFrame): Stock price data.
Returns:
o	DataFrame with added technical indicators.
•	extract_keywords(data, column='headline', n=10)
Extracts the top n keywords from the specified column in a DataFrame.
Parameters:
o	data (DataFrame): Input data.
o	column (str): Column to extract keywords from (default: 'headline').
o	n (int): Number of keywords to extract.
Returns:
o	List of keywords.
•	publication_trends(data, column='date')
Analyzes publication trends based on dates.
Parameters:
o	data (DataFrame): Input data.
o	column (str): Date column (default: 'date').
Returns:
o	DataFrame summarizing trends over time.
•	articles_per_publisher(data, column='publisher')
Counts the number of articles per publisher.
Parameters:
o	data (DataFrame): Input data.
o	column (str): Publisher column (default: 'publisher').
Returns:
o	DataFrame summarizing article counts per publisher.
•	calculate_text_lengths(data, column='headline')
Calculates the length of text in the specified column.
Parameters:
o	data (DataFrame): Input data.
o	column (str): Text column (default: 'headline').
Returns:
o	DataFrame with added text length column.

3. data_visualization.py
This module handles data visualization.
•	plot_publication_trends(publication_counts)
Visualizes trends in publication counts over time.
Parameters:
o	publication_counts (DataFrame): Data summarizing publication counts.
Returns:
o	Matplotlib plot.
•	plot_close_price_with_moving_averages(df, file_name)
Plots stock closing prices alongside moving averages.
Parameters:
o	df (DataFrame): Stock price data with moving averages.
o	file_name (str): Path to save the plot.
Returns:
o	Matplotlib plot.
•	plot_rsi(df, file_name)
Plots the Relative Strength Index (RSI) for stock prices.
Parameters:
o	df (DataFrame): Stock data with RSI values.
o	file_name (str): Path to save the plot.
Returns:
o	Matplotlib plot.
•	plot_macd(df, file_name)
Plots the Moving Average Convergence Divergence (MACD) indicator.
Parameters:
o	df (DataFrame): Stock data with MACD values.
o	file_name (str): Path to save the plot.
Returns:
o	Matplotlib plot.
•	plot_sentiment_vs_stock(merged_df)
Compares sentiment scores with stock price movements.
Parameters:
o	merged_df (DataFrame): Merged DataFrame of sentiment and stock data.
Returns:
o	Matplotlib plot.
•	plot_sentiment_distribution(news_df)
Displays the distribution of sentiment scores in the news data.
Parameters:
o	news_df (DataFrame): News data with sentiment scores.
Returns:
o	Matplotlib plot.

4. sentiment_analysis.py
This module performs market sentiment analysis.
•	sentiment_analysis(news_df, stock_ticker)
Analyzes the sentiment of news headlines for a specific stock ticker.
Parameters: 
o	news_df (DataFrame): News headlines.
o	stock_ticker (str): Stock ticker symbol.
Returns:
o	DataFrame with sentiment analysis results.

Notes
•	Dependencies: Ensure all required Python libraries are installed as per requirements.txt.
•	Usage: Each function is designed to be modular and reusable in various workflows.
