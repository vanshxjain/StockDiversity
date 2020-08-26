# Stock Diversity
Stock Diversity is a tool designed for financial analysis. It grabs data for tickers and generates a heatmap to visualize the relationship between each stock.

## Instructions
Simply run main.py and follow the instructions.

Libraries Needed:
- yfinance
- pandas
- seaborn
- matplotlib

Notation :

pip install **library** 

or

(If using Anaconda)
conda install **library**

conda install -c ranaroussi yfinance
***only for yfinance library***

## How to Read the Map
Consider the following example output:
![Example](/Example_Result.png)

The above cluster-map shows the correlation coefficients of each stock with one another after being hierarchically clustered. Each box is shaded proportionally to the strength of the correlation of those two stocks and then the stocks are grouped together to see which companies overall showed the most similar performance over the selected timeframe. For example, we can see that Apple (AAPL) and Amazon (AMZN) are grouped right next to each other. This means that on average, the stocks of Apple and Amazon tend to trend in the same direction. On the contrary, if we take a look at Apple (AAPL) and Ford (F) they are on polar opposites of the plot, indicating that they do not behave similarly on any average trading day.

## How it Works / Our Goal
User Inputs:
* Start Date
* End Date
* String with Ticker Symbols

Output:
- Clustered Heat Map

The purpose of this application is to allow for a visualization of ones stock portfolio and to predict how each individual stock would behave on a given trading day. The user can use this tool to diversify their portfolio by aiming to have a low correlation between most of their stocks (a lighter colored graph) so that their investments are spread across a wide variety of sectors and can have a lower risk factor if a certain industry crashes.
