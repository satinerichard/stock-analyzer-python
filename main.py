import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class StockAnalyzer: 
    def __init__(self, symbol):
        self.symbol = symbol.upper()
        self.data = None

    def fetch_data(self, period='1y'):
        """fetch data from Yahoo Finance"""
        try:
            ticker = yf.Ticker(self.symbol)
            self.data = ticker.history(period=period)
            print(f"Data for {self.symbol} fetched successfully.")
            return self.data
        except Exception as e:
            print(f"Error fetching data for {self.symbol}: {e}")
            return None
    
    def calculate_daily_returns(self):
        """calculate daily returns"""
        if self.data is not None:
            self.data['Daily Return'] = self.data['Close'].pct_change()
            print("Daily returns calculated.")
            return self.data['Daily Return']
        else:
            print("Data not available. Please fetch data first.")
            return None
        
    def calculate_moving_average(self, window=20):
        """calculate moving average"""
        if self.data is not None:
            self.data[f'MA_{window}'] = self.data['Close'].rolling(window=window).mean()
            print(f"{window}-day moving average calculated.")
            return self.data[f'MA_{window}']
        else:
            print("Data not available. Please fetch data first.")
            return None
    
    def print_statistics(self):
        """print basic statistics"""
        if self.data is not None:
            avg_return = self.data['Daily Return'].mean()
            volatility = self.data['Daily Return'].std()
            print(f"Average Daily Return: {avg_return:.4f}")    
            print(f"Volatility (Std Dev of Daily Returns): {volatility:.4f}")
        else:
            print("Data not available. Please fetch data first.")
        

if __name__ == "__main__":
    print("Stock Analyzer starting...")
    symbol = input("Enter stock symbol (e.g., AAPL): ")
    analyzer = StockAnalyzer(symbol)
    data = analyzer.fetch_data("6mo")
    if data is not None:
        analyzer.calculate_daily_returns()
        analyzer.calculate_moving_average(20)
        analyzer.print_statistics()

        print(data.head())
        plt.figure(figsize=(10, 5))
        plt.plot(data.index, data['Close'], label='Close Price')
        plt.plot(data.index, data['MA_20'], label='20-Day MA', linestyle='--')
        plt.title(f"{analyzer.symbol} Stock Price")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.grid()
        plt.show()