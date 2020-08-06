# Stock Diversity
Stock Diversity is a tool designed for financial analysis. It grabs data for tickers and generates a heatmap to visualize the relationship between each stock.

##How it Works
First User Inputs:
*Start Date
*End Date
*String with Ticker Symbols

Generates  clustered heat map that visualizes the relationships between different stocks in a set time frame.
All stock data is pulled from Yahoo Finance.
The algorithim uses the Pearson Correlation coefficient on daily percentage returns to fidn relationships between stocks.
Ward clustering is implemented to find which stocks are closely related and then the data is shown as a heatmap.
