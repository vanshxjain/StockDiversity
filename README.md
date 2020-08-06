# Stock Diversity
Stock Diversity is a tool designed for financial analysis. It grabs data for tickers and generates a heatmap to visualize the relationship between each stock.

## Instructions
Simply run main.py and follow the instructions.

Libraries that need to be installed:

Notation : pip install **library** 

- yfinance
- pandas
- seaborn
- matplotlib

## How it Works
User Inputs:
* Start Date
* End Date
* String with Ticker Symbols

Output:
- Clustered Heat Map

Using the yfinance API, the data for each ticker is downloaded. We then find the daily percentage change and use this data to calculate the Pearson Correlation Coefficient between the stocks. Ward clustering is applied to return a neatly organized heatmap

