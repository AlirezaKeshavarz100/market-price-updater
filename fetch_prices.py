import yfinance as yf

print("STARTING DATA FETCH...")

ticker = yf.Ticker("ZC=F")

data = ticker.history(period="1d")

print(data)

print("DONE")
