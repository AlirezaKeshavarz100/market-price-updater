import yfinance as yf

ticker = yf.Ticker("ZC=F")

print("Getting price...")

print(ticker.fast_info)
