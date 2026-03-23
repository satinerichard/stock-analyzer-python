# Python stock market analyzer
An object-oriented Python tool designed to fetch stock market data, perform technical analysis and visualize price trends using real financial data from Yahoo Finance.
This project allows the user to enter a stock symbol (AAPL, GOOGL, ACN) and performs basic financial analysis such as returns, volatility and moving averages. It also generates a visualization of stock prices trend over the last 6 months.



## Built with

**Tech used:** Python, pandas, matplotlib, yfinance

To build this stock analyzer I created a class StockAnalyzer with severals methods in it. I used fetch_data to connect to the yfinance API  and get data from the it. The method calculate_daily_returns computes the percentage changes, calculate_moving_average performs a rolling mean (AM) and print_statistics outputs mean return and volatility. I used matplotlib to generate a time-series plot. 


## Getting started 

**Prerequisites**

Make sure you have:
- Python
- pip

**Installation**

1) Clone the repository
```bash
git clone https://github.com/satinerichard/stock-analyzer-python.git
cd stock-amalyzer-python
```

2) Install depedencies
```bash
pip install yfinance pandas matplotlib
```

**Usage**

1) Run the program
```bash
python3 main.py
```

2) Enter a stock symbol when prompted(e.g. AAPL, GOOGL)

3) The script will output statistics in the terminal and open a window with the plot.



**Example output**

If the user enters AAPL:





