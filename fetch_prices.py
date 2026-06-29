import os
import json
import requests
import yfinance as yf

from datetime import datetime

DJANGO_API_URL = os.environ["DJANGO_API_URL"]
WEBHOOK_TOKEN = os.environ["WEBHOOK_TOKEN"]


AGRI_SYMBOLS = {
    "Corn": "ZC=F",
    "Wheat": "ZW=F",
    "Soybeans": "ZS=F",
    "Soybean Meal": "ZM=F",
    "Soybean Oil": "ZL=F",
    "Rice": "ZR=F",
    "Oats": "ZO=F",

    "Coffee Arabica": "KC=F",
    "Sugar": "SB=F",
    "Cocoa": "CC=F",
    "Cotton": "CT=F",
    "Orange Juice": "OJ=F",

    "Live Cattle": "LE=F",
    "Lean Hogs": "HE=F"
}

DIRECT_PAIRS = {
    "EUR/USD": "EURUSD=X",
    "GBP/USD": "GBPUSD=X",
    "USD/JPY": "USDJPY=X",
    "USD/CHF": "USDCHF=X",
    "AUD/USD": "AUDUSD=X",

    "EUR/GBP": "EURGBP=X",
    "EUR/JPY": "EURJPY=X",
    "EUR/CHF": "EURCHF=X",
    "EUR/AUD": "EURAUD=X",

    "GBP/JPY": "GBPJPY=X",
    "GBP/CHF": "GBPCHF=X",
    "GBP/AUD": "GBPAUD=X",

    "CHF/JPY": "CHFJPY=X",
    "AUD/JPY": "AUDJPY=X",
    "AUD/CHF": "AUDCHF=X"
}

def get_price(symbol):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")

        if data.empty:
            return None

        return float(data["Close"].iloc[-1])

    except Exception as e:
        print(f"Error for {symbol}: {e}")
        return None


def fetch_all():
    result = {}

    print("START FETCHING ALL PRICES...")

    # commodities
    for name, symbol in AGRI_SYMBOLS.items():
        price = get_price(symbol)
        result[name] = price
        print(f"{name}: {price}")

    # forex
    for name, symbol in DIRECT_PAIRS.items():
        price = get_price(symbol)
        result[name] = price
        print(f"{name}: {price}")

    output = {
        "timestamp": datetime.utcnow().isoformat(),
        "prices": result
    }

    return output


if __name__ == "__main__":
    data = fetch_all()

    print("\nFINAL JSON:\n")
    print(json.dumps(data, indent=2))
