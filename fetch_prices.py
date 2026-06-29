import yfinance as yf

print("Getting price...")

ticker = yf.Ticker("ZC=F")

data = ticker.history(period="1d")

print(data)

print("Done")
