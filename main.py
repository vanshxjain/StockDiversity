import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def generateMap(stockDF):
	cmap= sns.diverging_palette(15,145,n=100)

	stockmap = sns.clustermap(stockDF.pct_change().corr(),
		cmap=cmap,method='ward',vmin=-1,vmax=1, annot = True)
	return stockmap
def getData(tick,start,stop):
	stocks = yf.download(tick,start=start,end=stop)
	stocks = stocks['Close']
	return stocks
def main():
	startDate= input('Enter your Start Date (mm/dd/yyyy): ')
	startDate = startDate.split('/')
	startDate = str(startDate[2]+'-'+startDate[0]+'-'+startDate[1])
	endDate= input('Enter your End Date (mm/dd/yyyy): ')
	endDate = endDate.split('/')
	endDate = str(endDate[2]+'-'+endDate[0]+'-'+endDate[1])
	print('Enter a list of tickers you would like to evaluate. (AAPL, BRK-B, TSLA,.etc)')
	tickers = input('Enter a list of comma seperated stock tickers: ')
	generateMap(getData(tickers,startDate,endDate))
	plt.show()
main()
