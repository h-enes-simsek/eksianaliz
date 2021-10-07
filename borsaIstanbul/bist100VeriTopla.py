import yfinance as yf

msft = yf.Ticker("^XU100")

# get stock info
msft.info

# get historical market data
hist = msft.history(period="max")

print(hist)

hist.to_csv("bist100.csv", header=True, index=True)
